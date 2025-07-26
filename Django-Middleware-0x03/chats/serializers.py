from rest_framework import serializers
from .models import User, Conversation, Message
from django.core.exceptions import ValidationError as DjangoValidationError

class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    role_display = serializers.SerializerMethodField()
    password = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'},
        min_length=8,
        error_messages={
            'min_length': 'Password must be at least 8 characters long.'
        }
    )
    
    class Meta:
        model = User
        fields = [
            'user_id', 'first_name', 'last_name', 'full_name', 
            'email', 'phone_number', 'role', 'role_display',
            'password', 'created_at'
        ]
        extra_kwargs = {
            'user_id': {'read_only': True},
            'created_at': {'read_only': True}
        }

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"

    def get_role_display(self, obj):
        return obj.get_role_display()

    def validate_email(self, value):
        if User.objects.filter(email__iexact=value).exists():
            raise serializers.ValidationError("This email is already in use.")
        return value

class MessageSerializer(serializers.ModelSerializer):
    formatted_time = serializers.SerializerMethodField()
    message_body = serializers.CharField(
        max_length=2000,
        error_messages={
            'max_length': 'Message cannot exceed 2000 characters.'
        }
    )
    
    class Meta:
        model = Message
        fields = [
            'message_id', 'sender', 'message_body', 
            'sent_at', 'formatted_time'
        ]
        extra_kwargs = {
            'message_id': {'read_only': True},
            'sender': {'read_only': True},
            'sent_at': {'read_only': True}
        }

    def get_formatted_time(self, obj):
        return obj.sent_at.strftime("%b %d, %Y %I:%M %p")

class ConversationSerializer(serializers.ModelSerializer):
    participant_count = serializers.SerializerMethodField()
    conversation_id = serializers.CharField(
        required=False,
        allow_null=True,
        read_only=True
    )
    
    class Meta:
        model = Conversation
        fields = [
            'conversation_id', 'participants', 
            'messages', 'participant_count', 'created_at'
        ]
        extra_kwargs = {
            'created_at': {'read_only': True}
        }

    def get_participant_count(self, obj):
        return obj.participants.count()

    def validate(self, data):
        participants = data.get('participants', [])
        if len(participants) < 2:
            raise serializers.ValidationError(
                "A conversation must have at least 2 participants."
            )
        return data

class MessageCreateSerializer(serializers.Serializer):
    message_body = serializers.CharField(
        max_length=2000,
        required=True,
        error_messages={
            'blank': 'Message cannot be empty.',
            'required': 'Message content is required.'
        }
    )
    
    def validate(self, data):
        try:
            if not data['message_body'].strip():
                raise serializers.ValidationError(
                    {"message_body": "Message cannot be empty."}
                )
        except KeyError:
            raise serializers.ValidationError(
                {"message_body": "This field is required."}
            )
        return data

    def create(self, validated_data):
        try:
            return Message.objects.create(**validated_data)
        except DjangoValidationError as e:
            raise serializers.ValidationError(str(e))
from rest_framework import viewsets, status, filters
from rest_framework.response import Response
from rest_framework.decorators import action, api_view
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth import authenticate
from .auth import get_tokens_for_user
from .models import Conversation, Message
from .serializers import (
    ConversationSerializer,
    MessageSerializer,
    ConversationCreateSerializer,
    MessageCreateSerializer
)

@api_view(['POST'])
def jwt_login(request):
    """Custom JWT login using email/password"""
    email = request.data.get('email')
    password = request.data.get('password')
    
    user = authenticate(email=email, password=password)
    if not user:
        return Response(
            {"detail": "Invalid credentials"},
            status=status.HTTP_401_UNAUTHORIZED
        )
        
    tokens = get_tokens_for_user(user)
    return Response(tokens, status=status.HTTP_200_OK)

class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.prefetch_related('participants', 'messages').all()
    serializer_class = ConversationSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['participants__id', 'created_at']
    ordering_fields = ['created_at']
    search_fields = ['participants__first_name', 'participants__last_name', 'participants__email']

    def get_serializer_class(self):
        if self.action == 'create':
            return ConversationCreateSerializer
        return super().get_serializer_class()

    @action(detail=True, methods=['post'])
    def send_message(self, request, pk=None):
        conversation = self.get_object()
        serializer = MessageCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        message = Message.objects.create(
            conversation=conversation,
            sender=request.user,
            message_body=serializer.validated_data['message_body']
        )
        
        return Response(
            MessageSerializer(message).data,
            status=status.HTTP_201_CREATED
        )

class MessageViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = MessageSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['sender__id', 'sent_at']
    ordering_fields = ['sent_at']

    def get_queryset(self):
        conversation_id = self.kwargs['conversation_pk']
        return Message.objects.filter(
            conversation_id=conversation_id
        ).select_related('sender')

    def get_serializer_context(self):
        return {'request': self.request}
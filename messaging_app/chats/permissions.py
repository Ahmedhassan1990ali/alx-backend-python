from rest_framework import permissions

class IsParticipant(permissions.BasePermission):
    """Check if user is a conversation participant"""
    def has_object_permission(self, request, view, obj):
        return request.user in obj.participants.all()
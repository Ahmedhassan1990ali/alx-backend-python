from rest_framework import permissions

class IsParticipantOfConversation(permissions.BasePermission):
    """Allow access only to conversation participants"""
    def has_permission(self, request, view):
        # DRF's IsAuthenticated handles the auth check
        return request.user and request.user.is_authenticated
    
    def has_object_permission(self, request, view, obj):         
        # Always allow safe methods (GET, HEAD, OPTIONS)
        if request.method in permissions.SAFE_METHODS:
            return True

        # Method verification
        if request.method in ["PUT", "PATCH", "DELETE"]:
            # Conversation access check
            if hasattr(obj, 'participants'):
                return request.user in obj.participants.all()
            
            # Message access check
            if hasattr(obj, 'conversation'):
                return request.user in obj.conversation.participants.all()

        return False
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.conf import settings

def get_tokens_for_user(user):
    """Generate JWT tokens with custom claims"""
    refresh = RefreshToken.for_user(user)
    
    # Add custom claims
    refresh['email'] = user.email
    refresh['role'] = user.role
    refresh['name'] = f"{user.first_name} {user.last_name}"
    
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class CustomJWTAuthentication(JWTAuthentication):
    """Enhanced JWT auth with:
    - Stricter header validation
    - User activity tracking
    """
    
    def authenticate(self, request):
        try:
            header = self.get_header(request)
            if header is None:
                return None

            raw_token = self.get_raw_token(header)
            if raw_token is None:
                return None

            validated_token = self.get_validated_token(raw_token)
            user = self.get_user(validated_token)
            
            # Update last_login on token use
            if getattr(settings, 'UPDATE_LAST_LOGIN_ON_AUTH', False):
                user.save_last_login()
                
            return (user, validated_token)
        except Exception as e:
            raise AuthenticationFailed(str(e))
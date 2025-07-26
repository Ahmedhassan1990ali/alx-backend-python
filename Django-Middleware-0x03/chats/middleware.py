from datetime import datetime, time
import logging
from django.http import HttpResponseForbidden
from django.core.cache import cache

logger = logging.getLogger('request_logger')

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Get user info
        user = "Anonymous"
        if hasattr(request, 'user') and request.user.is_authenticated:
            user = request.user.email
        
        # Log the request
        logger.info(f"{datetime.now()} - User: {user} - Path: {request.path}")
        
        response = self.get_response(request)
        return response
    

class RestrictAccessByTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.restricted_start = time(21, 0)  # 9 PM
        self.restricted_end = time(18, 0)    # 6 PM

    def __call__(self, request):
        from datetime import datetime
        now = datetime.now().time()
        
        # Check if current time is between 9 PM and 6 AM (overnight restriction)
        if (now >= self.restricted_start) or (now <= self.restricted_end):
            if request.path.startswith('/api/conversations/') or request.path.startswith('/api/messages/'):
                return HttpResponseForbidden(
                    "Chat access is restricted between 9 PM and 6 AM"
                )
        
        return self.get_response(request)
    

class OffensiveLanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.limit = 5  # Messages per minute
        self.window = 60  # Seconds

    def __call__(self, request):
        # Only check message sending requests
        if request.method == 'POST' and any(
            path in request.path 
            for path in ['/api/messages/', '/send_message/']
        ):
            ip = self.get_client_ip(request)
            cache_key = f'message_count_{ip}'
            
            # Get or initialize count
            count = cache.get(cache_key, 0)
            
            if count >= self.limit:
                return HttpResponseForbidden(
                    "Message limit exceeded. Please wait before sending more messages."
                )
            
            # Increment count
            cache.set(
                key=cache_key,
                value=count + 1,
                timeout=self.window
            )
        
        return self.get_response(request)

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        return x_forwarded_for.split(',')[0] if x_forwarded_for else request.META.get('REMOTE_ADDR')

class RolepermissionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.admin_paths = [
            '/api/admin/',
            '/api/conversations/delete/',
            '/api/users/'
        ]
        self.moderator_paths = [
            '/api/messages/delete/',
            '/api/reports/'
        ]

    def __call__(self, request):
        # Skip for non-protected paths
        if not any(
            request.path.startswith(path) 
            for path in self.admin_paths + self.moderator_paths
        ):
            return self.get_response(request)

        # Check authentication
        if not request.user.is_authenticated:
            return HttpResponseForbidden("Authentication required")

        # Admin-only paths
        if any(request.path.startswith(path) for path in self.admin_paths):
            if request.user.role != 'admin':
                return HttpResponseForbidden("Admin privileges required")

        # Moderator paths (moderator or admin)
        if any(request.path.startswith(path) for path in self.moderator_paths):
            if request.user.role not in ['admin', 'moderator']:
                return HttpResponseForbidden("Moderator privileges required")

        return self.get_response(request)
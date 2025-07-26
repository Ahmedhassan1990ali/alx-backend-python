from datetime import datetime, time
import logging
from django.http import HttpResponseForbidden

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
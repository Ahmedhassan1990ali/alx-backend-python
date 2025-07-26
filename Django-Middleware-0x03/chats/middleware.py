from datetime import datetime
import logging

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
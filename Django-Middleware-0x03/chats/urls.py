from django.urls import path, include
from rest_framework_nested import routers
from .views import jwt_login, ConversationViewSet, MessageViewSet

router = routers.DefaultRouter()
router.register(r'conversations', ConversationViewSet, basename='conversation')
conversations_router = routers.NestedDefaultRouter(
    router, 
    r'conversations', 
    lookup='conversation'
)
conversations_router.register(
    r'messages', 
    MessageViewSet, 
    basename='conversation-messages'
)


urlpatterns = [
    path('auth/login/', jwt_login, name='jwt-login'),
    path('', include(router.urls)),
    path('', include(conversations_router.urls)),
    path(
        'conversations/<uuid:conversation_pk>/send_message/',
        ConversationViewSet.as_view({'post': 'send_message'}),
        name='conversation-send-message'
    ),
]




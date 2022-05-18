from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import MessageView, UserRegisterView

urlpatterns = [
    path('api/message/', MessageView.as_view()),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('api/register/', UserRegisterView.as_view()),
]
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import UserLoginView, UserRegisterView, UserProfileAPIView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login-view'),
    path('profile/', UserProfileAPIView.as_view(), name='profile-view'),
]

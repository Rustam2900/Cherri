from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import UserLoginView

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login-view'),
]

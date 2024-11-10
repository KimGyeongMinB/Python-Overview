from django.urls import path
from .views import LoginView, SignUpView, UserProfileView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),  # signup
    path("login/", LoginView.as_view(), name="token_obtain_pair"), # login
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"), # refresh token
    path('profile/', UserProfileView.as_view(), name='profile'),  # 사용자 프로필 URL
]
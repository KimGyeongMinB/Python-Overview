from django.urls import path
from .views import LoginView, SignUpView
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),  # signup
    path("login/", LoginView.as_view(), name="token_obtain_pair"), # login
]
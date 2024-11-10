from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSignupSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import LoginSerializer

class SignUpView(APIView):
    def post(self,request):
        serializer = UserSignupSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            data = serializer.data.copy()
            return Response(data, status=status.HTTP_201_CREATED)
        
        # 유효하지 않을 때의 응답 반환
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer # login custom

from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

# SignUp
class UserSignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    roles = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['username', 'password', 'nickname', 'roles']

    def create(self,validated_data):
        user = User(
            username=validated_data['username'],
            nickname=validated_data['nickname']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    def validate_username(self, value):
        if not value.replace(" ", "").isalnum():  # 공백을 제외하고 알파벳과 숫자로 구성된지 확인
            raise serializers.ValidationError("잘못된 정보를 입력하셨습니다")
        return value
    
    def get_roles(self, obj):
        # obj = User
        return [{"role": obj.roles}]

    
class LoginSerializer(TokenObtainPairSerializer):
    # 검증된 정보 가져오기
    def validate(self, attrs):
        data = super().validate(attrs)

        # 'access' 키를 'token'으로 변경하여 반환
        return {"token": data['access']}
    
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','nickname']
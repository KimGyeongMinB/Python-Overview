import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

@pytest.mark.django_db
def test_signup():
    client = APIClient()
    data = {
        "username": "JIN HO",
        "password": "12341234",
        "nickname": "Mentos"
    }
    response = client.post('/api/accounts/signup/', data, format='json')

    assert response.status_code == 201
    assert response.data['username'] == 'JIN HO'
    assert response.data['nickname'] == 'Mentos'

    # 데이터베이스에 사용자 확인
    user = User.objects.filter(username='JIN HO').first()
    assert user is not None
    assert user.check_password('12341234')

@pytest.mark.django_db
def test_login():
    # 테스트 사용자 생성
    user = User.objects.create_user(username='JIN HO', password='12341234')
    user.is_active = True
    user.save()

    client = APIClient()
    data = {
        "username": "JIN HO",
        "password": "12341234"
    }
    response = client.post('/api/accounts/login/', data, format='json')

    assert response.status_code == 200
    assert 'token' in response.data
    token = response.data['token']  # 토큰 저장

@pytest.fixture
def get_tokens(db):
    # create user and generate access/refresh tokens
    user = User.objects.create_user(username='JIN HO', password='12341234')
    refresh = RefreshToken.for_user(user)
    return {
        "token": str(refresh.access_token),
        "refresh": str(refresh)
    }

@pytest.mark.django_db
def test_access_refresh_token_issue():
    user = User(username='JIN HO')
    user.set_password('12341234')  # 비밀번호 암호화 저장
    user.is_active = True  # 사용자 활성화
    user.save()

    client = APIClient()
    url = reverse('token_obtain_pair')
    data = {
        "username": "JIN HO",
        "password": "12341234"
    }
    response = client.post(url, data, format='json')

    print(response.data)


    assert response.status_code == 200
    assert 'token' in response.data

@pytest.mark.django_db
def test_token_validation(get_tokens):
    client = APIClient()
    access_token = get_tokens['token']
    url = reverse('profile') 

    client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
    response = client.get(url)

    assert response.status_code == 200

@pytest.mark.django_db
def test_refresh_token(get_tokens):
    client = APIClient()
    refresh_token = get_tokens['refresh']
    url = reverse('token_refresh')
    data = {
        "refresh": refresh_token
    }
    response = client.post(url, data, format='json')

    assert response.status_code == 200
    assert 'access' in response.data

@pytest.mark.django_db
def test_invalid_token():
    client = APIClient()
    url = reverse('profile')

    client.credentials(HTTP_AUTHORIZATION='Bearer invalidtoken')
    response = client.get(url)

    assert response.status_code == 401

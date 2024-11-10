from django.test import TestCase
import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

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

    # 데이터베이스에 사용자 생성 확인
    user = User.objects.filter(username='JIN HO').first()
    assert user is not None
    assert user.check_password('12341234') 


@pytest.mark.django_db
def test_login():
    # 테스트 사용자 생성
    user = User.objects.create_user(username='JIN HO', password='12341234')
    client = APIClient()
    data = {
        "username": "JIN HO",
        "password": "12341234"
    }
    response = client.post('/api/accounts/login/', data, format='json')

    assert response.status_code == 200
    assert 'token' in response.data

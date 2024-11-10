# Python-Overview
# Test Scenarios

<br>

# 1. Signup Test Scenarios
  클라이언트를 통해 회원가입 endpoint에 POST요청
  201 stauts_code
  사용자의 입력정보를 받아옴
  DB에서 확인 후 password hash

<br>
<br>


# 2. Login Test Scenarios
  클라이언트를 통해 사용자 정보 입력 후 POST 요청
  200 stauts_code
  token 유무 확인 후 저장

<br> 
<br>


# 3. Access_Token/Refresh_Token 
  로그인 시 token(access_token)/refresh_token 생성
  token이 유효할 시 200 status_code
  refresh_token 유효할 시 200 status_code
  token이 올바르지 않은 경우 401 status_code

<br>
<br>

# Middleware
  Django의 입력 또는 출력을 전역적으로 변경하기 위한 가볍고 낮은 수준의 "플러그인" 시스템
## 역할
- **요청 처리** : 클라이언트로부터의 요청이 Django 애플리케이션에 도달하면, 미들웨어는 요청을 처리하기 위해 순차적으로 실행
- **응답 처리** : Django 애플리케이션이 응답을 생성하면, 미들웨어는 이 응답을 수정하거나 추가 작업을 수행할 기회를 가짐

## Middleware 와 Decorators
  Dacorators는 특정 뷰 함수에 특정 기능을 적용하기 위해서 쓰임
  Middleware는 전역적으로 적용

# Django
Django는 Python 기반의 오픈 소스 웹 프레임워크로, 웹 애플리케이션 개발을 빠르고 효율적으로 할 수 있도록 지원.

## 특징
- **MTV 패턴**: Model, Template, View 패턴을 사용하여 유지 보수성을 높입니다.
- **ORM (Object-Relational Mapping)**: 데이터베이스 테이블을 Python 객체로 매핑하여 SQL 없이 데이터베이스 작업을 할 수 있습니다.

# JWT
Json Web Token의 약자로 일반적으로 클라이언트와 서버 사이에서 통신할 때 권한을 위해 사용하는 토큰
JWT는 헤더(header), 페이로드(payload), 서명(signature) 로 구성

## 헤더 (Header)
어떠한 알고리즘으로 암호화 할 것인지, 어떠한 토큰을 사용할 것 인지에 대한 정보가 들어있다. 

## 정보 (Payload)
전달하려는 정보
payload에 있는 내용은 수정이 가능하여 더 많은 정보를 추가할 수 있다. 그러나 노출과 수정이 가능한 지점이기 때문에 인증이 필요한 최소한의 정보만을 담아야 한다.

## 서명 (Signature)
가장 중요한 부분으로 헤더와 정보를 합친 후 발급해준 서버가 지정한 secret key로 암호화 시켜 토큰을 변조하기 어렵게 만들어준다.

<br>

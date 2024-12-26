# Sparta Market DRF API

Django REST Framework를 사용한 중고거래 플랫폼 API 서버입니다.

## 프로젝트 소개

스파르타 코딩클럽 회원들을 위한 중고거래 플랫폼의 백엔드 API를 제공합니다.

## 기술 스택

- Python 3.9+
- Django 4.2
- Django REST Framework
- SQLite3

## API 명세

### 회원 관리

#### 회원가입
- **Endpoint**: `/api/accounts/signup/`
- **Method**: POST
- **Body**:
  ```json
  {
    "username": "string",
    "password": "string",
    "password2": "string",
    "email": "user@example.com",
    "nickname": "string",
    "birth_date": "YYYY-MM-DD"
  }
  ```

#### 로그인
- **Endpoint**: `/api/accounts/login/`
- **Method**: POST
- **Body**:
  ```json
  {
    "username": "string",
    "password": "string"
  }
  ```

### 상품 관리

#### 상품 목록 조회
- **Endpoint**: `/api/products/`
- **Method**: GET
- **Auth**: 불필요

#### 상품 상세 조회
- **Endpoint**: `/api/products/{id}/`
- **Method**: GET
- **Auth**: 불필요

#### 상품 등록
- **Endpoint**: `/api/products/`
- **Method**: POST
- **Auth**: 필요
- **Body**: form-data
  - title: string
  - content: string
  - price: integer
  - image: file

#### 상품 수정
- **Endpoint**: `/api/products/{id}/`
- **Method**: PUT
- **Auth**: 필요 (작성자만 가능)
- **Body**: form-data
  - title: string
  - content: string
  - price: integer
  - image: file (선택)

#### 상품 삭제
- **Endpoint**: `/api/products/{id}/`
- **Method**: DELETE
- **Auth**: 필요 (작성자만 가능)

## 설치 및 실행 방법

1. 저장소 클론
```bash
git clone https://github.com/your-username/spartamarket_drf.git
cd spartamarket_drf
```

2. 가상환경 생성 및 활성화
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. 필요한 패키지 설치
```bash
pip install -r requirements.txt
```

4. 데이터베이스 마이그레이션
```bash
python manage.py makemigrations
python manage.py migrate
```

5. 서버 실행
```bash
python manage.py runserver
```

## API 테스트

API 테스트는 Postman을 사용하여 진행할 수 있습니다.

1. Postman 설치
2. 새로운 Collection 생성
3. 각 API 엔드포인트에 대한 요청 생성
4. 인증이 필요한 요청의 경우, Headers에 Token 추가:
   ```
   Authorization: Token your_token_here
   ```

## 프로젝트 구조
```
spartamarket_drf/
├── accounts/              # 사용자 관련 앱
├── products/             # 상품 관련 앱
├── spartamarket_drf/    # 프로젝트 설정
├── manage.py
├── requirements.txt
└── README.md
```

## 환경 변수
- DEBUG=True
- SECRET_KEY='your-secret-key'

## 라이센스
This project is licensed under the MIT License

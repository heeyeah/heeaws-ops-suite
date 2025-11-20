# heeaws-ops-suite

Operations Suite API Server

## 프로젝트 구조

```
heeaws-ops-suite/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI 메인 애플리케이션
│   ├── api/
│   │   ├── __init__.py
│   │   └── routes.py        # API 라우트 정의
│   └── core/
│       ├── __init__.py
│       └── config.py        # 애플리케이션 설정
├── requirements.txt         # Python 의존성
├── Dockerfile              # Docker 이미지 빌드 파일
├── docker-compose.yml      # Docker Compose 설정
└── README.md
```

## 로컬 개발 환경 설정

### 빠른 시작 (자동 설치 스크립트 사용)

**Windows PowerShell:**
```powershell
# 1. 환경 설정 및 의존성 설치
.\setup.ps1

# 2. 서버 실행
.\run.ps1
```

**Windows CMD:**
```cmd
# 1. 환경 설정 및 의존성 설치
setup.bat

# 2. 서버 실행
run.bat
```

> **참고:** Python이 설치되어 있지 않다면 [Python 3.11 이상](https://www.python.org/downloads/)을 먼저 설치해주세요.

### 수동 설정

#### 1. 가상 환경 생성 및 활성화

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

#### 2. 의존성 설치

```bash
pip install -r requirements.txt
```

#### 3. 서버 실행

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## Docker를 사용한 실행

### Docker Compose 사용 (권장)

```bash
# 이미지 빌드 및 컨테이너 실행
docker-compose up -d

# 로그 확인
docker-compose logs -f

# 컨테이너 중지
docker-compose down
```

### Docker 직접 사용

```bash
# 이미지 빌드
docker build -t heeaws-ops-suite:latest .

# 컨테이너 실행
docker run -d -p 8000:8000 --name heeaws-ops-suite-api heeaws-ops-suite:latest
```

## API 문서

서버 실행 후 다음 URL에서 API 문서를 확인할 수 있습니다:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 주요 엔드포인트

- `GET /` - 루트 엔드포인트
- `GET /health` - 헬스 체크
- `GET /api/v1/` - API 루트
- `GET /api/v1/status` - 상태 조회

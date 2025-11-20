"""
heeaws-ops-suite API 서버 메인 애플리케이션
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import routes
from app.core.config import settings

app = FastAPI(
    title="heeaws-ops-suite API",
    description="Operations Suite API Server",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API 라우터 등록
app.include_router(routes.router, prefix="/api/v1", tags=["api"])


@app.get("/")
async def root():
    """루트 엔드포인트"""
    return {
        "message": "heeaws-ops-suite API Server",
        "version": "1.0.0",
        "docs": "/docs"
    }


@app.get("/health")
async def health_check():
    """헬스 체크 엔드포인트"""
    return {"status": "healthy"}


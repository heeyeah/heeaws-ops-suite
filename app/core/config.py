"""
애플리케이션 설정
"""
from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    """애플리케이션 설정 클래스"""
    
    # 서버 설정
    API_V1_PREFIX: str = "/api/v1"
    PROJECT_NAME: str = "heeaws-ops-suite"
    
    # CORS 설정
    CORS_ORIGINS: List[str] = ["*"]
    
    # 서버 포트
    PORT: int = 8000
    HOST: str = "0.0.0.0"
    
    # 환경
    ENVIRONMENT: str = "development"
    DEBUG: bool = True
    
    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()


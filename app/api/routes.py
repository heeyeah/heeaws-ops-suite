"""
API 라우트 정의
"""
from fastapi import APIRouter
from typing import Dict

router = APIRouter()


@router.get("/")
async def api_root() -> Dict[str, str]:
    """API 루트 엔드포인트"""
    return {"message": "heeaws-ops-suite API v1"}


@router.get("/status")
async def get_status() -> Dict[str, str]:
    """상태 조회 엔드포인트"""
    return {"status": "operational"}


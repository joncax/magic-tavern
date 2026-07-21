"""Mercado Dinamico - precos flutuantes (atualizados por CronJob, nao aqui)."""
from fastapi import APIRouter

router = APIRouter(prefix="/market", tags=["market"])


@router.get("/prices")
def get_current_prices():
    raise NotImplementedError

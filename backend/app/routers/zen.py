"""Modo Zen - infinito, customizavel, sem recompensas de campanha."""
from fastapi import APIRouter

router = APIRouter(prefix="/zen", tags=["zen"])


@router.post("/session")
def create_zen_session():
    raise NotImplementedError

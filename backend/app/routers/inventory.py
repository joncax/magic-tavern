"""Livro de Registos - inventario do jogador."""
from fastapi import APIRouter

router = APIRouter(prefix="/inventory", tags=["inventory"])


@router.get("")
def get_inventory():
    raise NotImplementedError


@router.post("/sell")
def sell_items():
    raise NotImplementedError

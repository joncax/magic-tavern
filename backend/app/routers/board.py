"""Quadro de Avisos - missoes de entrega para escoar inventario."""
from fastapi import APIRouter

router = APIRouter(prefix="/board", tags=["board"])


@router.get("/quests")
def list_quests():
    raise NotImplementedError


@router.post("/quests/{quest_id}/deliver")
def deliver_quest(quest_id: int):
    raise NotImplementedError

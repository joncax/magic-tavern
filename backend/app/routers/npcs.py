"""Viajantes (NPCs) e afinidade."""
from fastapi import APIRouter

router = APIRouter(prefix="/npcs", tags=["npcs"])


@router.get("")
def list_npcs():
    raise NotImplementedError

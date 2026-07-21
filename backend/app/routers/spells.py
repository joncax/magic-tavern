"""Spells (power-ups): Identify, Magic Missile, Haste, Prestidigitation."""
from fastapi import APIRouter

router = APIRouter(prefix="/spells", tags=["spells"])


@router.post("/{spell_type}/use")
def use_spell(spell_type: str):
    raise NotImplementedError

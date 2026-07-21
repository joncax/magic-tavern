"""Diario da Taverna (modo campanha) - geracao on-demand de niveis."""
from fastapi import APIRouter

router = APIRouter(prefix="/levels", tags=["levels"])


@router.get("/next")
def get_next_level():
    """Gera e devolve o proximo nivel on-demand (grid, regras, layers)."""
    raise NotImplementedError


@router.post("/{level_id}/complete")
def complete_level(level_id: int):
    """
    Submete o resultado. O servidor NUNCA confia em recompensas vindas do
    cliente - calcula-as sozinho a partir da definicao do nivel na BD.
    """
    raise NotImplementedError


@router.get("/progress")
def get_progress():
    """Progresso no mapa da campanha."""
    raise NotImplementedError

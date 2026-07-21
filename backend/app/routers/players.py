"""Perfis de jogador - "login" simples sem password (ver GDD)."""
from fastapi import APIRouter

router = APIRouter(prefix="/players", tags=["players"])


@router.get("")
def list_players():
    """Lista os perfis existentes para o ecra de selecao."""
    raise NotImplementedError


@router.post("")
def create_player():
    """Cria um novo perfil (nome + avatar, sem password)."""
    raise NotImplementedError


@router.post("/{player_id}/select")
def select_player(player_id: int):
    """'Login': devolve um JWT com o player_id embutido."""
    raise NotImplementedError

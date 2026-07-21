"""
Armario de Artefactos. Sem tabela propria - e uma leitura sobre
player_inventory + items_master filtrada por categoria 'artifact'
(ver player_vault VIEW no schema.sql).
"""
from fastapi import APIRouter

router = APIRouter(prefix="/vault", tags=["vault"])


@router.get("")
def get_vault():
    raise NotImplementedError

from fastapi import FastAPI

from app.core.config import settings
from app.routers import (
    alchemy,
    board,
    inventory,
    levels,
    market,
    npcs,
    players,
    spells,
    vault,
    zen,
)

app = FastAPI(
    title="Magic Tavern API",
    version=settings.APP_VERSION,
    debug=settings.DEBUG,
)

app.include_router(players.router)
app.include_router(levels.router)
app.include_router(zen.router)
app.include_router(inventory.router)
app.include_router(alchemy.router)
app.include_router(vault.router)
app.include_router(market.router)
app.include_router(npcs.router)
app.include_router(board.router)
app.include_router(spells.router)


@app.get("/health")
def health():
    """
    Usado pelo readinessProbe no Helm chart. Deliberadamente simples
    nesta fase (sem check a BD) - o objetivo agora e validar a pipeline
    de CI/CD ponta-a-ponta. Quando os routers tiverem logica real, vale
    a pena reforcar isto com um SELECT 1 e adicionar um Postgres de
    servico ao workflow de CI para o testar em condicoes.
    """
    return {"status": "ok", "version": settings.APP_VERSION}

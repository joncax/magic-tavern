"""Mesa do Alquimista - destilar pocoes e criar artefactos."""
from fastapi import APIRouter

router = APIRouter(prefix="/alchemy", tags=["alchemy"])


@router.get("/recipes")
def list_known_recipes():
    raise NotImplementedError


@router.post("/brew")
def brew_potion():
    raise NotImplementedError


@router.post("/craft-artifact")
def craft_artifact():
    raise NotImplementedError

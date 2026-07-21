"""
Engine e sessao do SQLAlchemy. Sincrono de proposito nesta fase - mais
simples de raciocinar, e a escala (poucos jogadores) nao vai sentir
diferenca de performance face a async.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

engine = create_engine(settings.database_url, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

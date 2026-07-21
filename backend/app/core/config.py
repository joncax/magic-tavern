"""
Configuracao central da app, lida a partir de variaveis de ambiente.
As nao-secretas vem do ConfigMap (backend-configmap.yaml no chart Helm);
as secretas (POSTGRES_PASSWORD, JWT_SECRET_KEY) vem do Secret sincronizado
pelo Infisical Operator.
"""
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(case_sensitive=True)

    # Nao-secretas (ConfigMap)
    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: str = "5432"
    POSTGRES_DB: str = "magic_tavern"
    POSTGRES_USER: str = "tavern_user"
    APP_VERSION: str = "0.1.0"
    DEBUG: bool = False
    JWT_ALGORITHM: str = "HS256"

    # Secretas (Infisical -> Secret k8s)
    POSTGRES_PASSWORD: str = "changeme-local-dev"
    JWT_SECRET_KEY: str = "changeme-local-dev"

    @property
    def database_url(self) -> str:
        return (
            f"postgresql+psycopg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
            f"@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )


settings = Settings()

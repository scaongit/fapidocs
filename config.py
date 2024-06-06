from pydantic import BaseSettings


class Settings(BaseSettings):
    openai_api_key: str
    pinecone_api_key: str
    auth_secret: str
    cloud_storage_url: str

    class Config:
        env_file = ".env"


settings = Settings()

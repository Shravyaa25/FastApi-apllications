from pydantic_settings  import BaseSettings

class Settings(BaseSettings):
    POSTGRES_PORT: int = 5432
    POSTGRES_PASSWORD: str="password"
    POSTGRES_USER:str= "shravyas"
    POSTGRES_DB: str = "books_db"

settings = Settings()

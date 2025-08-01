from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
  model_config = SettingsConfigDict(env_file=".env", extra="ignore")
  
  DATABASE_URL: str
  ENVIRONMENT: str = "development"
  SECRET_KEY: str
  # 다른 환경 변수가 있다면 여기에 추가

settings = Settings()
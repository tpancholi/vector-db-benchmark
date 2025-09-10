from pydantic_settings import BaseSettings


class Settings(BaseSettings):
	TOPK_API_KEY: str
	QDRANT_URL: str
	MILVUS_HOST: str
	MILVUS_PORT: int
	WEAVIATE_URL: str
	EMBEDDING_MODEL: str

	class Config:
		env_file = ".env"
		env_file_encoding = "utf-8"
		case_sensitive = True


settings = Settings()

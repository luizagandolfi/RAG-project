from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv


class ConfigSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env')

    llm_key: str = Field(default="SECRET-KEY", env="LLM_KEY")
    llm_url: str = Field(default="LLM_URL", env="LLM_URL")
    llm: str = Field(default="gpt-4o", env="LLM")
    embedder: str = Field(default="text-embedding-3-small", env="EMBEDDER")
    drive_folder_url: str = Field(default="URL", env="DRIVE_FOLDER_URL")
    docs_dir: str = Field(default="./data/documentos_ambientais", env="DOCS_DIR")
    collection_name: str = Field(default="collection", env="COLLECTION_NAME")
    prompts_resource: str = Field(default="", env="PROMPTS_RESOURCE")


config = ConfigSettings()

""" config.py """

#from functools import lru_cache
#from pydantic import Field
#from pydantic_settings import BaseSettings, SettingsConfigDict
import os
from dotenv import load_dotenv


class Settings():
    load_dotenv()
    ASTRA_DB_KEYSPACE = os.environ['ASTRA_DB_KEYSPACE']
    ASTRA_DB_SECURE_BUNDLE_PATH = os.environ['ASTRA_DB_SECURE_BUNDLE_PATH']
    ASTRA_DB_APPLICATION_TOKEN = os.environ['ASTRA_DB_APPLICATION_TOKEN']
    OPENAI_API_KEY = os.environ['OPENAI_API_KEY']


"""
class Settings(BaseSettings):

    # initialise settings from .env
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

    # first argument of 'Field' is the default
    # environment variable is same as variable name, or overridden using validation_alias
    # ... here means field is required

    ASTRA_DB_KEYSPACE: str = Field(...)
    ASTRA_DB_SECURE_BUNDLE_PATH: str = Field(...)
    ASTRA_DB_APPLICATION_TOKEN: str = Field(...)

    # OpenAI Token
    OPENAI_KEY: str = Field(...)

@lru_cache()
def getSettings():
    return Settings()

    """

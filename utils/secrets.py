from dotenv import load_dotenv
import os
from pathlib import Path


def get_env_pass(key: str):
    dotenv_path = Path(__file__).resolve().parent.parent / ".env"
    load_dotenv(dotenv_path, override=False)
    return os.getenv(key)
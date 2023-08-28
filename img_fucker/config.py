import os
from dynaconf import Dynaconf
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

settings = Dynaconf(
    load_dotenv=True,
    dotenv_path=ROOT_DIR.joinpath("envs", ".env"),
    envvar_prefix_for_dynaconf=False,
)

redis_host = settings('redis_host')
redis_port = settings('redis_port')

api_host = settings('api_host')
api_port = settings('api_port')

API_NINJAS = settings('api_ninjas')
MAIL_VALIDATION = settings('mail_validation')

import functools
import json

from settings import SETTING_PATH
from yaml import safe_load


def get_app_config():
    with open(SETTING_PATH) as file:
        config = safe_load(file)
    return config


def construct_db_url(config):
    dsn = "postgresql+asyncpg://{username}:{password}@{host}:{port}/{database}"
    return dsn.format(**config)


pretty_json = functools.partial(
    json.dumps, indent=4, ensure_ascii=False, default=str
)

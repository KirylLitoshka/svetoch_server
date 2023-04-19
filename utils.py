import functools
import json

from settings import TEST_CONFIG
from sqlalchemy.ext.asyncio import create_async_engine
from yaml import safe_load


def get_app_config():
    with open(TEST_CONFIG) as file:
        config = safe_load(file)
    return config


def construct_db_url(config):
    dsn = "postgresql+asyncpg://{username}:{password}@{host}:{port}/{database}"
    return dsn.format(**config)


async def on_startup(app):
    application_name = app["app_name"]
    config = get_app_config()
    db_url = construct_db_url(config[application_name])
    app['db'] = create_async_engine(db_url, echo=True)


async def on_shutdown(app):
    await app["db"].dispose()


pretty_json = functools.partial(
    json.dumps, indent=4, ensure_ascii=False, default=str
)

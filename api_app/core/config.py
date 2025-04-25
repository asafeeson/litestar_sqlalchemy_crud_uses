import os
from litestar.plugins.sqlalchemy import (
    AsyncSessionConfig,
    SQLAlchemyAsyncConfig,
    SQLAlchemyPlugin,
)

session_config = AsyncSessionConfig(expire_on_commit=False)

DB_USER = os.getenv("DB_USER", "user")
DB_PASSWORD = os.getenv("DB_PASSWORD", "password")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", 5432)
DB_NAME = os.getenv("DB_NAME", "db_name")

connection_string = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

sqlalchemy_config = SQLAlchemyAsyncConfig(
    connection_string=connection_string,
    before_send_handler="autocommit",
    session_config=session_config,
    create_all=True,
)

alchemy = SQLAlchemyPlugin(config=sqlalchemy_config)

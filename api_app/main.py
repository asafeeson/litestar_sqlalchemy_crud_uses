import os
from litestar import Litestar, get
from litestar_granian import GranianPlugin
from dotenv import load_dotenv
from core.config import alchemy
from api.routers import api_router

load_dotenv()

# DEBUG to False in Production!!!
LITESTAR_DEBUG = bool(os.getenv("LITESTAR_DEBUG", False))


@get("/")
async def hello_world() -> dict[str, str]:
    return {"message": "Hello World!"}


async def on_startup(app: Litestar) -> None: ...


async def on_shutdown() -> None:
    # close connections
    ...


app = Litestar(
    plugins=[GranianPlugin(), alchemy],
    on_startup=[on_startup],
    on_shutdown=[on_shutdown],
    debug=LITESTAR_DEBUG,
    route_handlers=[api_router],
)

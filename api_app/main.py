import os
from litestar import Litestar, get
from litestar_granian import GranianPlugin
from dotenv import load_dotenv

load_dotenv()

LITESTAR_DEBUG = bool(os.getenv("LITESTAR_DEBUG", False))

@get("/")
async def hello_world() -> dict[str, str]:
    return {"message": "Hello World!"}


async def on_startup(app: Litestar) -> None:
    ...
    
async def on_shutdown() -> None:
    # close connections
    ...



app = Litestar(
    plugins=[GranianPlugin()],
    on_startup=[on_startup],
    on_shutdown=[on_shutdown],
    debug=LITESTAR_DEBUG,
    route_handlers=[
        hello_world
    ]
)

# DEBUG to False in Production!!!
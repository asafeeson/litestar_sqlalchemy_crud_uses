from litestar import Litestar, get
from litestar_granian import GranianPlugin

@get("/")
async def hello_world() -> dict[str, str]:
    return {"message": "Hello World!"}


app = Litestar(
    plugins=[GranianPlugin()],
    route_handlers=[
        hello_world
    ]
)

from litestar import Router
from controllers import UserController

api_router = Router(
    path="/api/v1",
    route_handlers=[UserController]
)
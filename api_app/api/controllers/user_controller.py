from litestar import Controller, get, post, patch, delete
from domain.schemas.user_schemas import UserDTO, UserCreateDTO, UserResponseDTO, UserUpdateDTO


class UserController(Controller):
    path = "/users"
    tags = "Users"
    
    @post("/")
    async def create_user() -> UserResponseDTO:
        ...
        
    @get("/")
    async def list_users() -> list[UserResponseDTO]:
        ...
        
        
    @get("/{user_id:int}")
    async def get_user(user_id: int) -> UserResponseDTO:
        ...
        
    @patch("/{user_id:int}")
    async def update_user(user_id: int):
        ...
        
        
    @delete("/{user_id:int}")
    async def delete_user(user_id: int):
        ...
    
    
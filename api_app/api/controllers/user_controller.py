from litestar import Controller, get, post, patch, delete
from domain.schemas.user_schemas import (
    UserDTO,
    UserCreateDTO,
    UserResponse,
    UserUpdateDTO,
)
from api_app.services.user_service import UserService
from advanced_alchemy.filters import FilterTypes
from advanced_alchemy.service import OffsetPagination


class UserController(Controller):
    path = "/users"
    tags = ["Users"]

    @post("/")
    async def create_user(
        self, user_service: UserService, data: UserCreateDTO
    ) -> UserResponse:
        obj = await user_service.create(data)
        return user_service.to_schema(data=obj, schema_type=UserResponse)

    @get("/")
    async def list_users(
        self, user_service: UserService, filters: list[FilterTypes]
    ) -> OffsetPagination[UserResponse]:
        results, total = await user_service.list_and_count(*filters)
        return user_service.to_schema(results, total, filters, schema_type=UserResponse)

    @get("/{user_id:int}")
    async def get_user(self, user_id: int, user_service: UserService) -> UserResponse:
        obj = await user_service.get(user_id)
        return user_service.to_schema(obj, schema_type=UserResponse)

    @patch("/{user_id:int}")
    async def update_user(
        self, user_service: UserService, data: UserUpdateDTO, user_id: int
    ) -> UserResponse:
        obj = await user_service.update(data=data, item_id=user_id)
        return user_service.to_schema(obj, schema_type=UserResponse)

    @delete("/{user_id:int}")
    async def delete_user(self, user_service: UserService, user_id: int) -> None: 
        await user_service.delete(item_id=user_id)

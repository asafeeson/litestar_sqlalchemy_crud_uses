from pydantic import BaseModel, Field, ConfigDict

class BaseSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)


class UserDTO(BaseSchema):
    id: int | None = None
    name: str | None = None
    surname: str | None = None
    username: str
    hashed_password: str


class UserCreateDTO(BaseSchema):
    id: int
    name: str
    surname: str
    username: str = Field(..., min_length=3, max_length=50)
    password: str = Field(..., min_length=8)


class UserUpdateDTO(BaseSchema):
    name: str | None = None
    surname: str | None = None
    username: str | None = Field(None, min_length=3, max_length=50)
    password: str | None = Field(None, min_length=8)


class UserResponse(BaseSchema):
    id: int
    name: str
    surname: str
    username: str

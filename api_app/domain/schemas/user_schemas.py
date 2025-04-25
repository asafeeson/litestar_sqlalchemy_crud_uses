from pydantic import BaseModel, Field


class UserDTO(BaseModel):
    id: int | None = None
    name: str | None = None
    surname: str | None = None
    username: str
    hashed_password: str


class UserCreateDTO(BaseModel):
    id: int
    name: str
    surname: str
    username: str = Field(..., min_length=3, max_length=50)
    password: str = Field(..., min_length=8)


class UserUpdateDTO(BaseModel):
    name: str | None = None
    surname: str | None = None
    username: str | None = Field(None, min_length=3, max_length=50)
    password: str | None = Field(None, min_length=8)


class UserResponseDTO(BaseModel):
    id: int
    name: str
    surname: str
    username: str

from typing import Optional
from advanced_alchemy.repository import SQLAlchemyAsyncRepository
from advanced_alchemy.service import SQLAlchemyAsyncRepositoryService
from db.models.users import UserModel


class UserService(SQLAlchemyAsyncRepositoryService[UserModel]):
    
    class Repo(SQLAlchemyAsyncRepository[UserModel]):
        model_type = UserModel
        
    repository_type = Repo
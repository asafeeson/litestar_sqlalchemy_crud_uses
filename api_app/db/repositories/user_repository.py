from advanced_alchemy.repository import SQLAlchemyAsyncRepository
from advanced_alchemy.service import SQLAlchemyAsyncRepositoryService

from db.models.users import UserModel

class UserRepository(SQLAlchemyAsyncRepository[UserModel]):
    model_type = UserModel



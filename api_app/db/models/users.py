from __future__ import annotations
from advanced_alchemy.base import BigIntAuditBase
from sqlalchemy.orm import Mapped, mapped_column


class UserModel(BigIntAuditBase):
    __tablename__ = "user"
    name: Mapped[str]
    surname: Mapped[str]
    username: Mapped[str] = mapped_column(unique=True)
    hashed_password: Mapped[str]
    
    
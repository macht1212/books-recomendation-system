from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from models_orm.base import Base
from models_orm import Authors, Category # Publisher


class Books(Base):
    __tablename__ = 'books'

    id: Mapped[int] = mapped_column(primary_key=True)
    author1: Mapped[str] = mapped_column(ForeignKey('authors.id', ondelete="CASCADE"), nullable=False, default='ND')
    author2: Mapped[str] = mapped_column(ForeignKey('authors.id', ondelete="CASCADE"), default=0)
    author3: Mapped[str] = mapped_column(ForeignKey('authors.id', ondelete="CASCADE"), default=0)
    category: Mapped[int] = mapped_column(ForeignKey('category.id', ondelete="CASCADE"), default=0)
    publisher: Mapped[int] = mapped_column(ForeignKey('publisher.id', ondelete='CASCADE'), default=0)
    title: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(default='No text')
    rating: Mapped[float] = mapped_column(default=0.0)

    def __repr__(self):
        return f'Title: {self.title}, description: {self.description}'
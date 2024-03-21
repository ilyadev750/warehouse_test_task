from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy import ForeignKey
from sqlalchemy import UniqueConstraint, CheckConstraint
from sqlalchemy.orm import mapped_column
from sqlalchemy import String
from sqlalchemy.orm import relationship
from typing import List


class Base(DeclarativeBase):
    pass


class Category(Base):

    __tablename__ = "goods_categories"

    id: Mapped[int] = mapped_column(primary_key=True)
    category: Mapped[str] = mapped_column(String(50))

    __table_args__ = (UniqueConstraint('category', name='category'),)

    main_shelve: Mapped["MainShelve"] = relationship(back_populates="category")
    goods: Mapped[List["Good"]] = relationship(back_populates="category")


class MainShelve(Base):

    __tablename__ = "main_shelves"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    category_id: Mapped[int] = mapped_column(
        ForeignKey("goods_categories.id", onupdate="CASCADE", ondelete="CASCADE")
        )
    
    __table_args__ = (UniqueConstraint('category_id', name='unique_category'),)

    category: Mapped["Category"] = relationship(back_populates="main_shelve")
    minor_shelves: Mapped[List["MinorShelve"]] = relationship(back_populates="main_shelve")


class Good(Base):

    __tablename__ = "goods"

    id: Mapped[int] = mapped_column(primary_key=True)
    model_name: Mapped[str] = mapped_column(String(50))
    category_id: Mapped[int] = mapped_column(
        ForeignKey("goods_categories.id", onupdate="CASCADE", ondelete="CASCADE")
        )
    
    __table_args__ = (UniqueConstraint('model_name', name='unique_model'),)
    
    category: Mapped["Category"] = relationship(back_populates="goods")
    

class MinorShelve(Base):

    __tablename__ = "minor_shelves"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    main_shelve_id: Mapped[int] = mapped_column(
        ForeignKey("main_shelves.id", onupdate="CASCADE", ondelete="CASCADE")
        )
    
    __table_args__ = (
        UniqueConstraint('name', 'main_shelve_id', name='unique_minor_shelve_for_main_shelve'),
        CheckConstraint(name != main_shelve_id.name, name='not_equal_main_shelve')
        )
    
    main_shelve: Mapped["MainShelve"] = relationship(back_populates="minor_shelves")
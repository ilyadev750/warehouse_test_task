from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy import ForeignKey
from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import mapped_column
from sqlalchemy import String, INTEGER, BOOLEAN
from sqlalchemy.orm import relationship
from typing import List


class Base(DeclarativeBase):
    pass


class Category(Base):
    """Модель категорий товаров."""

    __tablename__ = "goods_categories"

    id: Mapped[int] = mapped_column(primary_key=True)
    category: Mapped[str] = mapped_column(String(50))

    __table_args__ = (UniqueConstraint('category', name='category'),)

    goods: Mapped[List["Good"]] = relationship(back_populates="category")


class Shelve(Base):
    """Модель стеллажей."""

    __tablename__ = "shelves"

    id: Mapped[int] = mapped_column(primary_key=True)
    shelve: Mapped[str] = mapped_column(String(50))


class GoodShelve(Base):
    """Модель стеллажей."""

    __tablename__ = "good_shelve"

    id: Mapped[int] = mapped_column(primary_key=True)
    good_id: Mapped[str] = mapped_column(
        ForeignKey(
            "goods.id", onupdate="CASCADE", ondelete="CASCADE"
            )
        )
    shelve_id: Mapped[str] = mapped_column(
        ForeignKey(
            "shelves.id", onupdate="CASCADE", ondelete="CASCADE"
            )
        )
    is_main: Mapped[bool] = mapped_column(BOOLEAN)


class Good(Base):
    """Модель товаров."""

    __tablename__ = "goods"

    id: Mapped[int] = mapped_column(primary_key=True)
    model_name: Mapped[str] = mapped_column(String(50))
    category_id: Mapped[int] = mapped_column(
        ForeignKey(
            "goods_categories.id", onupdate="CASCADE", ondelete="CASCADE"
            )
        )

    __table_args__ = (UniqueConstraint('model_name', name='unique_model'),)

    category: Mapped["Category"] = relationship(back_populates="goods")
    ordered_goods: Mapped[List["OrderedGoods"]] = relationship(
        back_populates="good"
        )


class Order(Base):
    """Модель заказов."""

    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True)
    number: Mapped[int] = mapped_column(INTEGER)

    __table_args__ = (
        UniqueConstraint('number', name='unique_order'),
        )

    ordered_goods: Mapped[List["OrderedGoods"]] = relationship(
        back_populates="order"
        )


class OrderedGoods(Base):
    """Модель заказанных товаров."""

    __tablename__ = "ordered_goods"

    id: Mapped[int] = mapped_column(primary_key=True)
    order_id: Mapped[int] = mapped_column(
        ForeignKey("orders.id", onupdate="CASCADE", ondelete="CASCADE")
        )
    good_id: Mapped[int] = mapped_column(
        ForeignKey("goods.id", onupdate="CASCADE", ondelete="CASCADE")
        )
    quantity: Mapped[int] = mapped_column(INTEGER)

    __table_args__ = (
        UniqueConstraint('order_id', 'good_id', name='unique_order_and_good'),
        )

    good: Mapped["Good"] = relationship(back_populates="ordered_goods")
    order: Mapped["Order"] = relationship(back_populates="ordered_goods")

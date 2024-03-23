from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy import ForeignKey
from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import mapped_column
from sqlalchemy import String, INTEGER
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

    main_shelve: Mapped["MainShelve"] = relationship(back_populates="category")
    goods: Mapped[List["Good"]] = relationship(back_populates="category")


class MainShelve(Base):
    """Модель главных стеллажей."""

    __tablename__ = "main_shelves"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    category_id: Mapped[int] = mapped_column(
        ForeignKey(
            "goods_categories.id", onupdate="CASCADE", ondelete="CASCADE"
            )
        )

    __table_args__ = (UniqueConstraint('category_id', name='unique_category'),)

    category: Mapped["Category"] = relationship(back_populates="main_shelve")


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
    minor_shelves: Mapped[List["MinorShelve"]] = relationship(
        back_populates="good"
        )
    ordered_goods: Mapped[List["OrderedGoods"]] = relationship(
        back_populates="good"
        )


class MinorShelve(Base):
    """Модель второстепенных стеллажей."""

    __tablename__ = "minor_shelves"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    good_id: Mapped[int] = mapped_column(
        ForeignKey("goods.id", onupdate="CASCADE", ondelete="CASCADE")
        )

    __table_args__ = (
        UniqueConstraint(
            'name', 'good_id', name='unique_minor_shelve_for_good'),
        )

    good: Mapped["Good"] = relationship(back_populates="minor_shelves")


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

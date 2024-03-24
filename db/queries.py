from sqlalchemy.orm import Session
from .engine import engine
from .models import (Category, Shelve, Good,
                     GoodShelve, Order, OrderedGoods)


session = Session(engine)


class Query:
    """Класс, отвечающий за проведение запросов
    к базе данных"""

    def get_all_orders(self, orders_list):
        """Запрос на получение информации по заказанным товарам
        и местах их хранения."""
        query = session.query(OrderedGoods, Order, Good, Category, MainShelve)
        query = query.join(Order, Order.id == OrderedGoods.order_id)
        query = query.join(Good, Good.id == OrderedGoods.good_id)
        query = query.join(Category, Good.category_id == Category.id)
        query = query.join(MainShelve, Category.id == MainShelve.category_id)
        query = query.filter(Order.number.in_(orders_list))
        query = query.order_by(Category.category)
        records = query.all()
        return records

    def get_minor_shelves_for_goods(self):
        """Запрос на получение информации по дополнительным
        стеллажам для каждого товара."""
        query = session.query(MinorShelve, Good, Category)
        query = query.join(Good, MinorShelve.good_id == Good.id)
        query = query.join(Category, Good.category_id == Category.id)
        query = query.order_by(Good.id)
        records = query.all()
        return records 

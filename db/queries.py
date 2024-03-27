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
        subquery = self.get_main_or_minor_shelves_for_goods(condition=True).subquery()
        query = session.query(OrderedGoods, Order, Good, Category, subquery.c.shelve)
        query = query.join(Order, Order.id == OrderedGoods.order_id)
        query = query.join(Good, Good.id == OrderedGoods.good_id)
        query = query.join(Category, Good.category_id == Category.id)
        query = query.outerjoin(subquery)
        query = query.filter(Order.number.in_(orders_list))
        query = query.order_by(subquery.c.shelve)
        records = query.all()
        return records

    def get_main_or_minor_shelves_for_goods(self, condition):
        """Запрос на получение информации по основным или дополнительным
        стеллажам для каждого товара."""
        query = session.query(GoodShelve, Good, Category, Shelve)
        query = query.join(Good, Good.id == GoodShelve.good_id)
        query = query.join(Category, Good.category_id == Category.id)
        query = query.join(Shelve, GoodShelve.shelve_id == Shelve.id)
        query = query.filter(GoodShelve.is_main == condition)
        return query

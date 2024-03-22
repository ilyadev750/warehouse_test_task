from sqlalchemy.orm import Session
from .engine import engine
from .models import Category, MainShelve, Good, MinorShelve, Order, OrderedGoods


session = Session(engine)


class Query:

    def get_all_orders(self, orders_list):
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
        query = session.query(MinorShelve, Good, Category)
        query = query.join(Good, MinorShelve.good_id == Good.id)
        query = query.join(Category, Good.category_id == Category.id)
        query = query.order_by(Good.id)
        records = query.all()
        return records



    # for order_good, order, good, category, shelve in records:
    #     print(order_good.quantity, order.number, (good.model_name, f'id={good.id}'), category.category, shelve.name)





# query = session.query(MinorShelve, Good)
# query = query.outerjoin(Good, MinorShelve.good_id == Good.id)
# query = query.filter(Good.model_name.in_(['Lenovo', 'Rolex']))
# records = query.all()

# for shelve, good in records:
#     print(shelve.name, good.model_name)

# query = (select(OrderedGoods, Order, Good, Category)
#          .join(OrderedGoods.order)
#          .join(OrderedGoods.good)
#          .join(Good.category))
# query_2 = session.query(MinorShelve, Good)
# query_2 = query_2.join(Good, Good.id == MinorShelve.good_id)
# records = query_2.all()

# for shelve, good in records:
#     print(shelve.name, good.id)
from sqlalchemy.orm import Session
from engine import engine
from sqlalchemy import select
from models import Category, MainShelve, Good, MinorShelve, Order, OrderedGoods


session = Session(engine)
# query = (select(OrderedGoods, Order, Good, Category)
#          .join(OrderedGoods.order)
#          .join(OrderedGoods.good)
#          .join(Good.category))

query = session.query(OrderedGoods, Order, Good, Category)
query = query.join(Order, Order.id == OrderedGoods.order_id)
query = query.join(Good, Good.id == OrderedGoods.good_id)
query = query.join(Category, Good.category_id == Category.id)

records = query.all()

for order_good, order, good, category in records:
    print(order_good.quantity, order.number, good.model_name, category.category)
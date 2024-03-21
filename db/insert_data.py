from sqlalchemy.orm import Session
from models import Category, MainShelve, Good, MinorShelve, Order, OrderedGoods
from engine import engine


# with Session(engine) as session:
    # ordered_good_1 = OrderedGoods(order_id=1, good_id=1, quantity=2)
    # ordered_good_2 = OrderedGoods(order_id=1, good_id=3, quantity=1)
    # ordered_good_3 = OrderedGoods(order_id=1, good_id=6, quantity=2)
    # ordered_good_4 = OrderedGoods(order_id=2, good_id=1, quantity=1)
    # ordered_good_5 = OrderedGoods(order_id=2, good_id=8, quantity=5)
    # ordered_good_6 = OrderedGoods(order_id=3, good_id=5, quantity=2)
    # ordered_good_7 = OrderedGoods(order_id=3, good_id=4, quantity=2)

    # session.add_all([ordered_good_1])
    # session.commit()
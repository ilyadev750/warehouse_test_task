# from sqlalchemy.orm import Session
# from models import (Category, Shelve, Good,
#                     GoodShelve, Order, OrderedGoods)
# from engine import engine

"""Модуль для добавления информации в базу данных"""
# with Session(engine) as session:
#     good_shelve_1 = GoodShelve(good_id=1, shelve_id=1, is_main=True)
#     good_shelve_2 = GoodShelve(good_id=2, shelve_id=1, is_main=True)
#     good_shelve_4 = GoodShelve(good_id=3, shelve_id=2, is_main=True)
#     good_shelve_5 = GoodShelve(good_id=3, shelve_id=4, is_main=False)
#     good_shelve_6 = GoodShelve(good_id=3, shelve_id=5, is_main=False)
#     good_shelve_7 = GoodShelve(good_id=4, shelve_id=3, is_main=True)
#     good_shelve_8 = GoodShelve(good_id=5, shelve_id=3, is_main=True)
#     good_shelve_9 = GoodShelve(good_id=5, shelve_id=6, is_main=False)
#     good_shelve_10 = GoodShelve(good_id=6, shelve_id=3, is_main=True)

#     session.add_all([good_shelve_1, good_shelve_2, good_shelve_4, good_shelve_5,
#                      good_shelve_6, good_shelve_7, good_shelve_8, good_shelve_9,
#                      good_shelve_10])
#     session.commit()
import unittest
from sqlalchemy.orm import Session
from db.engine import engine
from db.models import Category, MainShelve, Good, MinorShelve, Order, OrderedGoods


session = Session(engine)


class TestQuery(unittest.TestCase):

    def setUp(self):
        self.minor_shelves_1_good_category = 'Б, 5, Lenovo, Ноутбук'
        self.minor_shelves_2_good_category = 'V, 3, Sennheiser, Микрофон'
        self.order_category_mainshelve = 'Заказ 10, Ноутбук HP, Главный стеллаж A' 
        
    def get_records_1(self, model_name):
        query = session.query(MinorShelve, Good, Category)
        query = query.join(Good, MinorShelve.good_id == Good.id)
        query = query.join(Category, Good.category_id == Category.id)
        query = query.filter(Good.model_name == model_name)
        records = query.all()
        return records
    
    def get_records_2(self, order_number, model_name):
        query = session.query(OrderedGoods, Order, Good, Category, MainShelve)
        query = query.join(Order, Order.id == OrderedGoods.order_id)
        query = query.join(Good, Good.id == OrderedGoods.good_id)
        query = query.join(Category, Good.category_id == Category.id)
        query = query.join(MainShelve, Category.id == MainShelve.category_id)
        query = query.filter(Order.number.in_(order_number))
        query = query.filter(Good.model_name.in_(model_name))
        records = query.all()
        return records
    
    def get_result_1(self, records):
        result = ''
        for record in records:
            minor_shelve = record[0]
            result += f'{minor_shelve.name}, '
        good = record[1]
        category = record[2]
        result += f'{good.model_name}, '
        result += f'{category.category}'
        return result
    
    def test_get_minor_shelves_1_good_category(self):
        records = self.get_records_1(model_name='Lenovo')
        result = self.get_result_1(records=records)
        self.assertEqual(self.minor_shelves_1_good_category, result)

    def test_get_minor_shelves_2_good_category(self):
        records = self.get_records_1(model_name='Sennheiser')
        result = self.get_result_1(records=records)
        self.assertEqual(self.minor_shelves_2_good_category, result)

    def test_get_order_category_mainshelve(self):
        result = ''
        record = self.get_records_2(order_number=[10], model_name=['HP'])
        order = record[0][1]
        category = record[0][3]
        good = record[0][2]
        main_shelve = record[0][4]
        result += 'Заказ '
        result += f'{order.number}, '
        result += f'{category.category} {good.model_name}, '
        result += f'Главный стеллаж {main_shelve.name}'
        self.assertEqual(self.order_category_mainshelve, result)
        

if __name__ == "__main__":
    unittest.main()
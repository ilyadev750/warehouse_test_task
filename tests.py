import unittest
from sqlalchemy.orm import Session
from db.queries import Query
from db.engine import engine
from db.models import Good


session = Session(engine)


class TestQuery(unittest.TestCase, Query):

    def setUp(self):
        """Установка аттрибутов для проверки"""
        self.minor_shelves_1_good_category = '3, В, Xiaomi, Телефон'
        self.order_category_mainshelve = 'Заказ 11, Телевизор Toshiba, id=2, Главный стеллаж А'

    def get_records_1(self, model_name):
        """Запрос к базе данных для получения информации
        по второстепенным стеллажам для товара"""
        query = self.get_main_or_minor_shelves_for_goods(condition=False)
        query = query.filter(Good.model_name == model_name)
        records = query.all()
        return records

    def get_records_2(self, order_number):
        """Запрос к базе данных для получения полной
        информации по заказу"""
        records = self.get_all_orders(orders_list=order_number)
        return records

    def get_result_1(self, records):
        """Обработка запроса из базы данных по
        второстепенным стеллажам, формирование
        результата"""
        result = ''
        for record in records:
            minor_shelve = record[3]
            result += f'{minor_shelve.shelve}, '
        good = record[1]
        category = record[2]
        result += f'{good.model_name}, '
        result += f'{category.category}'
        return result

    def get_result_2(self, records):
        """Обработка запроса из базы данных по
        заказанному товару, формирование
        результата"""
        result = ''
        order = records[0][1]
        category = records[0][3]
        good = records[0][2]
        main_shelve = records[0][4]
        result += 'Заказ '
        result += f'{order.number}, '
        result += f'{category.category} {good.model_name}, '
        result += f'id={good.id}, '
        result += f'Главный стеллаж {main_shelve}'
        return result

    def test_get_minor_shelves_1_good_category(self):
        """Тест 1"""
        records = self.get_records_1(model_name='Xiaomi')
        result = self.get_result_1(records=records)
        self.assertEqual(self.minor_shelves_1_good_category, result)

    def test_get_order_category_mainshelve(self):
        """Тест 2"""
        records = self.get_records_2(order_number=[11])
        result = self.get_result_2(records=records)
        self.assertEqual(self.order_category_mainshelve, result)


if __name__ == "__main__":
    unittest.main()

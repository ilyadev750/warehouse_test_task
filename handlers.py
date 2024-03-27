from db.queries import Query


class Handler(Query):
    """Класс, отвечающий за обработку и вывод
    в консоль полученной информации из базы
    данных """

    def __init__(self, orders_list):
        self.current_shelve = None
        self.orders_list = orders_list
        self.minor_shelves = {}

    def print_all_orders_with_shelves(self):
        """Обработка и вывод информации по
        номерам заказов для сборщика"""
        records = self.get_all_orders(self.orders_list)
        if not records:
            print('По вашему запросу данных не найдено!')
            return

        print('\n=+=+=+=+')
        print(
            f"Страница сборки заказов {', '.join([str(x) for x in self.orders_list])}\n"
            )

        for ordered_good, order, good, category, main_shelve in records:
            if main_shelve != self.current_shelve:
                self.current_shelve = main_shelve
                print(f'===Стеллаж {self.current_shelve}')
            print(f'{category.category} {good.model_name} (id={good.id})')
            print(f'заказ {order.number}, {ordered_good.quantity} шт')

            minor_shelves = self.minor_shelves.get(good.id)
            if minor_shelves:
                print(f'Доп.стеллажи: {minor_shelves}\n')
            else:
                print('')

    def collect_info_about_minor_shelves(self):
        """Обработка информации по второстепенным стеллажам"""
        query = self.get_main_or_minor_shelves_for_goods(condition=False)
        records = query.all()
        for record in records:
            minor_shelve = record[3]
            good = record[1]
            good_minor_shelves = self.minor_shelves.get(good.id)
            if not good_minor_shelves:
                self.minor_shelves[good.id] = f'{minor_shelve.shelve}'
            else:
                self.minor_shelves[good.id] += f', {minor_shelve.shelve}'

    def run(self):
        """Начало работы по поиску и обработке информации"""
        self.collect_info_about_minor_shelves()
        self.print_all_orders_with_shelves()

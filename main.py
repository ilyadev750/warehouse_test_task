import sys
from handlers import Handler


if __name__ == '__main__':
    """Запуск программы через консоль с номерами
    заказов в виде аргументов"""
    args = sys.argv[1:]
    try: 
        orders_list = [int(x.replace(",", "")) for x in args]
    except ValueError:
        print(f'Заказ должен содержать только числа, но не строки!')
        orders_list = []
    handler = Handler(orders_list=orders_list)
    handler.run()
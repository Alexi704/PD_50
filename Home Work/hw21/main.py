
from classes import Request, Shop, Store

if __name__ == '__main__':
    shop = Shop()
    store = Store()

    store.add('собачки', 5)
    store.add('яблоко', 2)
    store.add('машинки', 8)

    shop.add('печеньки', 1)
    shop.add('яблоко', 1)
    shop.add('машинки', 1)
    shop.add('коробки', 1)
    shop.add('собачки', 2)

    print('На складе есть:')
    print(store.get_items())

    print('В магазине есть:')
    print(shop.get_items())

    user_answer = input('Введите строчку такого типа: "Доставить 2 собачки со склад в магазин": \n')
    data_request = Request(user_answer)

    print(data_request)

    result_store = store.remove(data_request.product, data_request.amount)

    if result_store:
        print(f'Курьер забрал {data_request.amount} {data_request.product} со склада')
        print(f'Курьер везет {data_request.amount} {data_request.product} со склада в магазин')
        result_shop = shop.add(data_request.product, data_request.amount)

        if not result_shop:
            store.add(data_request.product, data_request.amount)
        else:
            print(f'Курьер доставил {data_request.amount} {data_request.product} в магазин')

    print('На складе есть:')
    print(store.get_items())

    print('В магазине есть:')
    print(shop.get_items())



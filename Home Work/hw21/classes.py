from abc import abstractmethod

class Storage:
    @abstractmethod
    def add(self, name, count):
        pass

    @abstractmethod
    def remove(self, name, count):
        pass

    @abstractmethod
    def get_free_space(self):
        pass

    @abstractmethod
    def get_items(self):
        pass

    @abstractmethod
    def get_unique_items_count(self):
        pass


class Store(Storage):
    def __init__(self):
        self.items = {}
        self.capacity = 100

    def add(self, name, count):
        if self.get_free_space() > 0:
            if self.get_free_space() >= count:
                print(f'Товар {name} добавлен')
                if name in self.items.keys():
                    self.items[name] = self.items[name] + count
                else:
                    self.items[name] = count
                return True
            else:
                print(f'Не хватает места для хранения, нужно уменьшить количество. Максимум {self.get_free_space()} ')
        else:
            print(f'Нет свободного места')
        return False

    def remove(self, name, count):
        if name in self.items.keys():
            if self.items[name] >= count:
                print('Есть нужное количество.')
                self.items[name] = self.items[name] - count
                return True
            else:
                # print(f'Нет такого количества товара. Максимум {self.get_free_space()} ')
                print(f'Нет такого количества товара. Максимум {self.items[name]} ')

        else:
            print('Такого товара нет')
            return False
        return False

    def get_free_space(self):
        return self.capacity - sum(self.items.values())

    def get_items(self):
        return self.items

    def get_unique_items_count(self):
        return len(self.items.keys())


class Shop(Store):
    def __init__(self):
        self.items = {}
        self.capacity = 20
        self.limit = 5

    def add(self, name, count):
        if self.get_unique_items_count() <= self.limit:
            super().add(name, count)
            return True
        else:
            print(f'Не хватает места для хранения, уникальных товаров не может быть больше {self.limit}')
            return False


class Request:
    def __init__(self, str_input):
        data = str_input.split(' ')
        # Доставить 3 печеньки из склад в магазин
        self.from_ = data[4]
        self.to = data[6]
        self.amount = int(data[1])
        self.product = data[2]

    def __repr__(self):
        return f'Доставить {self.amount} {self.product} печеньки со {self.from_} в {self.to}'

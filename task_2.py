bag = {}
products = {}


class Product():
    def __init__(self, name, price):
        self.name = name
        self.price = price
        products[self.name] = self.price


class Book(Product):
    pass

class Film(Product):
    pass

class Shop():
    def __init__(self):
        self.bag = bag
        self.products = products
        self.final_price = 0

    def get_info(self):
        "Вывод товаров"

        for section, (prod, price) in enumerate(products.items(), start=1):   

            if section <= 5:
                print(f'{section}. Книга - {prod} - {price} -  рублей')

            elif section >= 6:     
                print(f'{section}. Фильм - {prod} - {price} -  рублей')
        print('0. Закончить покупку')

    def by_product(self, selected_index):
        "Покупка товара"
        for section, (prod, price) in list(enumerate(products.items(), start=1)):
            if section == selected_index:
                self.bag.update({prod: price})
                del products[prod]
                self.get_info()


                print(f"В корзину добавлен товар товар: {prod}")

    
    def calculating_product(self):
        "Подсчёт суммы товаров из корзины пользователя"

        print("Ваша корзина:")
        for prod, price in self.bag.items():
            
            self.final_price += price
            print(f"{prod} - {price}")
        print(f"Итог: {self.final_price} руб.")
                



book_1 = Book('Староста-горничная (Манга)', 400)
book_2 = Book('Токийский гуль (Манга)', 710)
book_3 = Book('Атака титанов (Манга)', 534)
book_4 = Book('Моя геройская академия (Манга)', 670)
book_5 = Book("Boku no pico (Хентай Манга)", 1000)

film_1 = Film("Веном 2", 420)
film_2 = Film("Человек паук, нет пути домой", 400)
film_3 = Film("Анчартед: На картах не значится", 360)
film_4 = Film("Игра теней", 290)
film_5 = Film("Бэтмен", 470)


shop = Shop()

while True:
    shop.get_info()
    loop = True
    while loop:
        try:
            selected_index = int(input('Какой товар хотите купить ?\n '))
        except ValueError:
            print('Введите число !')
        else:
            loop = False
    if selected_index == 0:
        shop.calculating_product()
        break
    shop.by_product(selected_index)


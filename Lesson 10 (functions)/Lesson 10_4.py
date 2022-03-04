# ЗАДАЧА
# Интернет магазин осуществляет экспресс доставку для своих товаров по цене 100
# рублей за первый товар и 50 рублей за каждый последующий товар.

# Напишите функцию, которая принимает в качестве аргумента количество товаров
# в заказе и возвращает стоимость доставки.

# РЕШЕНИЕ

def delivery_cost(count):
    first_item_delivery = 100
    item_delivery = 50
    return first_item_delivery + item_delivery * (count - 1)

count = int(input('Введите количество товаров '))
print(delivery_cost(count))
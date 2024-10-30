#!/usr/bin/env python3
# -*- coding: utf-8 -*-

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

lamps_cost = store[goods['Лампа']][0]['quantity'] * store[goods['Лампа']][0]['price']
lamp_code = goods['Лампа']
lamps_item = store[lamp_code][0]
lamps_quantity = lamps_item['quantity']
lamps_price = lamps_item['price']
lamps_cost = lamps_quantity * lamps_price
print('Лампа -', lamps_quantity, 'шт, стоимость', lamps_cost, 'руб')


tables_quantity_1 = store[goods['Стол']][0]['quantity']
tables_quantity_2 = store[goods['Стол']][1]['quantity']
tables_quantity = tables_quantity_1 + tables_quantity_2
tables_price_1 = store[goods['Стол']][0]['price']
tables_price_2 = store[goods['Стол']][1]['price']
tables_cost = (tables_quantity_1 * tables_price_1) + (tables_quantity_2 * tables_price_2)
print('Стол -', tables_quantity, 'шт., стоимость', tables_cost, 'руб.')


sofas_quantity_1 = store[goods['Диван']][0]['quantity']
sofas_quantity_2 = store[goods['Диван']][1]['quantity']
sofas_quantity = sofas_quantity_1 + sofas_quantity_2
sofas_price_1 = store[goods['Диван']][0]['price']
sofas_price_2 = store[goods['Диван']][1]['price']
sofas_cost = (sofas_quantity_1 * sofas_price_1) + (sofas_quantity_2 * sofas_price_2)
print('Диван -', sofas_quantity, 'шт., стоимость', sofas_cost, 'руб.')


chairs_quantity_1 = store[goods['Стул']][0]['quantity']
chairs_quantity_2 = store[goods['Стул']][1]['quantity']
chairs_quantity_3 = store[goods['Стул']][2]['quantity']
chairs_quantity = chairs_quantity_1 + chairs_quantity_2 + chairs_quantity_3
chairs_price_1 = store[goods['Стул']][0]['price']
chairs_price_2 = store[goods['Стул']][1]['price']
chairs_price_3 = store[goods['Стул']][2]['price']
chairs_cost = (chairs_quantity_1 * chairs_price_1) + (chairs_quantity_2 * chairs_price_2) + (chairs_quantity_3 * chairs_price_3)
print('Стул -', chairs_quantity, 'шт., стоимость', chairs_cost, 'руб.')
inventory = {
    "Яблука": 10,
    "Банани": 15
}
def update_inventory(product, amount):
    if product in inventory:
        inventory[product] += amount
    else:
        inventory[product] = amount
    if inventory[product] <= 0:
        del inventory[product]
print("Початковий склад:", inventory)

update_inventory("Яблука", 5)
update_inventory("Груші", 10)
update_inventory("Банани", -15)
print("Оновлений склад:", inventory)

# Додаткове завдання
products = [
    {"продукт": "Гантелі", "кількість": 4},
    {"продукт": "Футбольний м'яч", "кількість": 10},
    {"продукт": "Килимок для йоги", "кількість": 5},
    {"продукт": "Велотренажер", "кількість": 1}
]
low_stock = []
for item in products:
    if item["кількість"] < 5:
        low_stock.append(item["продукт"])
print("Продукти, яких менше ніж 5 на складі:", low_stock)
# Lab Exercise 03
print('Lab Exercise 03 \n')

# Setup
food_items = [
    ['dumplings', 'Appetizer', '6.99'],
    ['spring rolls', 'Appetizer', '5.99'],
    ['niangao', 'Dessert', '7.99'],
    ['whole fish', 'Main', '32.99'],
    ['whole chicken', 'Main', '25.99'],
    ['tangyuan', 'Dessert', '11.99'],
    ['longevity noodles', 'Main', '19.99'],
    ['fa gao', 'Dessert', '11.99']
    ]

# Problem 01 (3 points)

for i in range(len(food_items)):
    food_items[i][2] = float(food_items[i][-1])

print(food_items)


# Problem 02 (4 points)

desserts = []
for item in food_items:
    if item[1].lower() == 'dessert':
        desserts.append(item)

print(desserts)


# Problem 03 (4 points)

expensive_mains = []
for item in food_items:
    if item[1].lower() == 'main' and float(item[2]) > 20:
        expensive_mains.append(item)

print(expensive_mains)


# Problem 04 (4 points)

appetizer_count = 0
main_count = 0
dessert_count = 0
for item in food_items:
    if item[1].lower() == 'appetizer':
        appetizer_count += 1
    elif item[1].lower() == 'main':
        main_count += 1
    else:
        dessert_count += 1

print(appetizer_count)
print(main_count)
print(dessert_count)

# Problem 05 (5 points)

order = []
price_total = 0
i = 0

while price_total < 50:
    order.append(food_items[i])
    price_total += float(food_items[i][2])
    i +=1

print(order)
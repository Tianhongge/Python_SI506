# SI 506: Lab Exercise 03

## This week's Lab Exercise

This week's lab exercise includes five (5) problems that focus on loops and conditional statements.

## Background
The Chinese New Year starts on February 1, 2022. Food is a large part of the celebration activities. For this week's lab assignment you will be working with a list of lists that contain food items that are typical of Chinese New Year celebrations. The list below is named `food_items` and outlines what type of dish each item is and how much a serving costs at a local restaurant.

```python
food_items =[
            ['dumplings', 'appetizer', '6.99'],
            ['spring rolls', 'appetizer', '5.99'],
            ['niangao', 'dessert', '7.99'],
            ['whole fish', 'main', '32.99'],
            ['whole chicken', 'main', '25.99'],
            ['tangyuan', 'dessert', '11.99'],
            ['longevity noodles', 'main', '19.99'],
            ['fa gao', 'dessert', '11.99']]
```

## 1.0 Problem 01 (3 points)

Loop over the `food_items` list and convert the price from type `string` to type `float`. Take the converted number and assign it back to the original position in `food_items`.

:bulb: Convert each price encountered to a float and access the list element using list indexing to update the price.

## 2.0 Problem 02 (4 points)

Implement an `if` statement inside a `for` loop that identifies each dessert item in `food_items`.
Loop over the `food_items` list; if the food is a dessert, append the food item, which is a list, to
the new list named `desserts`.

:bulb: Python is a case-sensitive programming language. Be careful about the uppercase letters in the list.
You might need to use a built-in str method to convert the uppercase letters to lowercase when performing string matching.

## 3.0 Problem 03 (4 points)

Implement a compound `if` statement inside a `for` loop to check for any main dish items that cost more than $20.
Loop over the `food_items` list; if the item is *a main dish and costs more than $20*, append it to a list called `expensive_mains`.

:bulb: In this question, you might not need to convert the uppercase letters to lowercase. But it is a good practice
to make all letters the same case when performing a _case-insensitive_ string comparison.

## 4.0 Problem 04 (4 points)

Implement an `if-elif-else` statement inside a `for` loop and count the food items based on their category.
Loop over the `food_items` list and if the category is 'appetizer', increment a variable called `appetizer_count` by one. If the category is 'main', increment a variable called `main_count` by one. Otherwise, increment a variable called `dessert_count` by one.

:bulb: Recall that you can utilize the built-in function print() to check on the values being counted in the appetizer, main, and dessert counter variables. When satisfied with your conditional statements you can comment out print() or remove the expression from your code.

## 5.0 Problem 05 (5 points)

Implement a `while` loop that continues to add items to your order until the total price of your order is greater than or equal to $50.
While your price total is less than 50, add the price to the price total.

::bulb:: If you want to make sure this works for several scenarios, try rearranging the order of the food lists in `food_items`.
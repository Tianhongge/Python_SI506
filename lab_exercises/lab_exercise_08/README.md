# SI 506: Lab Exercise 08

## This week's Lab Exercise

This week's lab exercise includes five (5) problems that focus on list comprehensions.

## Background

For this lab, you are provided with a csv file that includes information about the the previous winners of the NASCAR championship cup (1949-2021).
After the file is read in, the list of lists will contain the year of the championship, the driver who won, the number of the driver's car, the manufacturer of the driver's car, and the number of wins.
You will use list comprehension to complete the problems.

## 1.0 Problem 01 (2 points)

1. Write a function called `read_csv` that defines four parameters:

    * `filepath` (str): A filepath of a csv file to be read from.

    * `encoding` (str): Name of encoding used to decode file. Has a *default value* of `utf-8-sig`.

    * `newline` (str): Replacement value for newline; *default value* is `''`.

    * `delimiter` (str): Delimiter that separates row values; *default value* is `','`.

    This function should load a csv file and return its contents in a list of lists, where each list is one row from the csv file. You *must* employ a list comprehension when accessing each row in the `reader` object.

2. Inside the `main()` function, call `read_csv` and set the file path to `nascar_champions.csv`. Then utilize list slicing to ensure the return value does not contain the header list element. Assign the return value to a variable called `nascar_champs`.

## 2.0 Problem 02 (4 points)

1. Implement a function called `get_driver_names()` that accepts one parameter: `champs`, a list of lists containing information about NASCAR champions from 1949-2021. This function *must* utilize list comprehension to loop over `nascar_champs` and append the name of each driver to a list. Return the resulting list. Your loop variable *must* be called `champ`.

2. Inside of the `main()` function, call `get_driver_names()` passing to it the list argument `nascar_champs` and assign the return value to a variable called `nascar_winners`.

:bulb: In order to pass the autograder, you *must* use list comprehension and use the variable names above exactly as written.

## 3.0 Problem 03 (4 points)

1. Implement a function called `get_multiple_nascar_winners()` that accepts one parameter: `champs`, a list of lists containing information about NASCAR champions from 1949-2021. Loop over `champs` and append the name of each driver who has at least 2 wins. Utilize a conditional statement and list comprehension. Return the cleaned list. Your loop variable *must* be called `champ`.

2. Inside of the `main()` function, call `get_multiple_nascar_winners()` passing to it the list `nascar_champs` as the argument. Assign the return value to a variable called `multiple_winners`.

:bulb: All of the values read in from the csv are still in string format, so you may have to cast an element to a different type for proper comparison.

## 4.0 Problem 04 (5 points)

1. Implement a function called `clean_lists()` that accepts two parameters: `multiple_winners`, a list containing the names of all drivers who have at least 2 wins and `nascar_winners`, a list containing the names of all drivers who won NASCAR championships from 1949-2021. Utilize 2 separate list comprehensions to obtain the unique values of each list. Your loop variable *must* be called `winner` in both list comprehensions.

Append the unique values of multiple_winners to a variable called `multiple_winners_copy` and append the unique values of `nascar_winners` to a variable called `nascar_winners_copy`. Return a tuple consisting of `multiple_winners_copy` and `nascar_winners_copy` in that order.

2. Inside of the `main()` function, call `clean_lists()` passing to it the list arguments `multiple_winners` and `nascar_winners`. Utilize tuple unpacking to unpack the return value into two variables called `clean_mult_winners` and `clean_nascar_winners`.

:bulb: Note that you must call the list's `append` method within the list comprehension in order to properly execute this function. Use the proper `if` statement to check whether a driver's name is already in the copied list or not.

## 5.0 Problem 05 (5 points)

1. Implement a function called `cat_car_manufacturers()` that accepts one parameter: `champs`, a list of lists containing information about NASCAR champions from 1949-2021. Utilize the accumulator pattern and list comprehension to categorize car manufacturers of the winning drivers as car manufacturers from before 1985 and car manufacturers from 1985-2021. Declare two empty lists: `oldest_cars` and `youngest_cars` and utilize an `if-else` statement within a list comprehension in order to append the car manufacturers of winning vehicles from before 1985 to `oldest_cars` and append car manufacturers of winning vehicles from 1985 and after to `youngest_cars`. Return a tuple consisting of `youngest_cars` and `oldest_cars` in that order.

2. Inside of the `main()` function, call `cat_car_manufacturers()` passing to it the list argument `nascar_champs`. Utilize tuple unpacking to unpack the return value into two variables called `youngest_manf` and `oldest_manf`.

:bulb: You *must* utilize only one list comprehension. Your loop variable must be called `champ`. Your list comprehension must have only an `if-else` statement within it. Your `if` statement must check if the year is less than 1985 (and must include casting of the list element within this check). Your `else` statement must append to `youngest_cars` if it does not meet the requirements to be appended to `oldest_cars`.
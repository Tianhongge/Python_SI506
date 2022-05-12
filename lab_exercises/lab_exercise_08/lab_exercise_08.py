import csv

# LAB EXERCISE 06
print('Lab Exercise 08 \n')

# Problem 01 (2 points)
def read_csv(filepath, encoding='utf-8-sig', newline='', delimiter=','):
    """
    Reads a CSV file, parsing row values per the provided delimiter. Returns a list of lists,
    wherein each nested list represents a single row from the input file.

    Parameters:
        filepath (str): The location of the file to read
        encoding (str): name of encoding used to decode the file
        newline (str): specifies replacement value for newline '\n'
                       or '\r\n' (Windows) character sequences
        delimiter (str): delimiter that separates the row values

    Returns:
        list: nested "row" lists
    """
    with open(filepath, 'r', encoding=encoding, newline=newline) as file_obj:
        reader = csv.reader(file_obj, delimiter=delimiter)

        # data = []
        # for row in reader:
        #     data.append(row)

        data = [row for row in reader]
        return data

# Problem 02 (4 points)
def get_driver_names(champs):
    """
    This function returns a list containing all the names of drivers who won NASCAR championships from 1949-2021.

    Parameters:
        champs (list): A list of lists containing information about NASCAR champions from 1949-2021.

    Returns:
        A list containing all the names of drivers who won NASCAR championships from 1949-2021.
    """
    return [champ[1] for champ in champs]

# Problem 03 (4 points)
def get_multiple_nascar_winners(champs):
    """
    This function takes a list containing all the names of drivers who won NASCAR championships from 1949-2021 and returns a list of all the names of drivers who have at least 2 wins.

    Parameters:
        champs (list): A list of lists containing information about NASCAR champions from 1949-2021.
    Returns:
        A list containing the names of all drivers who have at least 2 wins.
    """
    return [champ[1] for champ in champs if int(champ[4]) >= 2]

# Problem 04 (5 points)
def clean_lists(multiple_winners, nascar_winners):
    """
    This function returns two cleaned lists that contain only unique values.

    Parameters:
        multiple_winners (list): A list containing the names of all drivers who have at least 2 wins.
        nascar_winners (list): A list containing the names of all drivers who won NASCAR championships from 1949-2021.
    Returns:
        a tuple containing (in this order):
            a list of unique driver names who have at least 2 wins.
            a list of unique driver names who won a NASCAR championship from 1949-2021.
    """
    multiple_winners_copy = []
    nascar_winners_copy = []
    [multiple_winners_copy.append(winner) for winner in multiple_winners if winner not in multiple_winners_copy]
    [nascar_winners_copy.append(winner) for winner in nascar_winners if winner not in nascar_winners_copy]
    return (multiple_winners_copy, nascar_winners_copy)

# Problem 05 (5 points)
def cat_car_manufacturers(champs):
    """
    This function returns two lists of car manufacturers that made the car of the winning drivers.
    Parameters:
        champs (list): A list of lists containing information about NASCAR champions from 1949-2021.
    Returns:
        a tuple containing (in this order):
            a list of non-unique car manufacturers that made the car of the winning driver in the year of 1985 or later.
            a list of non-unique car manufacturers that made the car of the winning driver before 1985.
    """
    oldest_cars = []
    youngest_cars = []

    [oldest_cars.append(champ[-2])
    if int(champ[0]) < 1985
    else youngest_cars.append(champ[-2])
    for champ in champs
    ]
    return (youngest_cars, oldest_cars)
# Call functions below
def main():
    """
    This function serves as the point of entry and controls the flow of this Python script

    Parameters:
        None

    Returns:
        None
    """

    # Problem 01
    print("Problem 01:\n")
    nascar_champs = read_csv('nascar_champions.csv')[1:]
    print(nascar_champs)

    # Problem 02
    print("Problem 02:\n")
    nascar_winners = get_driver_names(nascar_champs)
    print(nascar_winners)

    # Problem 03
    print("Problem 03:\n")
    multiple_winners = get_multiple_nascar_winners(nascar_champs)
    print(multiple_winners)

    # Problem 04
    print("Problem 04:\n")
    clean_multiple_winners, clean_nascar_winners = clean_lists(multiple_winners, nascar_winners)
    print(clean_multiple_winners)
    print('\n')
    print(clean_nascar_winners)

    # Problem 05
    print("Problem 05:\n")
    youngest_manf, oldest_manf = cat_car_manufacturers(nascar_champs)
    print(youngest_manf)
    print('\n')
    print(oldest_manf)


if __name__ == "__main__":
    main()
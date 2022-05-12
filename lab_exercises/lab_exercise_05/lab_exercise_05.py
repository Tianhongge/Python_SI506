# START LAB EXERCISE 05
from unittest import result


print('Lab Exercise 05 \n')


# PROBLEM 01
def read_file(filepath, encoding='utf-8'):
    """Reads text file and returns each line as a list element.

    Parameters:
        filepath (str): path to file
        encoding (str): name of encoding used to decode the file

    Returns
        list: list of strings
    """
    with open(filepath, 'r', encoding=encoding) as file_obj:
        return file_obj.readlines()


# PROBLEM 02
def has_phrase(speech, phrase):
    """Loops over the speech and checks to see if a phrase is present in the speech.

    Parameters:
        speech (list): a list that contains the information from the speech
        phrase (str): the phrase a user is looking for

    Returns:
        bool: True or False depending on if the phrase exists in the speech
    """

    for line in speech:
        if phrase.lower() in line.lower():
            return True
    return False



# PROBLEM 03
def find_phrases(speech, phrases):
    """Loops over the list of phrases and uses find_phrase to check if the phrase exists in the speech.

    Parameters:
        speech (list): a list that contains the information from the speech
        phrases (list): the list of phrases someone is looking for

    Returns:
        list: a list of tuples that outlines the word and the number of times it appears
    """

    phrase_result = []

    for phrase in phrases:
        result = has_phrase(speech, phrase)
        phrase_tup = (phrase, result)
        phrase_result.append(phrase_tup)

    return phrase_result



# PROBLEM 04
def write_file(filepath, data, encoding='utf-8'):
    """Write content to a target file encoded as UTF-8. Each element in the passed in sequence is written to a new line.

    Parameters:
        filepath (str): path to target file (if file does not exist it will be created)
        data (list): list of tuples comprising the content to be written to the target file
        encoding (str): name of encoding used to decode the file

    Returns:
        None
    """

    with open(filepath, 'w', encoding=encoding) as file_obj:
        for line in data:
            file_obj.write(f"{line}\n")


def main():
    """
    Program entry point. Controls flow of execution. All function calls must be made from main().

    Parameters:
        None

    Returns:
        None
    """

    filepath = 'mandela-prepared_speech.txt'


    #PROBLEM 5
    speech = read_file(filepath)

    print(speech)

    phrases = ['Leadership',
            'Africa belongs to all the people who live in it',
            'The University of Michigan',
            'Sharpeville',
            'Umkhonto we Sizwe',
            'SI 506',
            'School of Information']

    present_phrases = find_phrases(speech, phrases)

    print(present_phrases)

    write_file('stu_find_phrases_results.txt', present_phrases)


    #PROBLEM 6
    phrase, result = present_phrases[0]
    print(phrase)
    print(result)


if __name__ == '__main__':
    main()


# END LAB EXERCISE
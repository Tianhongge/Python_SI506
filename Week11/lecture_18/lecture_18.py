# SI 506: Lecture 18

import json
import pprint
import re

from datetime import datetime


def has_subject(subjects, subject):
    """Determines if passed in < subject > string is in the passed in < subjects >
    list. If a match is obtained the boolean True is returned; otherwise False is
    returned.

    Parameters:
        subjects (list): list of "subject" string elements
        subject (str): string to locate in the < subjects > list

    Returns:
        bool: True if a match is obtained; otherwise False
    """

    for subj in subjects:
        if subj['name'] =='subject' and subj['value'] == subject:
            return True
    return False


def read_json(filepath, encoding='utf-8'):
    """Reads a JSON document, decodes the file content, and returns a list or dictionary if
    provided with a valid filepath.

    Parameters:
        filepath (str): path to file
        encoding (str): name of encoding used to decode the file

    Returns:
        dict/list: dict or list representations of the decoded JSON document
    """

    with open(filepath, 'r', encoding=encoding) as file_obj:
        return json.load(file_obj)


def write_json(filepath, data, encoding='utf-8', ensure_ascii=False, indent=2):
    """Serializes object as JSON. Writes content to the provided filepath.

    Parameters:
        filepath (str): the path to the file
        data (dict)/(list): the data to be encoded as JSON and written to the file
        encoding (str): name of encoding used to encode the file
        ensure_ascii (str): if False non-ASCII characters are printed as is; otherwise
                            non-ASCII characters are escaped.
        indent (int): number of "pretty printed" indention spaces applied to encoded JSON

    Returns:
        None
    """

    with open(filepath, 'w', encoding=encoding) as file_obj:
        json.dump(data, file_obj, ensure_ascii=ensure_ascii, indent=indent)


def main():
    """Program entry point.  Orchestrates program's flow of execution.

    Parameters:
        None

    Returns:
        None
    """

    # Configure pretty printer
    pp = pprint.PrettyPrinter(indent=2, sort_dicts=False, width=100)

    # CHALLENGE 01
    articles = read_json('E:/Coding/Python3.10/SI506/Week11/lecture_18/nyt-articles.json', encoding='utf-8') # TODO call function

    print(f"\nCh 01 Articles (n={len(articles)})")

    # Get 2022 articles only
    articles_2022 = []
    for article in articles:
        if article['pub_date'][:4] == "2022":
        # if article['pub_date'].startswith('2022'):
            articles_2022.append(article)

    # Write to file
    write_json('stu-nyt-articles-2022.json', articles_2022)


    # 2.0 NESTED LOOPS

    # Get all articles touching on Dementia
    dementia = []
    for article in articles:
        for keyword in article['keywords']:
            if keyword['name'] == 'subject' and keyword['value'] in ("Alzheimer's Disease", 'Dementia'):
                dementia.append(article)
                break
    # Implement loop

    print(f"\n2.0 Dementia articles (n={len(dementia)})")

    # Write to file
    write_json('stu-nyt-dementia-articles.json', dementia)


    # CHALLENGE 02

    # Get all subjects
    subjects = []
    for article in articles:
        for keyword in article ['keywords']:
            if keyword['name'] == 'subject' and keyword['value'] not in subjects:
                subjects.append(keyword['value'])

    # Subjects sorted (first 25)
    # print(f"\nCh 02 Subjects (n={len(subjects)}) = {sorted(subjects)[:25]}")

    # Write to file
    with open ('stu-subjects.txt', 'w') as file_obj:
        for subject in sorted(subjects):
            file_obj.write(f"{subject}\n")


    # CHALLENGE 03

    subject_counts = {}
    for subject in subjects:
        for article in articles:
            for keyword in article['keywords']:
                if keyword['name'] == 'subject' and keyword['value'] ==subject:
                    if subject not in subject_counts.keys():
                        subject_counts[subject] = 1
                    else:
                        subject_counts[subject] += 1
    # TODO Implement loop

    # Sort by value (reversed = -x[1]), then by key (x[0])
    # TODO Uncomment
    subject_counts = {k: v for k, v in sorted(subject_counts.items(), key=lambda x: (-x[1], x[0]))}

    # Subject counts
    # print(f"\nSubject counts (n={len(subject_counts)})")
    # pp.pprint(subject_counts)

    # Write to file
    # TODO Uncomment
    write_json('stu-nyt-subject_counts.json', subject_counts)


    # CHALLENGE 04

    subject_counts_fx = {}
    for subject in subjects:
        for article in articles:
            if has_subject(article['keywords'], subject):
                if subject not in subject_counts_fx.keys():
                    subject_counts_fx[subject] = 1
                else:
                    subject_counts_fx[subject] += 1

    # TODO Implement loop

    # Sort by value (reversed = -x[1]), then by key (x[0])
    # TODO Uncomment
    subject_counts_fx = {k: v for k, v in sorted(subject_counts_fx.items(), key=lambda x: (-x[1], x[0]))}

    # Assert dictionaries are equivalent.
    # TODO Uncomment
    assert subject_counts == subject_counts_fx


if __name__ == '__main__':
    main()
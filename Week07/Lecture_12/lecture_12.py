# SI 506: Lecture 12

import csv


def read_csv(filepath, encoding='utf-8', newline='', delimiter=','):
    """
    Reads a CSV file, parsing row values per the provided delimiter. Returns a list of lists,
    wherein each nested list represents a single row from the input file.

    WARN: If a byte order mark (BOM) is encountered at the beginning of the first line of decoded
    text, call < read_csv > and pass 'utf-8-sig' as the < encoding > argument.

    WARN: If newline='' is not specified, newlines '\n' or '\r\n' embedded inside quoted fields
    may not be interpreted correctly by the csv.reader.

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
        data = []
        reader = csv.reader(file_obj, delimiter=delimiter)
        for row in reader:
            data.append(row)

        return data


def read_file(filepath, encoding='utf-8', strip=True):
    """Read text file line by line. Remove whitespace and trailing newline
    escape character.

    Parameters:
        filepath (str): path to file
        encoding (str): name of encoding used to decode the file.
        strip (bool): remove white space, newline escape characters

    Returns
        list: list of lines in file
    """
    with open(filepath, 'r', encoding=encoding) as file_obj:
        if strip:
            data = []
            for line in file_obj:
                # data.append(line) # includes trailing newline '\n'
                data.append(line.strip()) # strip leading/trailing whitespace including '\n'
            return data

            # return [line.strip() for line in file_obj] # list comprehension (single line)
        else:
            return file_obj.readlines() # list


def write_csv(filepath, data, headers=None, encoding='utf-8', newline=''):
    """
    Writes data to a target CSV file. Column headers are written as the first
    row of the CSV file if optional headers are specified.

    WARN: If??newline=''??is not specified, newlines '\n' or '\r\n' embedded inside quoted
    fields may not be interpreted correctly by the csv.reader. On platforms that utilize
    `\r\n` an extra `\r` will be added.

    Parameters:
        filepath (str): path to target file (if file does not exist it will be created)
        data (list | tuple): sequence to be written to the target file
        headers (seq): optional header row list or tuple
        encoding (str): name of encoding used to encode the file
        newline (str): specifies replacement value for newline '\n'
                       or '\r\n' (Windows) character sequences

    Returns:
        None
    """
    with open(filepath, 'w', encoding=encoding, newline=newline) as file_obj:
        writer = csv.writer(file_obj)
        if headers:
            writer.writerow(headers)
            for row in data:
                writer.writerow(row)
        else:
            writer.writerows(data)


def write_file(filepath, data, encoding='utf-8', newline=True):
    """Write content to a target file encoded as UTF-8. If optional newline is specified
    append each line with a newline escape sequence (`\n`).

    Parameters:
        filepath (str): path to target file (if file does not exist it will be created)
        data (list | tuple): sequence of strings comprising the content to be written to the
                             target file
        encoding (str): name of encoding used to encode the file.
        newline (bool): add newline escape sequence to line

    Returns:
        None
    """
    with open(filepath, 'w', encoding=encoding) as file_obj:
        if newline:
            for line in data:
                file_obj.write(f"{line}\n") # add newline
        else:
            file_obj.writelines(data) # write sequence to file


def main():
    """Program entry point. Orchestrates execution flow.

    Parameters:
        None

    Returns:
        None
    """

    # 3.0 FILES

    filepath = './umsi-faculty.txt' # relative path
    # filepath = 'umsi-faculty.txt' # alternative

    # 3.1 OPEN/CLOSE FILE (YE OLDE WAY)

    file_obj = open(filepath) # TODO open
    data = file_obj.read() # TODO read: returns a single string
    # TODO CLOSE # close (REQUIRED)
    file_obj.close()
    print(f"\n3.1 faculty names .read()\n{data}")


    # 3.2 WITH STATEMENT (RECOMMENDED WAY)

    # TODO open with with()
    with open(filepath) as file_obj:
       data = file_obj.read() # TODO read returns a single string

    # print(f"\n3.2 with open() statement)\n{data}")


    # 3.3 FILE OPENING MODES

    with open(filepath, 'r') as file_obj: # open in read mode
        data = file_obj.read()

    # print(f"\n3.3 read mode ('r')\n{data}")

    # TODO Uncomment
    with open('./umsi-faculty-v2.txt', 'w') as file_obj: # open in write mode
        file_obj.write(data) # writes string to file


    # 3.4 READ METHODS (READLINE(), READLINES())

    # 3.4.1 READLINE()

    with open(filepath, 'r') as file_obj: # open in read mode
        data = file_obj.readline()
        # data += file_obj.readline() # UNCOMMENT: call n times but not efficient
        # data += file_obj.readline() # UNCOMMENT: call n times but not efficient
        # data += file_obj.readline() # UNCOMMENT: call n times but not efficient

    # print(f"\n3.4.1 faculty names .readline()\n{data}")


    # 3.4.2 READLINES()

    with open(filepath, 'r') as file_obj: # open in read mode
        data = file_obj.readlines() # returns list; elements include trailing '\n'

    # print(f"\n3.4.2.1 faculty names .readlines() (type={type(data)}\n{data}")

    # print(f"\n3.4.2.2 faculty .readlines(), .join()\n{''.join(data)}") # print string (pretty)


    # 3.4.3 GOTCHA: READ(), READLINES() LIMITED TO ONE CALL ONLY

    with open(filepath, 'r') as file_obj: # open in read mode
        data = file_obj.read()
        data_lines = file_obj.readlines() # WARN: does not execute

    # print(f"\n3.4.3 data_lines list is empty = {data_lines}\n")


    # 3.5 WRITE METHODS (WRITE(), WRITELINES())

    # 3.5.1 WRITE STR TO FILE WITH WRITE()

    with open(filepath, 'r') as file_obj: # open in read mode
        data = file_obj.read() # returns a single multiline string

    # TODO Write file

    data = read_file(filepath)

    for i in  range(len(data)):
        name = data[i].strip().split(', ')
        data[i] = f"{name[1]} {name[0]}"

    print(f"DATA = {data}")

    write_file('./umsi-faculty-reversed.txt', data)

    # 3.5.2 WRITE SEQUENCE TO FILE WITH WRITELINES()

    with open(filepath, 'r') as file_obj: # open in read mode
        data = file_obj.readlines() # returns a list

    # Reverse names

    # TODO Implement for loop


    # WARN: does not update string
    # for faculty_member in data:
    #     name = faculty_member.strip().split(', ') # strip \n
    #     faculty_member = f"{name[1]} {name[0]}\n" # does not update string element

    # TODO Uncomment
    # with open('./umsi-faculty-v4.txt', 'w') as file_obj: # open in write mode
    #     file_obj.writelines(data)


    # 3.5.3 WRITE SEQUENCE TO FILE WITH WRITE()

    with open(filepath, 'r') as file_obj: # open in read mode
        data = file_obj.readlines() # returns a list

    with open('./umsi-faculty-v5.txt', 'w') as file_obj: # open in write mode
        for row in data:
            # Surname only
            pass # TODO Implement

    # 3.5.4 CALL READ_FILE() / WRITE_FILE() INSTEAD

    # Get data
    data = read_file(filepath)

    # Access surnames first before calling function
    surnames = []
    for row in data:
        pass # TODO Implement (trailing \n not required)

    # Bonus: List comprehension (elegant list creation in a single line)
    # surnames = [row.split(', ')[0] for row in data]

    # Write surnames to file
    write_file('./umsi-faculty-v6.txt', surnames)


    # 4.0 CSV FILES

    # 4.3 RESNICK RECOMMENDER SYSTEMS

    # 4.3.1 Read CSV file and retrieve data
    # filepath = './resnick-publications.csv'
    filepath = 'E:\Coding\Python3.10\SI506\Week07\Lecture_12\resnick-publications.csv'
    publications = read_csv(filepath) # TODO call function

    # print(f"\n3.0: Total publications (rows) = {len(publications)}")

    # 4.3.2 Get headers
    headers = publications[0] # header row

    # print(f"\n3.0: Total elements (columns) = {len(headers)}")

    # 4.3.3 Filter title on "recommender"; accumulate results
    recommender_publications = []
    for publication in publications:
        if 'recommender' in publication[headers.index('title')].lower():
            recommender_publications.append(publication)

    # TODO Implement loop

    # 4.3.4 Write CSV file
    # TODO Uncomment
    filepath = './resnick-recommender_publications.csv'
    # write_csv(filepath, recommender_publications, headers)


if __name__ == '__main__':
    main()

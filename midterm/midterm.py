import csv


def classify_county_vax_level(county, headers, column_name):
    """Classifies a county according to a three-tiered ranking scheme.
    Classification of a target population (e.g., residents 65 years and older)
    is based on the corresponding "Series_Complete_*" column name passed in by
    the caller. Delegates to < get_county_attribute > the task of returning the
    (converted) percentage value of the county's target population who are fully
    vaccinated.

    Classifying a county is based on the following scheme.

    Tiers:
        High: greater than or equal to 75% of target population vaccinated fully
        Moderate: greater than or equal to 50% but less than 75% of target population
                  vaccinated fully
        Low: less than 50% of target population vaccinated fully

    Once the county is classified the function returns to the caller one of
    three labels: 'High', 'Moderate', 'Low'.

    Parameters:
        county (list): county-specific vaccination data
        headers (list): column names sourced from the first row of the CSV file
        column_name (str): header value used to look up the index value of the
                           target county list element

    Returns:
        str: classification label
    """

    rate = get_county_attribute(county, headers, column_name)
    if rate >= 75:
        return 'High'
    elif 50 <= rate <75:
        return 'Moderate'
    elif rate < 50:
        return 'Low'


def clean_county_data(county):
    """Mutates the passed in < county> list by converting numbers masquerading as
    strings to either an integer or float depending on whether or not the string
    representing a number that contains a fractional component (i.e., decimal).

    Checks each string element in the < county > list. Delegates to the function
    < is_floating_point_number > the task of confirming whether or not the string represents a
    float. If the expression evaluates to True, the string is converted to a
    float and assigned to the element. Delegates to the function < is_whole_number > the
    task of confirming whether or not the string represents an integer. If the
    expression evaluates to True, the string is converted to a
    int and assigned to the element. If the string does not represent a number
    it is ignored.

    Parameters:
      county (list): county-specific vaccination data

    Returns:
        None
    """

    for i in range(len(county)):
        if is_floating_point_number(county[i]):
            county[i] = float(county[i])
        elif is_whole_number(county[i]):
            county[i] = int(county[i])


def count_vax_adults_18to64(counties, headers):
    """Accumulates a count of all residents considered fully vaccinated between the
    ages of 18 and 64 (inclusive) across all < counties > provided by the caller.
    Delegates to < get_county_attribute > the task of retrieving each county's
    "Series_Complete_18Plus" and "Series_Complete_65Plus" values.

    Parameters:
        counties (list): nested lists of county-specific vaccination data
        headers (list): column names sourced from the first row of the CSV file

    Returns
        int: count of fully vaccinated residents between the ages of 18 and 64
    """
    count = 0
    i = 0
    for i in range(len(counties)):
        count = count + int(get_county_attribute(counties[i], headers, 'Series_Complete_18Plus')) - int(get_county_attribute(counties[i], headers, 'Series_Complete_65Plus'))
        i += 1
    return count

def get_counties_by_ur_codes_and_vax_level(counties, headers, ur_codes, vax_level='Low'):
    """Returns a list comprising zero or more formatted strings representing counties
    filtered on a tuple of urban/rural < ur_codes > and a < vax_level > code. The
    passed in < headers > list is employed to look up index values associated with
    the nested county elements.

    String format:
        Each "county" list element string is formatted as follows:

        < Recip_County > (< UR_Code >-< UR_Code_Name >) vax level: < Vax_Level >

        Example: "Lapeer County (2-Large fringe metro) vax level: Low"

    Parameters:
        counties (list): nested lists of county-specific vaccination data
        headers (list): column names sourced from the first row of the CSV file
        ur_codes (tuple): comprises one or more integer UR Code items
        vax_level (str): Three-tiered ranking scheme: High, Moderate, Low.
                         Default = "Low"

    Returns:
        list: formatted "county" strings
    """

    counties_list = []
    for county in counties:
        if county[headers.index('UR_Code')] in ur_codes and county[headers.index('Vax_Level')] == vax_level:
            counties_list.append(f"{county[headers.index('Recip_County')]} ({county[headers.index('UR_Code')]}-{county[headers.index('UR_Code_Name')]}) vax level: {county[headers.index('Vax_Level')]}")
    return counties_list


def get_counties_with_lowest_vax_rate(counties, headers, column_name):
    """Returns a list comprising one or more formatted strings representing counties
    with the lowest vaccination rate for a designated age group. Ties are accomodated.
    Delegates to < get_county_attribute > the task of returning the county vaccination
    rate for a given age group. The age group is determined by passing to
    < get_county_attribute > the < headers > and a "*_Pop_Pct" < column_name > string
    as arguments.

    Acceptable < column_name > values include:

    Series_Complete_Pop_Pct
    Series_Complete_12PlusPop_Pct
    Series_Complete_18PlusPop_Pct
    Series_Complete_65PlusPop_Pct

    String format:
        Each "county" list element string is formatted as follows:

        < Recip County > (< rate >%)

        Example: "Hillsdale County (70.9%)"

    Parameters:
        counties (list): nested lists of county-specific vaccination data
        headers (list): column names sourced from the first row of the CSV file
        column_name (str): header value used to look up the index value of the
                           target county list element

    Returns:
        list: formatted "county" strings
    """

    lowest_rate = 100
    i = 0
    for i in range(len(counties)):
        if get_county_attribute(counties[i], headers, column_name) < lowest_rate:
            lowest_rate = get_county_attribute(counties[i], headers, column_name)
            i += 1

    counties_lowest_rate = []
    for county in counties:
        if county[headers.index(column_name)] == lowest_rate:
            counties_lowest_rate.append(f"{county[3]} ({lowest_rate}%)")

    return counties_lowest_rate


def get_county(counties, county_name):
    """Employs the passed in < county_name > as a filter in order to return
    the corresponding county element from the passed in list of counties. Name
    matching is case-insensitive. If no match is obtained the function returns
    None.

    Parameters:
        counties (list): nested lists of county-specific vaccination data
        county_name (str): name of county

    Returns:
        county (list): county list with a name value that matches the < county_name >
    """

    for county in counties:
        if county[3].lower() == county_name.lower():
            return county


def get_county_attribute(county, headers, column_name):
    """Returns a < county > list element by looking up its index value in
    the accompanying < headers > list using the < column_name > as the target
    header value.

    Parameters:
        county (list): county-specific vaccination data
        headers (list): column names sourced from the first row of the CSV file
        column_name (str): header value used to look up the index value of the
                           target county list element

    Returns:
        str: element sourced from passed in publication list
    """

    return county[headers.index(column_name)]


def get_county_nchs_codes(nchs_codes, county):
    """Returns the NCHS urban/rural codes and descriptors, comprising the
    < cbsa_title >, < ur code > (converted to int), and < ur code_name >
    associated with the matching county name value derived from the passed in
    < county > list. Name matching is case-insensitive. If no match is
    obtained the function returns None.

    Parameters:
        nchs_codes (list): nested lists of NCHS urban/rural codes and descriptors
        county (list): county-specific vaccination data

    Returns:
        tuple: three-item tuple containing the < cbsa_title >, < code >, and
               < code_name > for a given county
    """

    for code in nchs_codes:
        if code[1].lower() == county[3].lower():
            return code[2], int(code[3]), code[4]


def is_floating_point_number(string):
    """Checks if a floating point number (e.g., a number that includes a fractional
    component) is masquerading as a string.

    WARN: function relies on str.isnumeric() behavior. Strings like "24.5" and
    "-1" are not considered numeric due to the presence of the period ('.') and
    the dash ('-') respectively.

    Parameters:
        string (str): Non-decimal number (e.g., '55363') cast as a string

    Returns:
        bool: True if string is a number with a decimal component; False otherwise.
    """

    try:
        return True if not string.isnumeric() and float(string) else False # ternary operator
    except ValueError:
        return False


def is_whole_number(string):
    """Checks if a whole number (i.e., an integer) is masquerading as a string.

    WARN: function relies on str.isnumeric() behavior. Strings like "24.5" and
    "-1" are not considered numeric due to the presence of the period ('.') and
    the dash ('-') respectively.

    Parameters:
        string (str): Non-decimal number (e.g., '55363') cast as a string

    Returns:
        bool: True if string can be converted to an integer; False otherwise.

    """

    try:
        return True if string.isnumeric() and int(string) else False # ternary operator
    except ValueError:
        return False


def read_csv(filepath, encoding='utf-8', newline='', delimiter=','):
    """
    Reads a CSV file, parsing row values per the provided delimiter. Returns a list of lists,
    wherein each nested list represents a single row from the input file.

    WARN: If a byte order mark (BOM) is encountered at the beginning of the first line of decoded
    text, call < read_csv > and pass 'utf-8-sig' as the < encoding > argument.

    WARN: If newline='' is not specified, newlines '\n' or '\r\n' embedded inside quoted fields
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


def write_csv(filepath, data, headers=None, encoding='utf-8', newline=''):
    """
    Writes data to a target CSV file. Column headers are written as the first
    row of the CSV file if optional headers are specified.

    WARN: If newline='' is not specified, newlines '\n' or '\r\n' embedded inside quoted
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


def main():
    """Entry point for script.

    Parameters:
        None

    Returns:
        None
    """

    # CHALLENGE 01

    wash_data = read_csv('./mi-covid-washtenaw-20220220.csv')

    max_positivity_rates = wash_data[1:7]
    week_04 = wash_data[-8:-1]
    odd_days = wash_data[1::2]



    # CHALLENGE 02

    # CDC County vaccination data
    vax_data = read_csv('./mi-covid-vax_counties-20220219.csv')
    vax_headers = vax_data[0]
    vax_counties = vax_data[1:]

    jackson_cty = get_county(vax_counties, 'jackson county')
    # print(jackson_cty)

    # CHALLENGE 03

    jackson_cty_vax_complete_pct = float(get_county_attribute(jackson_cty, vax_headers, 'Series_Complete_Pop_Pct'))
    # print(jackson_cty_vax_complete_pct)

    # CHALLENGE 04

    for county in vax_counties:
        clean_county_data(county)
    # print(vax_counties)

    # CHALLENGE 05

    vax_adults_18to64 = count_vax_adults_18to64(vax_counties, vax_headers)
    # print(vax_adults_18to64)

    # CHALLENGE 06

    for county in vax_counties:
        county.insert(5, classify_county_vax_level(county, vax_headers, 'Series_Complete_Pop_Pct'))

    vax_headers.insert(5, 'Vax_Level')

    write_csv('stu-vax_levels.csv', vax_counties, vax_headers)

    # CHALLENGE 07

    # NCHS County UR codes
    nchs_codes_data = read_csv('./mi-nchs-urban_rural_codes.csv') # TODO Call function
    nchs_codes_headers = nchs_codes_data[0] # TODO Assign
    nchs_codes = nchs_codes_data[1:] # TODO Assign

    # TODO Implement function < get_county_nchs_codes >

    ingham_cty = get_county(vax_counties, 'Ingham County') # TODO Call function
    ingham_cty_ur_code = get_county_nchs_codes(nchs_codes, ingham_cty) # TODO Call function
    # print(ingham_cty_ur_code)

    # CHALLENGE 08

    # TODO Implement function < get_counties_with_lowest_vax_rate >

    lowest_vax_rates_12_plus = get_counties_with_lowest_vax_rate(vax_counties, vax_headers, 'Series_Complete_12PlusPop_Pct') # TODO Call function

    lowest_vax_rates_18_plus = get_counties_with_lowest_vax_rate(vax_counties, vax_headers, 'Series_Complete_18PlusPop_Pct') # TODO Call function

    lowest_vax_rates_65_plus = get_counties_with_lowest_vax_rate(vax_counties, vax_headers, 'Series_Complete_65PlusPop_Pct') # TODO Call function

    # print(lowest_vax_rates_12_plus)
    # print(lowest_vax_rates_18_plus)
    # print(lowest_vax_rates_65_plus)

    # CHALLENGE 09

    for i in range(len(vax_counties)):
        cbsa_title, ur_code, ur_code_name = get_county_nchs_codes(nchs_codes, vax_counties[i])
        vax_counties[i].insert(5, cbsa_title)
        vax_counties[i].insert(6, ur_code)
        vax_counties[i].insert(7, ur_code_name)

    vax_headers.insert(5, 'CBSA_Title')
    vax_headers.insert(6, 'UR_Code')
    vax_headers.insert(7, 'UR_Code_Name')

    write_csv('stu-ur_vax_levels.csv', vax_counties, vax_headers)


    # CHALLENGE 10

    # TODO Implement function < get_counties_by_ur_codes_and_vax_level >

    metro_moderate_vax_rates = get_counties_by_ur_codes_and_vax_level(vax_counties, vax_headers, (1, 2), 'Moderate') # TODO Call function

    metro_low_vax_rates = get_counties_by_ur_codes_and_vax_level(vax_counties, vax_headers, (1, 2)) # TODO Call function

    noncore_low_vax_rates = get_counties_by_ur_codes_and_vax_level(vax_counties, vax_headers, (6,)) # TODO Call function

    # print(metro_moderate_vax_rates)
    # print(metro_low_vax_rates)
    # print(noncore_low_vax_rates)

# Do not modify or remove this if statement
if __name__ == '__main__':
    main()
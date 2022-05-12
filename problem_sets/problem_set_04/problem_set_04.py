musicians = [['name', 'city', 'state', 'instruments', 'inspiration', 'birth_date', 'death_date'],
    [' Christian Scott Atunde Adjuah ', 'New Orleans', 'LA', ['trumpet'], 'Miles Davis', 'Mar 1983'],
    ['Ron Carter ', 'Ferndale', 'mi', ['double bass', 'cello'], 'Miles Davis', 'May 4, 1937'],
    [' Alice Coltrane ', 'Detroit', 'MI', ['piano', 'harp', 'vocals'], 'Ernest Farrow', '1937', '2007'],
    ['Esperanza Spalding', 'Portland', 'OR', ['double bass', 'guitar', 'vocals'], 'Ron Carter', '1984'],
    [' Robert Glasper ', 'Houston', 'tx', ['piano'], 'Herbie Hancock', 'April 1978'],
    [' Marquis Hill ', 'Chicago', 'IL', ['trumpet'], 'Lee Morgan', 'April 15, 1987'],
    [' Dorothy Ashby', 'Detroit', 'Mi', ['harp', 'piano', 'koto'], 'Omar Khayyam', 'Aug 1932', '1986'],
    ['Walter Smith III ', 'Houston', 'Tx', ['saxophone'], 'John Coltrane', 'Sept 24, 1980'],
    [' Cecile McLorin Salvant', 'Miami', 'fL', ['vocals'], 'Sarah Vaughan','August 28, 1989'],
    [' Sarah Elizabeth Charles', 'Springfield', 'MA', ['vocals'], 'Sarah Vaughan', '1989'],
    ['Miles Davis', 'Alton', 'iL', ['trumpet', 'cornet', 'piano'], 'Elwood Buchanan','1926', '1991'],
    ['John Coltrane', 'Hamlet', 'Nc', ['saxophone'], 'Alice Coltrane', 'Sep 1926', 'July 17, 1967'],
    ['Herbie Hancock', 'Chicago', 'il', ['piano', 'keyboard'], 'Miles Davis', '1940'],
    ['Roy Brooks ', 'Detroit', 'MI', ['drums'], 'Lionel Hampton','March 9, 1938', '2005'],
    ['Wayne Shorter', 'Newark', 'nj', ['saxophone'], 'John Coltrane', 'Aug 25, 1933'],
    [' Bobbi Humphrey', 'Marlin', 'TX', ['flute', 'vocals'], 'Herbie Mann', '1950'],
    [' Thelonius Monk', 'Rocky Mount', 'NC', ['piano'], 'Duke Ellington', '1917', 'February 17, 1982']
]

# PROBLEM 1 (16 POINTS)
def clean_list(info):
    if len(info) == 6:
        info.append(None)
    else:
        info[6] = int(info[6][-4:])
    info[0] = info[0].strip()
    info[2] = info[2].lower()
    info[5] = int(info[5][-4:])

for musician in musicians[1:]:
    clean_list(musician)


print(f'\nProblem 1: musicians =\n{musicians}')


# PROBLEM 2 (16 POINTS)
def get_state(info):
    return info[2]

mi_musicians = []

for musician in musicians:
    if get_state(musician) == 'mi':
        mi_musicians.append(musician[0])


print(f'\nProblem 2: mi_musicians =\n{mi_musicians}')


# PROBLEM 3 (16 POINTS)
south_states = ['al', 'ar', 'de', 'fl', 'ga', 'ky', 'la', 'md', 'ms',
    'nc', 'ok', 'sc', 'tn', 'tx', 'va', 'wv']

northeast_states = ['ct', 'ma', 'me', 'nh', 'nj', 'ny', 'pa', 'ri', 'vt']

def is_from_region(info, region):
    if get_state(info) in region:
        return True
    else:
        return False

southerners = []
northeasterners = []
for musician in musicians:
    if is_from_region(region=south_states, info=musician) == True:
        southerners.append(tuple([musician[0], musician[2]]))
    elif is_from_region(region=northeast_states, info=musician) == True:
        northeasterners.append(tuple([musician[0], musician[2]]))

print(southerners)
print(northeasterners)

# PROBLEM 4 (16 POINTS)
def is_inspired(info, inspo, idx=4):
    if inspo.lower() == info[idx].lower():
        return True
    else:
        return False

davis_count = 0
for musician in musicians[1:]:
    if is_inspired(musician, 'Miles Davis') == True:
        davis_count += 1

davis_percent =round(davis_count / len(musicians[1:]) * 100, 2)
print(davis_percent)

# PROBLEM 5 (16 POINTS)
def calculate_age(info, end_year=2022):
    return tuple([info[0], int(end_year) - info[-2]])

min_age = 200
youngest_musicians = []
for musician in musicians[1:]:
    (name_musician, age_musician) = calculate_age(musician)
    if age_musician < min_age:
        min_age = age_musician

for musician in musicians[1:]:
    if int(2022 - musician[-2]) == min_age:
        youngest_musicians.append(musician[0])

print(youngest_musicians)

# PROBLEM 6 (20 POINTS)
past_musicians = []
current_musicians = []
items = musicians[1:]
i = 0
while i < len(musicians[1:]):
    if not items[i][-1] is None:
        past_musicians.append(calculate_age(items[i], items[i][-1]))
    else:
        current_musicians.append(calculate_age(items[i]))
    i += 1

print(past_musicians)
print(current_musicians)



# PROBLEM 7 (25 POINTS)
def plays_woodwind(info, idx=3):
    woodwinds = ['clarinet', 'trumpet', 'saxophone', 'flute', 'bassoon',
        'oboe', 'trumpet', 'piccolo', 'cornet']
    for instrument in info[idx]:
        if instrument in woodwinds:
            return True
    else:
        return False


wind_musicians = 0
for musician in musicians[1:]:
    if plays_woodwind(musician) == True:
        wind_musicians += 1

print(wind_musicians)
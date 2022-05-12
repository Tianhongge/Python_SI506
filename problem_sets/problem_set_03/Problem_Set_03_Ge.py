# Problem Set 3

# SETUP
chinese_holidays = [
    ['Holiday Name', 'Date', 'Number of Days off', 'Official Public Holiday'],
    ["New Year's Day", '2022-01-01', '3 days off', False],
    ['Spring Festival', '2022-02-01', '7 days off', True],
    ['Lantern Festival', '2022-02-15', '0 days off', False],
    ['Qingming Festival', '2022-04-05', '3 days off', True],
    ['Labor Day', '2022-05-01', '5 days off', True],
    ['Dragon Boat Festival', '2022-06-03', '3 days off', True],
    ['Qixi Festival', '2022-08-04', '0 days off', True],
    ['Mid-Autumn Festival', '2022-09-10', '3 days off', True],
    ['National Day', '2022-10-01', '7 days off', False],
    ['Double Ninth Festival', '2022-10-04', '0 days off', True]
]

activities = [
    ["New Year's Day", 'Decorating Houses | Eating Dumplings'],
    ['Spring Festival', 'Exchanging Red Envelopes | Family Reunion Dinner'],
    ['Lantern Festival', 'Watching Lanterns | Eating Tangyuan'],
    ['Qingming Festival', 'Tomb Sweeping | Spring Outing'],
    ['Labor Day', 'Visiting Tourist Spots | Shopping'],
    ['Dragon Boat Festival', 'Dragon Boat Racing | Eating Zongzi'],
    ['Qixi Festival', 'Dating | Shopping'],
    ['Mid-Autumn Festival', 'Eating Mooncakes | Family Reunion Dinner'],
    ['National Day', 'Military Parade | Visiting Tourist Spots'],
    ['Double Ninth Festival', 'Climbing Mountain | Eating Chongyang Cakes']
]


# Problem 1
header = chinese_holidays[0]
holidays = chinese_holidays[1:]

for holiday in holidays:
    holiday[2] = int(holiday[2].replace(' days off', ''))
    if holiday[2] == 0:
        holiday[3] = False
    else:
        holiday[3] = True

print(chinese_holidays)


# Problem 2
num_holidays = 0

for holiday in chinese_holidays[1:]:
    if holiday[3] == True:
        num_holidays += 1

print(num_holidays)


# Problem 3
public_holidays = []
other_holidays = []

for holiday in chinese_holidays[1:]:
    if holiday[3] == True:
        public_holidays.append(holiday[0])
    else:
        other_holidays.append(holiday[0])

print(public_holidays)
print(other_holidays)


# Problem 4
long_break = []
medium_break = []
short_break = []
no_break = []

for holiday in chinese_holidays[1:]:
    if holiday[2] == 0:
        no_break.append(holiday[0])
    elif holiday[2] > 0 and holiday[2] <= 3:
        short_break.append(holiday[0])
    elif holiday[2] > 3 and  holiday[2] <= 5:
        medium_break.append(holiday[0])
    else:
        long_break.append(holiday[0])

print(long_break)
print(medium_break)
print(short_break)
print(no_break)


# Problem 5

newholidays = chinese_holidays[1:]
i = 0
while i < len(newholidays):
    newholidays[i][1] = newholidays[i][1].split('-')
    i += 1

print(chinese_holidays)


# Problem 6
holidays = chinese_holidays[1:]
for i in range(len(holidays)):
    if int(holidays[i][1][1]) >=3 and int(holidays[i][1][1]) <=5:
        holidays[i].insert(0, 'Spring')
    elif int(holidays[i][1][1]) >=6 and int(holidays[i][1][1]) <=8:
        holidays[i].insert(0, 'Summer')
    elif int(holidays[i][1][1]) >=9 and int(holidays[i][1][1]) <=11:
        holidays[i].insert(0, 'Fall')
    elif int(holidays[i][1][1]) == 12 or 1 or 2:
        holidays[i].insert(0, 'Winter')

print(chinese_holidays)


# Problem 7
j = 0
while j < len(activities):
    if 'eating zongzi' in activities[j][1].lower():
        dragon_boat_activities = activities[j][-1].split(' | ')
    j += 1

print(dragon_boat_activities)
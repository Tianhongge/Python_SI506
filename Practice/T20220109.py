#Number_Integers
print(-25)

my_int = -25
print(my_int)

int_ans = 150-100
print(int_ans)

#Number_Floating-Point
print(17.3)

my_flt = 17.3
print(my_flt)

my_flt = 45.57 + 35.99
print(my_flt)

#Booleans
my_bool = 400 > 100
print(my_bool)

#Strings
hw = "hello, world!"
print(hw)

#Lists a changeable, ordered sequence of elements
sea_creatures = ['sharks','squid','shrimp']
print(sea_creatures)

#Tuples an unchangeable, ordered sequence of elements
coral = ('blue coral','staghorn coral','pillar coral')
print(coral)

#Dictionaries
sammy = {'name': 'Sammy', 'animal': 'shark', 'color': 'blue', 'location': 'ocean'}
print(sammy['animal'])


#Chapter2 Variables, expressions, and statements
#2.1 Values and types
#What type a value has
type('Hello,World!')
type(12)
type(2.2)
type('34')

#2.2 Variables
#An assignmnet statement creates new variables and give them values
message = 'And how for something completely different'
n = 17
pi = 3.1415926

print(message)
print(n)
print(pi)

type(message)
type(n)
type(pi)

#2.3 Variable names and keywords: 1. cannot start with a number 2. better to start with a lowercase letter(uppercase letter is allowed)
#Python reserves 35 keywords:
#and del from None True as elif global nonlocal try assert else if not while break except import or with class False in pass yield countinue finally is raise async def for lambda return await

#2.4 Statements 语句
print(1)
x = 2
print(x)

#2.5 Operators and operands 运算符与运算对象
20+32
hour = 23
minute = 46
hour-1
hour*60+minute
minute/60
5**2
(5+9)*(15-7)

#'/' & '//' 
minute = 46
minute/60
minute//60

#2.6 Expressions: an expression is a combination of value, variables, and operators

#2.7 Order of operations

#2.8 Modulus operator 模运算 对整数运算得到相除的remainder  
#检验数是否能被整除
remainder = 7%3
print(remainder)

#提取数字最后边的数位
x = 101
rightnum = x%100
print(rightnum)

#2.9 String operations
first = '100'
second = '150'
print(first+second)

first = 'Test '
second = 3
print(first*second)

#2.10 Asking the user for input
name = input('What is your name?\n')
#'\n'为换行符，user可以在提示语的下一行输入input的内容
print(name)

prompt = 'What... is the airspeed velocity of an unladen swallow?\n'
speed = input(prompt)
int(speed)

#2.11 Comments

#2.12 Choosing mnemonic variable names

#2.13 Debugging

#2.14 Glossary

#2.15 Exercise
#EX2
name = input('What is your name?\n')
print('Hello ' + name)

#EX3
hours = input('Enter your hours\n')
rate = input('Enter your rate per hour\n')
pay = int(hours) * int(rate)
print('Your gross pay is ' + str(pay))


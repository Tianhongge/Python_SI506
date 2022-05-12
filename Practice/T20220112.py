# An introduction to working with Strings in Python3

## Creating and printing strings
from cgi import print_environ_usage


print("Let's print out this strings")

## String concatenation
print("Sammy" + "Shark")

print("Sammy " + "Shark")

### Be sure not to use + operator between two different data type like
print("Sammy" + 27) 

##String replication
print("Sammy" * 9)

## Storing strings in variables
my_str = "Sammy likes declaring strings"
print(my_str)


# How to format text in Python 3

## String literals
### Difference between string literal and string value: string literal is "Hello, World!", string value is Hello, World!
print('Sammy says, "Hello!"')

## Multiple lines
print(
'''
This strings is on
multiple lines
'''
)

##Escape characters 当某个符号被多次使用时，在前面加上\可以实现escape characters，避免识别错误
print("Sammy says, \"Hello!\"")

print('Sammy\'s balloon is red.')
### \n: Line break
print("This string\nspans multiple\nlines.")
### \t: Tab
print("1.\tShark\n2.\tShrimp\n3.\tSquid")

#Raw strings
###当我们不希望计算机识别\时
print(r"Sammy says,\"The balloon\'s color is red.\"")


# An introduction to string function in Python 3

## Making strings upper and lower case
ss = "Sammy Shark"
print(ss.upper())
print(ss.lower())

## Boolean methods 布尔值 判断
number = "5"
letter = "abcdef"
print(number.isnumeric())
print(letter.isnumeric())

movie = "2001: A SAMMY ODYSSEY"
book = "A Thousand Splendid Shark"
poem = "sammy lived in a pretty how town"
print(movie.islower())
print(book.istitle())
### str.isalnum()  str.isalpha()  str.islower()  str.isnumeric()  str.isspace()  str.istitle()  str.upper()

## Determining string length 
open_source = "Sammy contributed to open source."
print(len(open_source))

## join(), split() and replace method
balloon = "Sammy has a balloon."
print(" ".join(balloon))
print("".join(reversed(balloon)))
print(",".join(["sharks","crustaceans","plankton"]))
print(balloon.split())
print(balloon.split("a")) #字母a被remove并在此处打断
print(balloon.replace("has","had"))

# Oreilly Introduction of lists
bicycles = ['trek','cannondale','readline','specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[3])
print(bicycles[-1])
message = f"My first bicycle was a {bicycles[0].title()}"
print(message)

## Changing, adding, and removing elements
### Modifying elements in a list
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

### Adding elements to a list
motorcycles = ['honda','yamaha','suzuki']
motorcycles.append('ducati')
print(motorcycles)

motorcycles = ['honda','yamaha','suzuki']
motorcycles.insert(0,'ducati')
print(motorcycles)

### Removing elements from a list
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)

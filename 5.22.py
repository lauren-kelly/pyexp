# variables
# notes:
# must start with a letter or _
_myName = "Lauren"
# not a number
# 1stname= "something" causes an error - it won't skip it
name1 = "something"
_MyName = "gawd for real? why?"

print(_myName + _MyName + name1)

greeting = "My age is"
# age = input("What is your age?")
# input will automatically put input in as a string. innnnnteresting.
# otherwise to add in a number it has to be in string format, not int
# age = 99 fails
age = "99"

print(greeting + age)

# an integer is here
a = 12

# a float is different
b = 3
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a % b)

for i in range(1, a//b):
    print(i)

print(a + b / 3 - 4 * 12)
print((a + b) // 3)
print((((a + b) // 3) - 4) * 12)
print((((a + b) / 3) - 4) * 12)
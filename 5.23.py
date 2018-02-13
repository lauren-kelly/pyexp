a = 12
b = 3
c = a + b
d = c / 3
e = d - 4
print(e * 12)

# strings - sequence data types

parrot = "Norwegian Blue"
print(parrot)
print(parrot[3])
print(parrot[-10])
print(parrot[0:6])
# start at 0 - show me 6 characters total.

print(parrot[:6])
# start at 0 (empty) - show up to (not including 6)
print(parrot[3:])
# start at 3 show me the rest

print(parrot[-4:-2])
# start 4 from the end, and go to -2

print(parrot[0:6:2])
# start at 0 - go as far as 6 - show every 2nd char (so jump one)
# N _ r _ e

print(parrot[0:6:3])
# start at 0, go as far as 6 - show every 3rd (jump 2)
# N _ _ w _ _


number = "9,876,543,210,654,321"
numbers = "1, 2, 3, 4, 5, 6, 7, 8, 9"

print(number[1::4])
# start at 1 - go to the end, skip 3
# _ , _ _ _ , etc
print(numbers[0::3])
# start at 0, go to the end, skip 2 (show every 3rd)
# 1 _ _ 2 _ _ 3

string1 = "he's "
string2 = "probably "
print(string1 + string2)
print("he's " "probably " "pining")
print("hello" *5)
# print("hello " *5 +4)
print("hello " * (5 +4))
print("hello " * 5 + "4")

today = "friday"
print("day" in today)
print("fri" in today)
print("thurs" in today)
print("parrot" in "fjord")

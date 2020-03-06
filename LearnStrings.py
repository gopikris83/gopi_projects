# Printing slicing strings

e = 'Hello, Python'
print ("Slicing of Strings")
print (e[2:19])
print()

# Get the length of the string and Negative Index

a = "Hello, World!"
print("Get the Length :", len(a))
print (a[-19:])

# Using Strip method in Strings

r = '   Hello, Ani!   '
print("Print Stripped value:", r.strip())

# Using lower method in Strings

r = '   Hello, ANI!   '
print("Print Lower Case:", r.lower())


# Using upper method in Strings

r = '   Hello, ANI!   '
print("Print upper Case:", r.upper())

# Using replace method in Strings

r = '   Hello, Anirudh!   '
print("Print replacing value:", r.replace('Anirudh', 'honeyrudh'))

# Using Split method in strings

s = 'Hi, Vaiga'
print (s.split(","))
print()

# Check strings. Using in or not in

t = 'The python language is introduced in 1989 before Java'
x = "ell" in t
print (x)
print ()


d = 'The python language is introduced in 1989 before Java'
y = "is" not in d
print (y)


# String Concatenation

a = "Hey"
b = "Dhanya"
c = a + " " + b
print ("String Concatenation :", c)

# String Format

age = 36
txt = "My name is Gopi and I am {}"
print (txt.format(age))

# Unlimited number of arguments passing into the Strings

qty = 3
itemno = 12345
price = 50.60
myorder = "I want {} quantities of soap {} for dollars {}"
print (myorder.format(qty, itemno, price))

# Escape character

txt = "Hello, I want \' Anirudh\' to eat his food on time"
print (txt)


# Carriage return

txt = "Hello\rGopi"
print(txt)

# New Line printing

d = "\nHello\nKishore"
print(d)

# Capitalize String  --- Upper case the first letter alone
e = "good morning Chennai. my fate"
print (e.capitalize())

# USing Center method

e = "Banana"
print(e.center(10))

# using find method

txt = "Hello India, Welcome to this FM Radio"
print (txt.find("Well"))

# Join method

x = {"name": "John", "Country" : "Sweden"}
sep = "TEST"
y = sep.join(x)
print(y)


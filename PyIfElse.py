a = 20
b = 30

if a == b :
    print("a and b are equal")
elif b<a :
    print("a is greater")
else:
    print("B is greater")

# Short Hand If else

a = 40
b = 25
print("A") if a<b else print("B")

# Print the while loop

i = 1
while i < 6 :
    print(i)
    i += 1

# Print the while loop using break statement

i = 1
while i < 6:
    print ("I Value :", i)
    if i == 3 :
        break
    i += 1

# Continue statement

i = 1
while i < 7 :
    i += 1
    if i == 3 :
        continue
    print(i)

# Function

def my_func(fname):
    print (fname + " Refeal")

my_func("Gopi")
my_func("Dhanya")
my_func("Ani")

# Default Function

def my_func(country = "Norway"):
    print ("I am from " + country)

my_func("Sweden")
my_func("India")
my_func()
my_func("Brazil")

# One line if statement
print ("-------------")
a = 50
b = 20
print ("Yes") if b>a else print ("No")

# one line statement with 3 conditions
print ("--------------------------")
a = 230
b = 230
print ("A") if a > b else print ("=") if a==b else print ("B")




# Printing the tuple
thistuple = ("Ferrari", "Ford", "Benz", "Kia", "Bucati", "BMW", "Lamborgini", "Maruthi", "Renault", "Volvo")
print(" Print the tuple : ", thistuple)

# Access tuple items
thistuple = ("Ferrari", "Ford", "Benz", "Kia", "Bucati", "BMW", "Lamborgini", "Maruthi", "Renault", "Volvo")
print ("Print the indexed tuple :", thistuple[-2])

# Change the tuples values through converting the tuples into list
thistuple = ("Ferrari", "Ford", "Benz", "Kia", "Bucati", "BMW", "Lamborgini", "Maruthi", "Renault", "Volvo")
y = list(thistuple)
y[4] = "Nissan"
thistuple = tuple(y)

print ("Print the changed tuple values: ", thistuple)

# Loop through the tuple
thistuple = ("Ferrari", "Ford", "Benz", "Kia", "Bucati", "BMW", "Lamborgini", "Maruthi", "Renault", "Volvo")
for x in thistuple:
    print ("Loop through the list :-", x)

# Adding serial numbers to the loop throuigh list

thistuple = ("Ferrari", "Ford", "Benz", "Kia", "Bucati", "BMW", "Lamborgini", "Maruthi", "Renault", "Volvo")
for i in range(len(thistuple)):
    print ("{},{}".format(i+1,thistuple[i]))

# Check if an item exists in the tuple
thistuple = ("Ferrari", "Ford", "Benz", "Kia", "Bucati", "BMW", "Lamborgini", "Maruthi", "Renault", "Volvo")
if "Mahindra" in thistuple:
    print("Yes, this item is available")
else:
    print("No, this item is unavailable")

# Check if an item exists in the tuple through user inputs
thistuple = ("Ferrari", "Ford", "Benz", "Kia", "Bucati", "BMW", "Lamborgini", "Maruthi", "Renault", "Volvo")
inStr = input("Enter the input: ")
if inStr in thistuple:
    print("Yes, this item is available")
else:
    print("No, this item is unavailable")

# Add an item to the tuple
thistuple = ("Ferrari", "Ford", "Benz", "Kia", "Bucati", "BMW", "Lamborgini", "Maruthi", "Renault", "Volvo")
# thistuple[2] = "Toyota"
print(thistuple)








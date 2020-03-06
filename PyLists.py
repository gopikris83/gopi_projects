thislist = ["Ferrari", "Ford", "Benz"]
print(thislist)

# print indexing number values

thislist = ["Ferrari", "Ford", "Benz"]
print(thislist[1])

# print negative indexing number values

thislist = ["Ferrari", "Ford", "Benz"]
print("Negative Index :", thislist[-1])

# print range of indexes

thislist = ["Ferrari", "Ford", "Benz", "Kia", "Bucati", "BMW", "Lamborgini", "Maruthi", "Renault", "Volvo"]
print("Range of Index :", thislist[-4:-1])


# print change the value of the list

thislist = ["Ferrari", "Ford", "Benz", "Kia", "Bucati", "BMW", "Lamborgini", "Maruthi", "Renault", "Volvo"]
thislist [7] = "Rolls Royce"
print("Revised Index :", thislist)

# Loop through the list

thislist = ["Ferrari", "Ford", "Benz", "Kia", "Bucati", "BMW", "Lamborgini", "Maruthi", "Renault", "Volvo"]
for i in range(len(thislist)):
    print("{}. {}".format(i+1, thislist[i]))

# Add items to the list
thislist = ["Ferrari", "Ford", "Benz", "Kia", "Bucati", "BMW", "Lamborgini", "Maruthi", "Renault", "Volvo"]
thislist.append("Rolls Royce")
print("Revised Index after adding item :", thislist)

# Insert an items to the list
thislist = ["Ferrari", "Ford", "Benz", "Kia", "Bucati", "BMW", "Lamborgini", "Maruthi", "Renault", "Volvo"]
thislist.insert(2,"Toyota")
print("Revised Index after Inserting item :", thislist)

# Remove item from the list

thislist = ["Ferrari", "Ford", "Benz", "Kia", "Bucati", "BMW", "Lamborgini", "Maruthi", "Renault", "Volvo"]
thislist.remove("Maruthi")
print("Revised list after removing an item :", thislist)


# Using pop method

thislist = ["Ferrari", "Ford", "Benz", "Kia", "Bucati", "BMW", "Lamborgini", "Maruthi", "Renault", "Volvo"]
thislist.pop(1)
print("Using pop method:", thislist)

# Using del method to delete an item
thislist = ["Ferrari", "Ford", "Benz", "Kia", "Bucati", "BMW", "Lamborgini", "Maruthi", "Renault", "Volvo"]
del thislist[0]  # Must to have an index value
print ("Print the list after calling del method :", thislist)


# Deleting the list
thislist = ["Ferrari", "Ford", "Benz", "Kia", "Bucati", "BMW", "Lamborgini", "Maruthi", "Renault", "Volvo"]
del thislist
# print ("Deleting the list completely :", thislist)

# Clearing the values inside the list
thislist = ["Ferrari", "Ford", "Benz", "Kia", "Bucati", "BMW", "Lamborgini", "Maruthi", "Renault", "Volvo"]
thislist.clear()
print ("Clearing the list value :", thislist)

# Copying the list to another

thislist = ["Ferrari", "Ford", "Benz", "Kia", "Bucati", "BMW", "Lamborgini", "Maruthi", "Renault", "Volvo"]
newlist = thislist.copy()
print ("New List after copying from thislist :", newlist)


# Joining two list

thislist = ["Ferrari", "Ford", "Benz", "Kia", "Bucati", "BMW", "Lamborgini", "Maruthi", "Renault", "Volvo"]
newlist = [1,2,3,4,5,6,7,8,9]

mylist = newlist + thislist
print ("Print the values of two joined list - ", mylist)

# Another way to join two list
thislist = ["Ferrari", "Ford", "Benz", "Kia", "Bucati", "BMW", "Lamborgini", "Maruthi", "Renault", "Volvo"]
newlist = [1,2,3,4,5,6,7,8,9]

for x in newlist:
    thislist.append(x)

print ("Another way of joining the list - ", thislist)

# Using Extend method to add one element to another
thislist = ["Ferrari", "Ford", "Benz", "Kia", "Bucati", "BMW", "Lamborgini", "Maruthi", "Renault", "Volvo"]
newlist = [1,2]

newlist.extend(thislist)
print()
print ("Using Extend Methiod", newlist)

# Print the list in reverse order

thislist = ["Ferrari", "Ford", "Benz", "Kia", "Bucati", "BMW", "Lamborgini", "Maruthi", "Renault", "Volvo"]
thislist.reverse()
print ("Reversed order list : ", thislist)


# Print the sort list

thislist = ["Ferrari", "Ford", "Benz", "Kia", "Bucati", "BMW", "Lamborgini", "Maruthi", "Renault", "Volvo"]
thislist.sort()
print ("Sorted list : ", thislist)

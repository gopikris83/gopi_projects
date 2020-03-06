# Printing the Sets
thisSet = {"Ferrari", "Ford", "Benz", "Kia", "Bucati", "BMW", "Lamborgini", "Maruthi", "Renault", "Volvo"}
print(" Print the Set : ", thisSet)

# Add items to the Set

thisSet = {"Ferrari", "Ford", "Benz", "Kia", "Bucati", "BMW", "Lamborgini", "Maruthi", "Renault", "Volvo"}
thisSet.add("Toyota")
print ("Print the revised Set - ", thisSet)

# Add Multiple items to the Set

thisSet = {"Ferrari", "Ford", "Benz", "Kia", "Bucati", "BMW", "Lamborgini", "Maruthi", "Renault", "Volvo"}
thisSet.update(["Toyato", "Nissan"])
print ("Print the revised set after update - ", thisSet)

# Remove the items from the Set

thisSet = {"Ferrari", "Ford", "Benz", "Kia", "Bucati", "BMW", "Lamborgini", "Maruthi", "Renault", "Volvo"}
thisSet.remove("Maruthi")
print ("Print the set after removing item - ", thisSet)

# Remove the items from the Set using discard()

thisSet = {"Ferrari", "Ford", "Benz", "Kia", "Bucati", "BMW", "Lamborgini", "Maruthi", "Renault", "Volvo", "Volvo"}
thisSet.discard("Nissan") # Discards the value in the set and NOT reurn any error if the value is unavailable
print ("Print the set after discarding item - ", thisSet)

# Join Two sets
thisSet = {"Ferrari", "Ford", "Benz", "Kia", "Bucati", "BMW", "Lamborgini", "Maruthi", "Renault", "Volvo", "Volvo"}
thisSet1 = {"1","2","3","4","5"}

thisSet3 = thisSet.union(thisSet1)
print ("Joined Set :", thisSet3)

# Using update method
thisSet = {"Ferrari", "Ford", "Benz", "Kia", "Bucati", "BMW", "Lamborgini", "Maruthi", "Renault", "Volvo", "Volvo"}
thisSet1 = {"1","2","3","4","5"}

thisSet1.update(thisSet)
print("Using update Method: ", thisSet1)


# Using difference method
thisSet1 = {"Ferrari", "Ford", "Benz", "Kia", "Bucati", "BMW", "Lamborgini", "Maruthi", "Renault", "Volvo", "Volvo"}
thisSet2 = {"1","2","3","Kia","BMW", "Ferrari"}

thisSet3 = thisSet1.difference(thisSet2)
print ("Print the Difference:", thisSet3) # Prints the items that only exist in thisSet1 not in thisSet2


# Using difference update method
thisSet1 = {"Ferrari", "Ford", "Benz", "Kia", "Bucati", "BMW", "Lamborgini", "Maruthi", "Renault", "Volvo", "Volvo"}
thisSet2 = {"1","2","3","Kia","BMW", "Ferrari"}

thisSet1.difference_update(thisSet2)
print ("Print the Difference Update:", thisSet1) # removes the common items from both the sets.

# Using Intersection method - Returns the items that exists in both the sets.
thisSet1 = {"Ferrari", "Ford", "Benz", "Kia", "Bucati", "BMW", "Lamborgini", "Maruthi", "Renault", "Volvo", "Volvo"}
thisSet2 = {"1","2","3","Kia","BMW", "Ferrari"}

thisSet3 = thisSet1.intersection(thisSet2)
print ("Print the Intersection:", thisSet3)


# Using Intersection update - Removes the items that is not present in original sets.
thisSet1 = {"Ferrari", "Ford", "Benz", "Kia", "Bucati", "BMW", "Lamborgini", "Maruthi", "Renault", "Volvo", "Volvo"}
thisSet2 = {"1","2","3","Kia","BMW", "Ferrari"}

thisSet1.intersection_update(thisSet2)
print ("Print the Intersection Update:", thisSet1)

# Using Symmetric Difference - Removes the items that is common to the available sets and returns the set.
thisSet1 = {"Ferrari", "Ford", "Benz", "Kia", "Bucati", "BMW", "Lamborgini", "Maruthi", "Renault", "Volvo", "Volvo"}
thisSet2 = {"1","2","3","Kia","BMW", "Ferrari"}

thisSet3 = thisSet1.symmetric_difference(thisSet2)
print ("Symmetric Difference Set - ", thisSet3)






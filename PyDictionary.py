# Print the dictionary

thisdict = {"brand":"Ford",
            "Model":"Mustang Mach E",
            "Year":2019}

print("The Dictionary :", thisdict)

# Get the value of the Model Key

thisdict = {"brand":"Ford",
            "Model":"Mustang Mach E",
            "Year":2019}
x = thisdict["Model"]
print("Get the Model Key :", thisdict)

# Change the Value

thisdict = {"brand":"Ford",
            "Model":"Mustang Mach E",
            "Year":"2019"}
thisdict["Year"] = 2020
print("Change the Value :", thisdict)

# Loop through the dictionary

thisdict = {"brand":"Ford",
            "Model":"Mustang Mach E",
            "Year":2019}
for i, (key,value) in enumerate(thisdict.items()):
    print(i+1, value)



# Check If items existis in dictionary

thisdict = {"brand":"Ford",
            "Model":"Mustang Mach E",
            "Year":2019
            }

if "Model" in thisdict:
    print ("Yes, this 'model' is the key of the dictionary")

# Adding items to the dictionary

thisdict = {"brand":"Ford",
            "Model":"Mustang Mach E",
            "Year":2019
            }
thisdict["color"] = "Mars Red"
print("Revised Dictionary Value: ", thisdict)

# Removing items to the dictionary

thisdict = {"brand":"Ford",
            "Model":"Mustang Mach E",
            "Year":2019
            }
thisdict.pop("Model")
print("Remove Dictionary Value: ", thisdict)

# Using popitem items to the dictionary

thisdict = {"brand":"Ford",
            "Model":"Mustang Mach E",
            "Year":2019
            }
thisdict.popitem()
print("Print the revised Dictionary Value: ", thisdict)


# Nested Dictionary

myfavcars = {
    "Car1" : {
        "name" : "Ford",
        "year" : 2013
    },
    "Car2" : {
        "name" : "Toyota",
        "year" : 2015
    },
    "Car3" : {
        "name" : "Volvo",
        "year" : 2017
    }
    }
print ("Nested Dictionary :", myfavcars)

# Nested Dictionary - One dict that will contain another dictionary

car1 = {
    "name" : "Ford",
    "year" : 2013
}
car2 = {
    "name" : "Kia",
    "year" : 2015
}
car3 = {
    "name" : "GM",
    "year" : 2016
}

myfavcars = {
    "car1" : car1,
    "car2" : car2,
    "car3" : car3
}
print ("One Dict contains another Dictionary - ", myfavcars)


# Set Default Method

car = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year"  : 2019
}

x = car.setdefault("model","Bronco")
print(x)

# Another example

car = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year"  : 2019
}

x = car.setdefault("colour","Red")
print(x)

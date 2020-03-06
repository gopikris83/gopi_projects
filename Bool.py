print (10>7)
print ( 10==9)
print (10<7)
print (10==10)

# Evaluate values and variables
print("-----------------------")
print (bool("Hello"))
print (bool(15))
print (bool())
print (bool(None))
print (bool(False))


# Objects that are made from class

print ("--------------------------")
class myclass():
    def __len__(self):
        return 0

myobj = myclass()
print (bool(myobj))

# Arithmatic Operators

x = 9
y = 4
z = x // y
print ("Floor division : ", z)

e = 4
e += 7
print(e)


r = 3
r ^= 6
print(r)
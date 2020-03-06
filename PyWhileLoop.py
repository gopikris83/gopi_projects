# Basic while loop

i = 1
while i < 6 :
    print ("I value :", i)
    i += 1


# Exit the loop using break
print ("--------")

i = 1
while i < 6 :
    print (i)
    if i == 3 :
        break
    i += 1


# Using Continue stament

print ("<<<>>>>>")
i = 1
while i < 6 :
    i += 1
    if i == 2 :
        continue
    print ("I Value", i)
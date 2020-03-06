# -------- Defining variables outside of the function (Using global variables) ----------------

x = "Awesome"

def myfunc():
    print (" Python is "+x)

myfunc()

# ---------- Defining variables inside of the function (Using local variables) --------------------------

x = "Awesome"

def myfunc():
    x = "Fantastic"
    print ("Python is "+x)

myfunc()

print ("Python is"+x)

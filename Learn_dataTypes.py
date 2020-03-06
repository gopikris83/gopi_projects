# --- Identifying data types -------------------------

x = bool(-10)
print (type(x))
print(x)

# ---- Printing String data type -------------------

y = "Ford"
print (type(y))

# --- Print Integer data type -----------------------

z = 35
print (type(z))

# --- Print Float data type ---------------------------

a = 21.5
print (type(a))

# ----Print Complex data type -------------------------

c = -0J
print (type(c))
print ("Complex number is: ",c)

# ---Print list data type ------

d = ["Apple", "Orange", "Kiwi"]
print (type(d))
print (d)

# -----Print Tuple data type -------------

e = ("Apple", "Cherry", "Lychee")
print (type(e))
print (e)


# -----Print Range data type ------------

f = range (0,9)
print (type(f))
print (f)

# ---- Print dict data type ----------------

g = {"name": "Ani" , "age" : 6}
print (type(g))
print (g)
print (g['name'])

# ------Print set data type -------------------

x = {"Bus", "Train", "Truck"}
print (type(x))
print (x)

# ------- Print Frozenset data type ------------------

t = frozenset ({"India", "Sweden", "Spain"})
print (type(t))
print (t)

# ----------- Print bytes data types -------------------------

f = b"Hi"
print (type(f))
print (f)


# ----------Print bytearray data type ------------------------

h = bytearray (0)
print (type(h))
print (h)


# ---------- Print memoryview data type ---------------------

r = memoryview (bytes(1))
print (type(r))
print (r)
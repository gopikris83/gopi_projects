# ------ Seed Function inside Random -----------

import random
random.seed(10)

print (random.random())

# ---------------- Capture current state of random number ------------

import random
random.getstate()
print(random.random())
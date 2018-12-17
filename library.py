from random import random, uniform
from datetime import time

rn1 = random()
rn2 = uniform(1, 10)

print(rn1, rn2)

hour = time(int(uniform(0, 24)))

print(hour)


a = [0] * 10

print(iter(a))

import random

def gen():
    while True:
        yield random.randint(1, 100)

for i in gen():
    if i > 90:
        print(i)
        break
    print(i)
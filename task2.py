import random
a = random.randint(4, 10)

b = list(range(a))
max = 0
for i in b:
    b[i] = random.randint(1, 10)
    c = sum(b[i-2:i+1])
    if c > max:
        max = c
    print(b[i-2:i+1])


print(b)
print(max)
import random

a = [random.random() for i in range(5)]
max = 0
i = 0
while(i < 5):
    print a[i]
    if(max < a[i]):
           max = a[i]
    i += 1

print max

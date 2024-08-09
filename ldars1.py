import random
lst1=[]
lst2=[]
for i in range(10):
    lst1.append(random.randint(1, 10))
    lst2.append(random.randint(1, 10))
print(lst1)
print(lst2)
for i in range(len(lst1)):
    if not lst1[i]%2:
        natija=pow(lst1[i], 2)
        lst2.append(natija)
print(lst2)

    
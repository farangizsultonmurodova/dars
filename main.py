import random
import os
#os.system('cls')
lst = list()
toq_lst=[]
juft_lst=[]
for i in range(20):
    lst.append(random.randint(1,100))
for i in range(len(lst)):
    if i%2:
        toq_lst.append(i)
        toq_lst.sort()
    else:
        juft_lst.append(i)
        juft_lst.sort()
print( toq_lst)
print(juft_lst)

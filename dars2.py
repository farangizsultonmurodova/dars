import os
# os. system("cls")
def yigindi(lst:list):
    natija=[]
    for i in range(len(lst)):
        natija.append(sum(lst[i]))
    return natija


print(yigindi([(1,2),(2,3),(3,4)]))    
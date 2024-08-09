import os
os. system("cls")
def func(lst1,lst2,lst3):
	natija={}
	dct=dict(zip(lst2,lst3))
	new_dict = [{i:k} for i,k in dct.items()]
	for i in range(len(lst1)):
		natija[lst1[i]]=new_dict[i]
	return [natija]


print(func(
    ['S001','S002','S003','S004'],
    ['Adina Park','Leyton Marsh','Duncan Boyle','Saim Richards'],
    [85,98,89,92]
))

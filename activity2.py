list1=[1,2,3,4,5,6,7,8]
list2=['a','b','c','d','e','f','g','h']
zilist=zip(list2,list1)
print("list1 is : ",list1)
print("list2 is : ",list2)
print("Zipeed list is : ",list(zilist))
for x,y in zip(list2,list1[::-1]):
    print(x,y)

newdict={x:y for x,y in zip(list2,list1)}
print("Zipped dictionary is : ",newdict)
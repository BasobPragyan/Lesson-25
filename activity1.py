#Write a program to return the addition of numbers of two different lists. Then, display a list that is square of numbers of another list. Use the map() function here to get the desired result.
list1=[1,2,3,4,5,6,7,8]
list2=[9,10,11,12,13,14,15,16]
result=map(lambda x,y:x+y,list1,list2)
print("First list is : ",list1)
print("Second list is : ",list2)
print("Final add on both lists is : ",list(result))
def square(n):
    return n*n
sqlist=map(square,list1)
print("Square list is : ",list(sqlist))
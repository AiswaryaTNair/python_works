

n1=int(input('enter the number'))
list1=[]
for i in range(1,n1+1):
    list1.append(input('enter the list'))

n2=int(input("enter the number"))
list2=[]
for j in range(1,n2+1):
    list2.append(input("enter the list"))
    
dictonary = dict(zip(list1, list2))
print(dictonary)

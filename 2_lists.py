
def odd_even(list1,list2):
    list3=[]

    for number in list1:
        if int(number) % 2 != 0:
             list3.append(number)
             


    for number in list2:
        if int(number) % 2==0:
            list3.append(number)

            
    return list3


n1=int(input("enter the number"))
list1=[]
for i in range(1,n1+1):
    list1.append(input("enter the list"))


n2=int(input("enter the number"))
list2=[]
for j in range(1,n2+1):
    list2.append(input("enter the list"))

    
output=odd_even(list1,list2)
print(output)


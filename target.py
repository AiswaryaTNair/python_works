


def target_index(list,target):
    list1=[]
    for i in range(0,len(list)):
        for j in range(i+1,len(list)):
            #print(list[i],list[j])
            #print(list[i]+list[j])
            #print(target)
            if int(list[i])+int(list[j])==target:
                list1.append(i)
                list1.append(j)

    return list1
        


n=int(input("enter the number"))
list=[]
for i in range(1,n+1):
    list.append(input("enter the list"))

target=int(input("enter the target number"))

print(target_index(list,target))


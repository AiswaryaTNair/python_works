#from stringprep import in_table_c5


def First_Last(list):
    if list[0]==list[-1]:
        return True
    else:
        return False


n=int(input('enter the no'))
list=[]
for i in range(1,n+1):
    list.append(input())
    
#list=[10,12,14,16,15]

output=First_Last(list)
if output==True:
    print("same")
else:
    print("not same")





def find_factorial(n):
    print(n)
    if n==0:
        return 1
    else:
        return n*find_factorial(n-1)


#output=find_factorial(6)
#print(output)
        
    
    
def fact(n):
    result=1
    for i in range(1,n+1):
        result=result*i 
        #print(result)
    return result

print(fact(3))
	

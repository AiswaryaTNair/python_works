def exponent(base,expo):
    if expo==1:
        return(base)
    else:
        return(base**expo)


n=int(input("enter the base value"))
m=int(input("enter the exponent"))
print(exponent(n,m))  

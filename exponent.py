def exponent(base,expo):
    if expo==1:
        return(base)
    else:
        return(base*exponent(base,expo-1))


n=int(input("enter the base value"))
m=int(input("enter the exponent"))
print(exponent(n,m))   

def star(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print("*",end="")
        print()   
           

number=int(input("enter the number"))        
star(number) 
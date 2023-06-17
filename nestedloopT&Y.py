n=int(input("enter"))
i=1
while i<=7:
    b=n
    while b>=i:
        print(" ",end="")
        b=b-1
    j=1
    while j<=i:
        print("*",end=" ")
        j=j+1
    print()
    i=i+2
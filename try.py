n=int(input("enter"))
i=1
while i<=n:
    j=1
    while j<=n:
        if i+j==4 or j-i==2 or i==3:
            print("*",end=" ")
        else:
            print(" ",end=" ")
        j=j+1
    print()
    i=i+1
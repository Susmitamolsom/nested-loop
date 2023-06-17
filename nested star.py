n=int(input("enter"))
i=0
while i<n:
    j=0
    while j<n:
        if i+j==2 or j-i==2 or i-j==2 or i+j==6:
            print("*",end=" ")
        else:
            print(" ",end=" ")
        j=j+1
    print()
    i=i+1
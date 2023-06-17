i=4
while i>=1:
    j=1
    while j<=4:
        if i==4 or j==1 or i==j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
        j=j+1
    print()
    i=i-1
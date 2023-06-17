i=1
while i<=5:
    b=1
    while b<=i:
        if i==1 or b==1 or i==5 or b==5:
            print("*",end=" ")
        else:
            print(" ",end=" ")
        b=b+1
    print()
    i=i+2
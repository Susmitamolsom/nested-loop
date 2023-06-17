i=5
while i>=1:
    b=1
    while b<=5:
        if i==b or i==1 or b==1 or b==5:
            print("*",end=" ")
        else:
            print(" ",end=" ")
        b=b+1
    print()
    i=i-1
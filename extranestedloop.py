i=1
while i<=5:
    b=1
    while b<=5:
        if i==1 or i==5-1*b+4 or i==4 or i==1+b*2 or b==1 or b==5:
            print("*",end=" ")
        else:
            print(" ",end=" ")
        b=b+1
    print()
    i=i+1
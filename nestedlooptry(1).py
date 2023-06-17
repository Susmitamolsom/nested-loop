i=1
while i<=5:
    b=5
    while b>=1:
        if i==b or i==5 or b==1:
            print("*",end=" ") 
        else:
            print(" ",end=" ")
        b=b-1
    print()
    i=i+1
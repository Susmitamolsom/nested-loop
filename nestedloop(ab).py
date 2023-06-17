a=int(input("enter"))
i=1
c=0
while i<=a:
    b=a
    while b>=i:
        print(" ",end="")
        b=b-1
    j=1
    c=c+1
    while j<=i:
        print(c,end=" ")
        j=j+1
    print()
    i=i+2
n=int(input("enter"))
i=1
while i<=n:
    j=1
    while j<=i:
        if i%2!=0:
            print(i,end=" ")
        j=j+2
    print()
    i=i+2
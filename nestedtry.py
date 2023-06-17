i=1
k=65
while i<=5:
    j=5
    a=65
    while j>=i:
        print(" ",end=" ")
        j=j-1
    b=1
    while b<=i:
        print(chr(a),end=" ")
        b=b+1
        a=a+1
    print()
    i=i+1
    k=k+1

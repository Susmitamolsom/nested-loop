# n=int(input("enter no"))
# i=1
# while i<=n:
#     j=1
#     while j<=i:
#         print(j,end=" ")
#         j=j+1
#     print()
#     i=i+1

r=1
while r<=4:
    c=1
    while c<=4-r:
        print(" ",end=" ")
        c=c+1
    j=1
    while j<=r:
        print(j,end=" ")
        j=j+1
    m=r-1
    while m>0:
        print(m,end=" ")
        m=m-1
    print()
    r=r+1

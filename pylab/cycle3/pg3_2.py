n=int(input("enter limit: "))

n1=0
n2=1
next=n1

count=1
print("fibonacci series :")
while count<=n:
        print(next)
        count+=1
        n1,n2=n2,next
        next=n1+n2



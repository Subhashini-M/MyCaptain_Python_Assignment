#1.Fibonacci sequnece

n=int(input("Enter the no.of terms:"))
n1,n2=0,1
c=0
if n<=0:
    print("Enter a positive integer")
elif n==1:
    print("Fibonacci sequence",n,"is")
    print(n1)
else:
    print("Fibonacci sequence:")
    while c<n:
        print(n1)
        n3=n1+n2
        n1=n2
        n2=n3
        c=c+1



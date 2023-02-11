#To print the positive numbers from a list

n=int(input("Enter the number of elements:"))
T=[]
for i in range(n):
    num=input("Enter the number:")
    T.append(num)
print("T=",T)
for j in T:
    if int(j)>0:
        print(j)
print("are the positive numbers")

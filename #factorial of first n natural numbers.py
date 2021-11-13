#factorial of first n natural numbers
n=int(input("enter n="))
f=1
for i in range (1,n+1):
    f=f*i
print("the factorial",f)
#backward difference interpolation
n=7
x=[1991,1993,1995,1997,1999,2001,2003]
def cal_u(u,n):
    temp=u
    for i in range(1,n):
        temp=temp*(u+i)
    return temp
#define y values
y=[[0 for i in range(n)]for j in range (n)]

y[0][0]=10
y[1][0]=21
y[2][0]=33
y[3][0]=45
y[4][0]=51
y[5][0]=60
y[6][0]=73

for i in range(1,n):
    for j in range(i,n):
        y[j][i]=y[j][i-1]-y[j-1][i-1]

#displaying backward difference table 
for i in range(n):
    print(x[i],end="\t")
    for j in range (i+1):
      print(y[i][j],end="\t")
    print(" ")        

v = float(input("put the value of v "))
u=(v-x[n-1])/(x[1]-x[0])
import math

sum=y[n-1][0]
for i in range(1,n):
    sum=sum+((cal_u(u,i))*y[n-1][i])/math.factorial(i)
print(sum)
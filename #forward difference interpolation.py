#backward difference interpolation
n=4
x=[10,20,30,40]
def cal_u(u,n):
    temp=u
    for i in range(1,n):
        temp=temp*(u-i)
    return temp
#define y values
y=[[0 for i in range(n)]for j in range (n)]

y[0][0]=81
y[1][0]=93
y[2][0]=112
y[3][0]=123

for i in range(1,n):
    for j in range(i,n):
        y[j][i]=y[j][i-1]-y[j-1][i-1]
v = float(input("put the value of v "))
u=(v-x[n-1])/(x[1]-x[0])
import math

sum=y[n-1][0]
for i in range(1,n):
    sum=sum+((cal_u(u,i))*y[n-1][i])/math.factorial(i)
    print(sum)
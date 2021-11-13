#lagranges inter polation
n=5
x=[2,3,5,9,12]
y=[4,7,11,19,23]
X=float(input("enter the value of X:"))
def Interpolate(y,X,n):
       result=0
       for i in range(n):
           term=y[i]
           for j in range (n):
              if j!=i:
                term=term*((X-x[j])/(x[i]-x[i]))
            result=result+term
      return result
print("the value of y for ",X, "is",Interpolate(y,X,n))
   




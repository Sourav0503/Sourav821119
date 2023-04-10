def newton(f,df,x,tol):
    if (f(x)<tol):
        return x
    else :
        return newton(f,df,x-f(x)/df(x),tol)
f=lambda x:x**3-x**2-2*x-1
df=lambda x:3*x**2-2*x-2
tol=0.1
y=10
c=newton(f,df,y,tol)
print(c)
        
        
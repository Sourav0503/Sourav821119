def my_saving_plan(p,i,goal):
    c=0
    while (goal>p):
        s=(1+i)*p
        p=s
        c=c+1
        if (s>=goal):
            break
    return c
p=int(input("Enter principal amount = "))
i=float(input("Enter interest = "))
goal=int(input("Enter final ampunt = "))


c=my_saving_plan(p, i, goal)

print("Number of years = ",c)
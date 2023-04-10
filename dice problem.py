for t in range (1,101):
    x = int (input("Enter value of x = "))

    y = int(input("Enter value of y = "))


    if ((x>=1 and x<=6) and (y>=1 and y <=6)):
       if (x+y > 6):
           print("YES")
           
       else :
           print("NO")
       
           
    else :
       print ("invalid input")
    con = input(" Continue ? Y/N = ")
    if (con == "N" or con == "n"):
        break
       
   
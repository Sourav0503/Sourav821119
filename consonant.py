s = (input("Enter a string = "))
l = len(s)
c=0
for i in range(0,l):
    if (s[i] != 'a' and s[i] !='e' and s[i] != 'i' and s[i] != 'o' and s[i] != 'u' ):
        c=c+1
        if (c==4):
            print("NO")
            break
        else :
            continue
    else :
        c=0
if (c<4):
    print("YES")
    
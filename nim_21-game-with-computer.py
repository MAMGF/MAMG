x=21
while x!=1:
    y=int(input("Enter a number :"))
    if y>3 or y<0 :
        print ("Error")
        break
    x=x-y
    if x==1:
        print("computer are loses ")
    if y==1:
        z=3
    elif y==2:
        z=2
    else:
        z=1
    x=x-z
    print(x)
    if x==1:
        print("computer won")
        
        

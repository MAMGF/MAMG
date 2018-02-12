x=21
while x!=1:
    y=int(input("player 1 :"))
    if y>3 or y<0 :
        print("Error")
        break
    else:
        x=x-y
        print(x)
        if x==1:
            print("player 2 loses ")
        else:
            z=int(input("player 2 : "))
            if z>3 or z<0:
                print("Error")
                break
            x=x-z
            print(x)
            if x==1:
                print("player 1 loses")
                break

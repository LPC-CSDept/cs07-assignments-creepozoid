x = int(input("Enter x: "))
y = int(input("Enter y: "))
if  (x == 0 or y == 0):
    print ("Sorry, doesn't belong to any quadrant")
elif x > 0:
        if y > 0:
            print ("Quadrant 1")
        elif y < 0:
                print ("quadrant 4")
elif x < 0:
        if y > 0:
            print ("quadrant 2")
        elif y < 0:
            print ("quadrant 3")

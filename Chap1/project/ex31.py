print ("you enter a dark room with two doors. do you go thorough\
door #1 or door #2?")

door = input(">")

if door =="1":
    print ("there's a giant bear here eating a cheese cake.\
    what do you do ?")
    print ("1.take the cake.")
    print ("2. scream at the bear.")

    bear= input(">")

    if bear =="1":
        print ("the bear  eats your face off. good job! ")
    elif bear=="2":
        print ("the bear eats your legs off. good job!")
    else:
        print("well,doing %s is probably better. bear runs\
        away.") %bear
elif door=="2":
    print("you stare into the endless abyss at cthulu's retina.")
    print("1. blueberries")
    print("2. yellow jacket clothespins")
    print("3. understanding revolvers yelling melodies.")

    insantity = input(">")

    if insantity=="1 " or insantity=="2":
        print( "your body survives powered by a mind of jello\
            good job.")
    else:
        print("the insantity rots your eyes into a pool of muck,\
            good job!")

else:
    print("you stumble around and fall on a knife and die.\
    good job!")

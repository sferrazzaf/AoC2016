directions = 'L1, L3, L5, L3, R1, L4, L5, R1, R3, L5, R1, L3, L2, L3, R2, R2, L3, L3, R1, L2, R1, L3, L2, R4, R2, L5, R4, L5, R4, L2, R3, L2, R4, R1, L5, L4, R1, L2, R3, R1, R2, L4, R1, L2, R3, L2, L3, R5, L192, R4, L5, R4, L1, R4, L4, R2, L5, R45, L2, L5, R4, R5, L3, R5, R77, R2, R5, L5, R1, R4, L4, L4, R2, L4, L1, R191, R1, L1, L2, L2, L4, L3, R1, L3, R1, R5, R3, L1, L4, L2, L3, L1, L1, R5, L4, R1, L3, R1, L2, R1, R4, R5, L4, L2, R4, R5, L1, L2, R3, L4, R2, R2, R3, L2, L3, L5, R3, R1, L4, L3, R4, R2, R2, R2, R1, L4, R4, R1, R2, R1, L2, L2, R4, L1, L2, R3, L3, L5, L4, R4, L3, L1, L5, L3, L5, R5, L5, L4, L2, R1, L2, L4, L2, L4, L1, R4, R4, R5, R1, L4, R2, L4, L2, L4, R2, L4, L1, L2, R1, R4, R3, R2, R2, R5, L1, L2'.replace(" ", "").split(",")

eastwest = 0
northsouth = 0
facing = 90

for direction in directions:
    turn = direction[0]
    distance = int(direction[1:])
    print("{}'s turn is: {}".format(direction, turn))
    print("{}'s distance is: {}".format(direction, distance))
    if turn == "L":
        print("facing = {}".format(facing))
        print("setting facing +90")
        facing += 90
        if facing == 360:
            facing = 0
        if facing == -90:
            facing = 270
    elif turn == "R":
        print(facing)
        print("setting facing -90")
        facing -= 90
        if facing == 360:
            facing = 0
        if facing == -90:
            facing = 270
        print(facing)
    if facing == 0:
        eastwest += distance
    elif facing == 90:
        northsouth += distance
    elif facing == 180:
        eastwest -= distance
    elif facing == 270:
        northsouth -= distance
    print(eastwest)
    print(northsouth)
    
totaldistance = abs(eastwest) + abs(northsouth)
print(totaldistance)

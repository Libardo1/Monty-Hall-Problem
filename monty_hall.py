# Setup the Monty Hall problem to run simulations.

"""
NEEDS:
3 random values, 2 = goat, 1 = car
place values into array

"""
import random
import numpy as np

def monty_hall():

    GOAT = 0
    CAR = 1

    solution1 = 0
    solution2 = 0

    for x in range(10):

        doors = np.array([0,0,0])

        car_location = random.randint(0,2)

        # Place car in a random spot.
        doors[car_location] = CAR

        # Door selection.
        door_selected = random.randint(0,2)

        # SOLUTION 1 - LESS CHANCE
        # Pick a door, and stick to it
        if doors[door_selected] == CAR:
            solution1 += 1


        # SOLUTION 2 - Reveal a door that does not have a goat, pick the OTHER door.

        # Get a door with a goat in it.
        for index, value in enumerate(doors):
            if value != 1 and index != door_selected:
                goat_door = index

        # We now have a door with a goat and the door selected.
        last_door = len(doors) - (goat_door + door_selected)

        #print "door selected: ", door_selected
        #print "car location: ", car_location
        #print "goat location: ", goat_door

        if doors[last_door] == CAR:
            solution2 += 1


    #print "SOLUTION 1: ", solution1
    #print "SOLUTION 2: ", solution2
    if solution1 > solution2:
        return 1
    elif solution1 < solution2:
        return 2
    else:
        return 0

print monty_hall()

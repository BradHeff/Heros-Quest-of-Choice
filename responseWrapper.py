import gameState as state
import responseLeft
import responseRight
import responseForward
import responseFinale


def turn(response):
    # Sends the hero into the scenario of the current stage
    stages = [wrapper, wrapper2, wrapper3, wrapper4, wrapper5]
    stages[state.stage - 1](response)


def wrapper(response):
    # Stage 1 - The Dark Forest
    print("")
    print("- The Dark Forest -")
    print("The castle lies far ahead. The trees swallow the path.")
    if response == "l":
        responseLeft.face_trees()
    elif response == "r":
        responseRight.big_bill()
    else:
        responseForward.wolf_pack()


def wrapper2(response):
    # Stage 2 - The Swamplands
    print("")
    print("- The Swamplands -")
    print("Gray water, black mud, and things that bubble below.")
    if response == "l":
        responseLeft.quicksand()
    elif response == "r":
        responseRight.thief_1()
    else:
        responseForward.ferry_crossing()


def wrapper3(response):
    # Stage 3 - The Thorny Highlands
    print("")
    print("- The Thorny Highlands -")
    print("Cold wind, loose stone, and a gorge that swallows the road.")
    if response == "l":
        responseLeft.dark_cave()
    elif response == "r":
        responseRight.rockslide()
    else:
        responseForward.bridge_troll()


def wrapper4(response):
    # Stage 4 - The Castle Walls
    print("")
    print("- The Castle Walls -")
    print("Torches move along the ramparts. The princess is close.")
    if response == "l":
        responseLeft.moat()
    elif response == "r":
        responseRight.guard_post()
    else:
        responseForward.main_gate()


def wrapper5(response):
    # Stage 5 - The Dragon's Tower
    print("")
    print("- The Dragon's Tower -")
    print("You reach the tower stair. Smoke drifts down from above.")
    print("The princess is up there, and so is the dragon.")
    if response == "l":
        responseFinale.sneak_past()
    elif response == "r":
        responseFinale.charge_dragon()
    else:
        responseFinale.bargain()

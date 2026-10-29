import random
import gameState as state
import battle


def wolf_pack():
    # Stage 1 forward - the wolf in the dusk
    print("The path runs straight through the black trees.")
    print("Yellow eyes circle in the dusk. A lone wolf, bold and hungry, lunges!")
    outcome = battle.fight("The Wolf", 18, 4, 7)
    if outcome == "win":
        print("The wolf was gnawing a traveler's pack.")
        print("Inside: a torch and 5 gold.")
        state.add_item("torch")
        state.add_gold(5)
    elif outcome == "fled":
        print("You scramble onto a rock until the wolf loses interest.")
    if state.hero_alive:
        state.advance_stage()


def ferry_crossing():
    # Stage 2 forward - the river and the old ferryman
    print("A brown river blocks the way, fast and deep.")
    print("An old ferryman dozes on his raft. 'Ten coin a crossing,' he mutters.")
    choice = input("(P)ay, (S)wim : ").strip().lower()
    if choice == "p" and state.pay_gold(10):
        print("He poles you across, steady as stone.")
        print("'Dragons love gold more than maidens,' he says. 'Mark that.'")
    else:
        if choice == "p":
            print("Empty pockets. He shrugs and goes back to sleep.")
        swim_the_river()
    if state.hero_alive:
        state.advance_stage()


def swim_the_river():
    # The wet way across, heavy steel drowns
    if state.is_heavy():
        print("Halfway across, the steel drags you under. The river takes you.")
        state.die()
    else:
        print("The current batters you onto the far bank, coughing.")
        state.damage(10)


def bridge_troll():
    # Stage 3 forward - the toll on the rope bridge
    print("A rope bridge sways over a gorge. A troll squats at its head.")
    print("'Toll,' it rumbles. 'Ten coin. Or we fight.'")
    choice = input("(P)ay, (F)ight : ").strip().lower()
    if choice == "p" and state.pay_gold(10):
        print("The troll gnaws the coins and waves you across.")
    else:
        if choice == "p":
            print("Not enough coin. The troll cracks its knuckles.")
        outcome = battle.fight("The Troll", 30, 7, 10)
        if outcome == "win":
            print("Under the bridge lies the hoard: 25 gold and a red potion.")
            state.add_gold(25)
            state.add_item("potion")
        elif outcome == "fled":
            print("You back away. A mile upstream, a narrow ford saves you.")
    if state.hero_alive:
        state.advance_stage()


def main_gate():
    # Stage 4 forward - the shut gate and the shadowed side door
    print("The main gate stands shut. Torchlight moves on the walls above.")
    print("A small side door hides in the gatehouse shadow.")
    if state.has_item("torch"):
        print("By torchlight you study the lock. A traveler's trick opens it.")
        print("A guard's coat hangs inside - 5 gold in the pocket.")
        state.add_gold(5)
    elif random.random() < 0.5:
        print("You feel along the door in the dark and find the latch by luck.")
    else:
        print("A twig snaps underfoot. A guard descends the stair!")
        outcome = battle.fight("Gate Guard", 20, 6, 9)
        if outcome == "win":
            print("You step over him and through the door.")
        elif outcome == "fled":
            print("You hide in a gutter until he leaves, then slip inside.")
    if state.hero_alive:
        state.advance_stage()

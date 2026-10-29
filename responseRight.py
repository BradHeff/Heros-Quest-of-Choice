import random
import gameState as state
import battle


def big_bill():
    # Stage 1 right - the bandit on the road
    print("A fat bandit blocks the road, gold teeth grinning.")
    print("'Big Bill takes a toll, hero. Your coin, or your blood.'")
    choice = input("(P)ay, (F)ight, (R)un : ").strip().lower()
    if choice == "p":
        if state.pay_gold(10):
            state.add_item("torch")
            print("Bill bites the coin and waves you on.")
            print("He tosses you a torch. 'For the marsh, hero. Ha!'")
        else:
            print("Empty pockets. Bill's grin fades. He draws his blade!")
            bill_fight()
    elif choice == "f":
        bill_fight()
    else:
        print("You run. A thrown knife grazes your shoulder.")
        state.damage(8)
    if state.hero_alive:
        state.advance_stage()


def bill_fight():
    # Fists or steel against Big Bill
    outcome = battle.fight("Big Bill", 25, 5, 8)
    if outcome == "win":
        print("You take his coil of rope and his purse of 15 gold.")
        state.add_item("rope")
        state.add_gold(15)
    elif outcome == "fled":
        print("Bill laughs as you scramble off down the road.")


def thief_1():
    # Stage 2 right - the shadow in the mist
    print("Mist coils over the boardwalk. A shadow flickers - a thief!")
    if state.hero_gold > 0:
        print("His fingers are already in your purse.")
        choice = input("(C)hase, (I)gnore : ").strip().lower()
        if choice == "c":
            if random.random() < 0.5:
                print("You corner him against a sunken wall.")
                print("He throws the purse back, plus a knife jab for your trouble.")
                print("He drops a stolen red potion as he begs off.")
                state.damage(5)
                state.add_item("potion")
            else:
                print("He melts into the mist with every coin you own.")
                state.lose_gold(999)
        else:
            print("You let him vanish with a handful of your coin.")
            state.lose_gold(5)
    else:
        print("He flips your empty purse back with a shrug.")
        print("'Nothing, friend. Mind the tower - old Smokey sleeps light.")
        print("Mind your fires up top.' Then he is gone.")
    if state.hero_alive:
        state.advance_stage()


def rockslide():
    # Stage 3 right - stones from the leaning cliff
    print("The highland path runs beneath a leaning cliff.")
    print("A rumble overhead. Rockslide!")
    choice = input("(D)uck under the overhang, (S)print through : ").strip().lower()
    if choice == "d":
        print("You press into the stone as the world crashes past.")
    elif state.has_item("shield"):
        print("You sprint. A boulder glances off your shield as you dive clear.")
    elif random.random() < 0.5:
        print("You dive clear, heart hammering.")
    else:
        print("A stone the size of a fist finds your skull.")
        state.die()
    if state.hero_alive:
        state.advance_stage()


def guard_post():
    # Stage 4 right - two guards at the postern gate
    print("Two guards hunch over a brazier at the postern gate.")
    choice = input("(B)ribe, (S)neak, (F)ight : ").strip().lower()
    if choice == "b":
        if state.pay_gold(20):
            print("One pockets it. 'Saw nothing,' he says.")
            print("'Princess is in the high tower,' one mutters.")
            print("'Right above old Smokey.'")
        else:
            print("They laugh at your thin purse.")
            choice = input("(S)neak, (F)ight : ").strip().lower()
    if choice == "s":
        if random.random() < 0.5:
            print("You slip past while they argue over dice.")
        else:
            print("A guard spins around, sword drawn!")
            outcome = battle.fight("Gate Guard", 20, 6, 9)
            if outcome == "win":
                print("You step over him and through the gate.")
            elif outcome == "fled":
                print("You hide in a gutter, then slip over a low wall.")
    elif choice == "f":
        outcome = battle.fight("Gate Guard", 20, 6, 9)
        if outcome == "win":
            outcome = battle.fight("Gate Guard", 20, 6, 9)
        if outcome == "win":
            print("You lay them down quiet. Their purse holds 15 gold.")
            state.add_gold(15)
        elif outcome == "fled":
            print("You melt back into the shadows, then over a low wall.")
    if state.hero_alive:
        state.advance_stage()

import gameState as state
import battle


def face_trees():
    # Stage 1 left - the hollow tree in the forest
    print("Gnarled trees lean over the path like old men with secrets.")
    print("One hollow trunk catches your eye. Something glints inside.")
    choice = input("(T)ake it, (L)eave it : ").strip().lower()
    if choice == "t":
        state.add_item("sword")
        print("You pull a rusted sword from the hollow.")
        print("A note on the hilt reads: 'Steel saves you from fangs,")
        print("but the marsh swallows the heavy.'")
    else:
        print("You leave the glint alone. The forest seems to nod.")
    print("The path winds deeper.")
    state.advance_stage()


def quicksand():
    # Stage 2 left - the sucking mire
    print("Your boot sinks. Then your leg. Quicksand!")
    if state.has_item("rope"):
        print("You lash your rope around a gnarled root and haul yourself out.")
        print("Half-buried in the muck lies a battered shield. You dig it free.")
        state.add_item("shield")
    elif state.is_heavy():
        print("The steel drags you down like an anchor.")
        print("The marsh swallows the heavy. You sink.")
        state.die()
    else:
        print("You wrench yourself free by inches, gasping and drained.")
        state.damage(15)
    if state.hero_alive:
        state.advance_stage()


def dark_cave():
    # Stage 3 left - the pitch black shortcut
    print("A cave mouths open in the hillside. A shortcut, if you dare.")
    if state.has_item("torch"):
        print("Your torch pushes back the dark, stone by stone.")
        print("A dead adventurer clutches a chest: a shield and 10 gold.")
        state.add_item("shield")
        state.add_gold(10)
    else:
        print("You crawl forward by feel until a ledge gives way under you.")
        state.damage(20)
        print("You limp out the far side, empty handed.")
    if state.hero_alive:
        state.advance_stage()


def moat():
    # Stage 4 left - the black water below the walls
    print("The moat gleams far below, black and cold.")
    if state.has_item("rope"):
        print("You grapple the rope onto the wall and climb, hand over hand.")
    elif state.is_heavy():
        print("You slip into the water. The steel pulls you straight down.")
        state.die()
    else:
        print("You swim the moat and haul yourself over, teeth chattering.")
        state.damage(15)
    if state.hero_alive:
        state.advance_stage()

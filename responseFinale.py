import gameState as state
import battle


def sneak_past():
    # Final left - quiet steps past the dragon
    print("You creep up the tower steps, one hand on the wall.")
    if state.has_item("torch"):
        print("Your torch smoke curls up the stairwell.")
        print("The dragon's nostrils flare. It is awake - and it strikes first!")
        outcome = battle.fight("The Dragon", 60, 12, 18, can_run=False, enemy_first=True)
        if outcome == "win":
            rescue()
    else:
        print("You move like a shadow. The great bulk above stirs... and settles.")
        print("You slip past the sleeping dragon.")
        rescue()


def charge_dragon():
    # Final right - steel against scale
    print("You draw your weapon and charge up the steps, roaring.")
    outcome = battle.fight("The Dragon", 60, 12, 18, can_run=False)
    if outcome == "win":
        rescue()


def bargain():
    # Final forward - gold instead of blood
    print("You climb the stair with your purse held high.")
    if state.hero_gold >= 25:
        state.lose_gold(25)
        print("The dragon coils down, one eye on the coin.")
        print("'Gold,' it rumbles, 'shines brighter than maidens.'")
        print("It sweeps the coins into its hoard and turns away.")
        rescue()
    else:
        print("The dragon sniffs your thin purse and finds it insulting.")
        print("It rears up, furious!")
        outcome = battle.fight("The Dragon", 60, 15, 22, can_run=False)
        if outcome == "win":
            rescue()


def rescue():
    # The ending every choice was leading to
    print("")
    print("The princess's cell swings open.")
    print("'You came,' she whispers. 'Calculating to the last, my hero.'")
    print("You carry her down the tower and out into the dawn.")
    print("")
    print("============================")
    print("=  THE PRINCESS IS SAVED!  =")
    print("============================")
    bag = ", ".join(state.hero_items) if state.hero_items else "nothing at all"
    print(f"You finished with {state.hero_health} hp, {state.hero_gold} gold")
    print(f"and a bag of: {bag}.")
    state.game_won = True

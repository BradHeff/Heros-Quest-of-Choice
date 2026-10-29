import random
import gameState as state


def hero_roll():
    # Damage the hero deals, fists or steel
    if state.has_item("sword"):
        return random.randint(8, 12)
    return random.randint(3, 6)


def enemy_roll(enemy_min, enemy_max):
    # Damage the enemy deals, a shield softens the blow
    dmg = random.randint(enemy_min, enemy_max)
    if state.has_item("shield"):
        dmg = dmg // 2
        print("Your shield turns most of the blow!")
    return dmg


def fight(enemy_name, enemy_hp, enemy_min, enemy_max, can_run=True, enemy_first=False):
    # Turn based duel, returns win, fled or dead
    hp = enemy_hp
    if enemy_first:
        dmg = enemy_roll(enemy_min, enemy_max)
        state.damage(dmg)
        print(f"{enemy_name} strikes you for {dmg}!")
        if not state.hero_alive:
            return "dead"
    while state.hero_alive and hp > 0:
        print(f"{enemy_name} : {hp}/{enemy_hp} hp")
        choice = input("(A)ttack, (P)otion, (R)un : ").strip().lower()
        if choice == "a":
            dmg = hero_roll()
            hp -= dmg
            print(f"You hit {enemy_name} for {dmg}!")
        elif choice == "p":
            if state.has_item("potion"):
                state.remove_item("potion")
                state.heal(30)
                print("You gulp the red potion. Warmth floods back!")
            else:
                print("You have no potion!")
                continue
        elif choice == "r" and can_run:
            if random.random() < 0.5:
                print("You break away and run!")
                return "fled"
            print("You cannot get away!")
        elif choice == "r":
            print("There is nowhere to run!")
        else:
            print("You hesitate...")
            continue
        if hp <= 0:
            print(f"{enemy_name} falls!")
            return "win"
        dmg = enemy_roll(enemy_min, enemy_max)
        state.damage(dmg)
        print(f"{enemy_name} hits you for {dmg}!")
        if not state.hero_alive:
            return "dead"

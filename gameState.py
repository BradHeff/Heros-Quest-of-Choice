hero_health = 100
hero_gold = 10
hero_items = []
hero_alive = True
game_won = False
stage = 1


def reset():
    # Restores the starting values for a new quest
    global hero_health, hero_gold, hero_items, hero_alive, game_won, stage
    hero_health = 100
    hero_gold = 10
    hero_items = []
    hero_alive = True
    game_won = False
    stage = 1


def add_item(item):
    # Puts an item into the hero's bag
    if item not in hero_items:
        hero_items.append(item)


def has_item(item):
    # Checks the bag for an item
    return item in hero_items


def remove_item(item):
    # Takes an item out of the hero's bag
    if item in hero_items:
        hero_items.remove(item)


def is_heavy():
    # True when the hero carries steel that can drag him down
    return has_item("sword") or has_item("shield")


def add_gold(amount):
    # Drops coin into the hero's purse
    global hero_gold
    hero_gold += amount


def pay_gold(amount):
    # Spends coin only if the purse can cover it
    global hero_gold
    if hero_gold >= amount:
        hero_gold -= amount
        return True
    return False


def lose_gold(amount):
    # Coin slips away, whatever it leaves behind
    global hero_gold
    hero_gold = max(0, hero_gold - amount)


def damage(amount):
    # Hurts the hero, death follows at zero
    global hero_health, hero_alive
    hero_health -= amount
    if hero_health <= 0:
        hero_health = 0
        hero_alive = False


def heal(amount):
    # Mends the hero up to his limit
    global hero_health
    hero_health = min(100, hero_health + amount)


def die():
    # Ends the quest on the spot
    global hero_alive
    hero_alive = False


def advance_stage():
    # Moves the journey one step closer to the castle
    global stage
    stage += 1


def status_line():
    # One glance at everything the hero has left
    bag = ", ".join(hero_items) if hero_items else "empty"
    return f"HP: {hero_health} | Gold: {hero_gold} | Bag: {bag}"

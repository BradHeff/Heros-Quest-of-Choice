import gameState as state
import responseWrapper as wrapper


class Main:
    # Turn loop for the whole quest

    def __init__(this, response):
        super(Main).__init__()
        this.response = response
        this.running = True
        this.start_turn(response)

    def start_turn(this, response):
        # Turns run until the hero dies or the princess is safe
        while this.running:
            turn = response.strip().lower()
            if turn == "l":
                wrapper.turn("l")
            elif turn == "r":
                wrapper.turn("r")
            elif turn == "f":
                wrapper.turn("f")
            else:
                print("Only L, R or F will save her.")
            if not state.hero_alive or state.game_won:
                this.running = False
                break
            print("")
            print(state.status_line())
            response = input("What Direction? L,R,F : ")
        if not state.hero_alive:
            print("")
            print("============================")
            print("=        GAME OVER         =")
            print("============================")


if __name__ == "__main__":
    print("============================")
    print("=  Hero's Quest of Choice  =")
    print("============================")
    print("The princess is held in the castle far away.")
    print("Every turn is a choice, and the wrong one kills.")
    print("Steel saves you from fangs, but the marsh swallows the heavy.")
    print("A torch lights the dark... and wakes sleeping dragons.")
    playing = True
    while playing:
        firstRun = input("What Direction? L,R,F : ")
        Main(firstRun)
        if input("Play again? Y,N : ").strip().lower() == "y":
            state.reset()
        else:
            playing = False

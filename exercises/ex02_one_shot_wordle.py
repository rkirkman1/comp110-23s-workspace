"""One Shot Wordle"""
__author__ ="730401129"

SECRET: str = "python"
guess: str = input("What is your six-letter guess? ")
playing: bool = True
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
guess_index: int = 0
clue: str = ""

while playing:
    if guess == SECRET:
        while guess_index < len(guess):
            if guess[guess_index] == SECRET[guess_index]:
                clue = (clue + GREEN_BOX)
                guess_index += 1
            else:
                clue = (clue + WHITE_BOX)
                guess_index += 1
        print(clue)
        print("Woo! You got it!")
        playing = False
    else:
        if len(guess) != len(SECRET):
            guess: str = input("That was not 6 letters! Try again: ")
        else:
            """clue"""
            while guess_index < len(guess):
                """green box"""
                if guess[guess_index] == SECRET[guess_index]:
                    clue = (clue + GREEN_BOX)
                else:
                    """yellow box"""
                    testing: bool = False
                    yellow_index: int = 0
                    while not testing and yellow_index < len(SECRET):
                        if guess[guess_index] != SECRET[yellow_index]:
                            yellow_index += 1
                        else:
                            clue = (clue + YELLOW_BOX)
                            testing = True
                    """white box"""
                    if not testing:
                        clue = (clue + WHITE_BOX)
                guess_index += 1
        print(clue)
        print("Not quite. Play again soon!")
        exit()
                
                


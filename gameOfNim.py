import random
import sys
import time


def printError():
    sys.stdout.write("\033[F")  # Move cursor up by one line
    sys.stdout.write("\033[K")  # Clear the line
    print("Invalid option", end="", flush=True)
    time.sleep(0.5)
    for i in range(3):
        print("!", end="", flush=True)
        time.sleep(0.5)
    sys.stdout.write("\r")
    sys.stdout.write("\033[K")

def createGame(container):
    numberOfPiles = random.randint(2,5)
    for i in range(numberOfPiles):
        numberOfSticks = 2 * random.randint(0,3) + 1
        container.append(["|" for x in range(numberOfSticks)])

def printGame(container):
    print("Current Game State:")
    for index, pile in enumerate(container):
        print(f"Pile {index + 1}: ", end="")
        for stick in pile:
            print(stick, end="")
        print() 

def vsComputer():
    piles = []
    createGame(piles)
    printGame(piles)

    # Game loop
    playerTurn = 1  # Player 1 starts
    while True:
        if playerTurn == 1:
            print(">>>it's your turn.")
        else:
            print(">>>it's the computer's turn.")
        if gameWon(piles):
            winner = 2 if playerTurn == 1 else 1
            if winner == 1:
                print("Congratulations! you have won!")
            else:
                print("Hard luck! the computer won!")
            break
        else:
            if playerTurn == 1:
                try:
                    pileIndex = int(input("Enter pile number: ")) - 1
                    if pileIndex < 0 or pileIndex >= len(piles):
                        print("Invalid pile number. Please try again.")
                        continue

                    sticksToRemove = int(input("Enter number of sticks to remove: "))
                    if sticksToRemove < 1 or sticksToRemove > len(piles[pileIndex]):
                        print("Invalid number of sticks. Please try again.")
                        continue

                    [piles[pileIndex].pop() for ps in range(sticksToRemove)]
                except ValueError:
                    print("Invalid input. Please enter an integer.")
            else:
                # Computer's turn
                pileIndex, sticksToRemove = findBestMove(piles)
                print("Computer removes", sticksToRemove, "sticks from pile", pileIndex + 1)
                [piles[pileIndex].pop() for cs in range(sticksToRemove)]

        printGame(piles)
        playerTurn = 2 if playerTurn == 1 else 1


def findBestMove(piles):
    # Calculate the nim-sum of the current state
    nimSum = 0
    for pile in piles:
        nimSum ^= len(pile)

    # If the nim-sum is 0, the computer cannot win, so it makes a random move
    if nimSum == 0:
        # Choose a random pile
        pileIndex = random.randint(0, len(piles) - 1)
        # Choose a random number of sticks to remove
        sticksToRemove = random.randint(1, len(piles[pileIndex]))
        return pileIndex, sticksToRemove

    # Find a pile and number of sticks that makes the nim-sum become 0
    for i in range(len(piles)):
        xorValue = nimSum ^ len(piles[i])
        if xorValue < len(piles[i]):
            return i, len(piles[i]) - xorValue

    # If no such move exists, make a random move from a non-empty pile
    nonEmptyPiles = [i for i in range(len(piles)) if len(piles[i]) > 0]
    pileIndex = random.choice(nonEmptyPiles)
    sticksToRemove = random.randint(1, len(piles[pileIndex]))
    return pileIndex, sticksToRemove

    
def vsplayer():
    piles = []
    createGame(piles)
    printGame(piles)

    # Game loop
    playerTurn = 1  # Player 1 starts
    while True:
        print(">>>player",playerTurn,"turn")
        if gameWon(piles):
            winner = 2 if playerTurn == 1 else 1
            print("Congratulations!player",winner,"you have won!")
            break
        else: 
            try:
                pileIndex = int(input("Enter pile number: ")) - 1
                if pileIndex < 0 or pileIndex >= len(piles):
                    print("Invalid pile number. Please try again.")
                    continue

                sticksToRemove = int(input("Enter number of sticks to remove: "))
                if sticksToRemove < 1 or sticksToRemove > len(piles[pileIndex]):
                    print("Invalid number of sticks. Please try again.")
                    continue

                [piles[pileIndex].pop() for x in range(sticksToRemove)]
            except ValueError:
                print("Invalid input. Please enter an integer.")
        printGame(piles)
        playerTurn = 2 if playerTurn == 1 else 1
    

def gameWon(piles):
    """
    Checks if the game is won.
    """
    return sum(len(pile) for pile in piles)==0


def gameOfNim():
    print("""
░██████╗░░█████╗░███╗░░░███╗███████╗  ░█████╗░███████╗  ███╗░░██╗██╗███╗░░░███╗
██╔════╝░██╔══██╗████╗░████║██╔════╝  ██╔══██╗██╔════╝  ████╗░██║██║████╗░████║
██║░░██╗░███████║██╔████╔██║█████╗░░  ██║░░██║█████╗░░  ██╔██╗██║██║██╔████╔██║
██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░  ██║░░██║██╔══╝░░  ██║╚████║██║██║╚██╔╝██║
╚██████╔╝██║░░██║██║░╚═╝░██║███████╗  ╚█████╔╝██║░░░░░  ██║░╚███║██║██║░╚═╝░██║
░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝  ░╚════╝░╚═╝░░░░░  ╚═╝░░╚══╝╚═╝╚═╝░░░░░╚═╝ \n\n1) VS Computer \n2) VS Player \n3) Exit""")
    userchoice = input("Enter an option> ")
    while userchoice not in ["1","2","3"]:
        printError()
        userchoice = input("Enter a valid option> ")
        
    if userchoice == "1":
        vsComputer()
    elif userchoice == "2":
        vsplayer()
    else:
        return 


    
    
#----------------------------Main-Program-----------------------------
gameOfNim()
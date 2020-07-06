import zombiedice, random

class StopsAfterTwoBrains:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.

        diceRollResults = zombiedice.roll() # first roll
        # roll() returns a dictionary with keys 'brains', 'shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color, icon) tuples with the
        # exact roll result information.
        # Example of a roll() return value:
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
        #  'rolls': [('yellow', 'brains'), ('red', 'footsteps'),
        #            ('green', 'shotgun')]}

        # Stops rolling after it has rolled 2 brains. 
        brains = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']

            if brains < 2:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break

class RandomAfterFirstRoll:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        zombiedice.roll()

        # After the first roll, randomly decides if it will 
        # continue or stop
        move = random.randint(0, 1)
        while move == 1:
            zombiedice.roll()
            move = random.randint(0, 1)

class StopsAfterTwoShotguns:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()

        # Stops after two shotgun rolls
        shotgun = 0
        while diceRollResults is not None:
            shotgun += diceRollResults['shotgun']

            if shotgun < 2:
                diceRollResults = zombiedice.roll()
            else:
                break

class RandomOneOrFourOrTwoShotguns:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        # Decides randomly to roll between 1 to 4 times
        move = random.randint(1, 4)
        diceRollResults = zombiedice.roll() # Will roll at least one time
        roll_count = 1

        # Stops rolling early if it rolls two shotguns on one roll
        # Stops if we get 3 shotguns
        while roll_count < move and diceRollResults is not None:
            shotgun = diceRollResults['shotgun']
            if shotgun < 2:
                diceRollResults = zombiedice.roll()
            else:
                break
            
class StopsAtMoreShotgunsThanBrains:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll() # First roll
        
        # Stops when roll more shotguns than brains on roll
        brains = 0
        shotgun = 0
        while diceRollResults is not None:
            brains = diceRollResults['brains']
            shotgun = diceRollResults['shotgun']

            if shotgun <= brains:
                diceRollResults = zombiedice.roll()
            else:
                break
        
zombies = (
    zombiedice.examples.RandomCoinFlipZombie(name='Random'),
    zombiedice.examples.RollsUntilInTheLeadZombie(name='Until Leading'),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 2 Shotguns', minShotguns=2),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 1 Shotgun', minShotguns=1),
    StopsAfterTwoBrains(name='Stops at 2 Brains'),
    RandomAfterFirstRoll(name='Random After First'),
    StopsAfterTwoShotguns(name='Stops at 2 Shotguns'),
    RandomOneOrFourOrTwoShotguns(name='Random or 2 Shotguns'),
    StopsAtMoreShotgunsThanBrains(name='More Shots Than Brain'),
    # Add any other zombie players here.
)

# Uncomment one of the following lines to run in CLI or Web GUI mode:
#zombiedice.runTournament(zombies=zombies, numGames=1000)
zombiedice.runWebGui(zombies=zombies, numGames=1000)

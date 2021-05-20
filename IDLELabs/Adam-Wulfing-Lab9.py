import numpy as np
import random

# -------------------------------------------------
# CSCI 127, Lab 9
# June 18, 2020
# Adam Wulfing
# -------------------------------------------------

class Die:

    def __init__(self, sides):
        """A constructor method to create a die"""
        self.sides = sides

    def roll(self):
        """A general method to roll the die"""
        return random.randint(1, self.sides)

# -------------------------------------------------

class Yahtzee:

    def __init__(self, sides):
        """A constructor method that can record 5 dice rolls"""
        self.rolls = np.zeros(5, dtype=np.int16)
        self.sides = sides

    def roll_dice(self):
        """A general method that rolls 5 dice"""
        for i in range(len(self.rolls)):
            self.rolls[i] = Die(self.sides).roll()

    def count_outcomes(self):
        """A helper method that determines how many 1s, 2s, etc. were rolled"""
        counts = np.zeros(self.sides + 1, dtype=np.int16)
        for roll in self.rolls:
            counts[roll] += 1
        return counts

# -------------------------------------------------
# do not change anything above this line
# your methods here

    def is_it_high_roll(self):
        self.rolls.sort()
        x = min(self.rolls)
        if x >= 5:
            return True
        else:
            return False
    
    def is_it_three_of_a_kind(self):
        self.rolls.sort()
        x = 0
        y = 0
        if self.rolls[0] == self.rolls[2]:
            if self.rolls[0] != self.rolls[3]:
                return True
        if self.rolls[2] == self.rolls[4]:
            if self.rolls[1] != self.rolls[4]:
                return True
        if self.rolls[1] == self.rolls[3]:
            if self.rolls[0] != self.rolls[3]:
                if self.rolls[4] != self.rolls[3]:
                    return True
        else:
            return False

    def is_it_large_straight(self):
        self.rolls.sort()
        x = 0
        if self.rolls[4] == 5:
            if self.rolls[3] == 4:
                if self.rolls[2] == 3:
                    if self.rolls[1] == 2:
                        if self.rolls[0] == 1:
                            return True
                        else:
                            return False
                    else:
                        return False  
                else:
                    return False
            else:
                return False
            
        elif self.rolls[4] == 6:
            if self.rolls[3] == 5:
                if self.rolls[2] == 4:
                    if self.rolls[1] == 3:
                        if self.rolls[0] == 2:
                            return True
                        else:
                            return False
                    else:
                        return False  
                else:
                    return False
            else:
                return False
        else:
            return False
            

# do not change anything below this line
# -------------------------------------------------

def main(how_many):


    high_rolls = 0
    three_of_a_kinds = 0
    large_straights = 0
    game = Yahtzee(6)       # 6-sided dice

    for i in range(how_many):
        game.roll_dice()
        if game.is_it_high_roll():
            high_rolls += 1
        elif game.is_it_three_of_a_kind():
            three_of_a_kinds += 1
        elif game.is_it_large_straight():
            large_straights += 1

    print("Number of Rolls:", how_many)
    print("---------------------")
    print("Number of High Rolls:", high_rolls)
    print("Percent:", "{:.2f}%\n".format(high_rolls * 100 / how_many))
    print("Number of Three of a Kinds:", three_of_a_kinds)
    print("Percent:", "{:.2f}%\n".format(three_of_a_kinds * 100 / how_many))
    print("Number of Large Straights:", large_straights)
    print("Percent:", "{:.2f}%".format(large_straights * 100 / how_many))

# -------------------------------------------------
#change back to 2000 when turn in
main(20000)

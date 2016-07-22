"""


Created on Wed Jul 13 13:38:18 2016

"""
from random import randint

class Pokemon:
    # pokemon traits are determined in a constructor
    def __init__(self, oriname, oriType, orihp, orimoves):
        self.name = oriname
        self.type = oriType
        self.hp = orihp
        self.cp = randint(1, 600)
        self.moves = orimoves
        
    #fight
    def battle(self, my_move, opponent, their_move):
        #make my  move and announce it
        print(self.name + " used " + my_move + " !!!")
        #opponent health = my move- their health
        opponent.hp -= (self.moves[my_move] * self.cp)
        print(opponent.name + " has " + str(opponent.hp) + " HP left")
        #check if theyre alive
        if opponent.hp  <= 0:
            print(opponent.name + " is DEAD")
            print("You Win!!!")
            return
        #make their move
        print(opponent.name + " used " + their_move + " !!!")
        self.hp -(opponent.moves[their_move] * opponent.cp)
        if self.hp <= 0:
            print(self.name + "DIED")
            print(opponent.name + " Wins!")
            return
           

eeve_moves = {"Swift":10, "Dig":20}
vee = Pokemon('Eevee', "normal", 'Dig', 90)

squirtle_moves = {"Squirt":40, "Water Gun":100}
squats = Pokemon('Squirtle', "Water", 90)

vee.battle("Dig", squats, "Squirt", vee)
print("Vee Cp: " + str(vee.cp))
print("Squirt Cp: " + str(squats.cp))

        
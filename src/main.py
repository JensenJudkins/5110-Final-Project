#Game tracked by a pandas dataframe
#Game is played my multiple players which are rows in the dataframe
#Each 'good guy' has a column for bank money, defense level, strategy assigned, what action they last took, number of times they have been attacked
#Each 'bad guy' has a column for bank money, attack level, strategy assigned

import pandas as pd
import numpy as np

import Strategy

from helpers import consult_strategy
from Good_Guy import Good_Guy
from Bad_Guy import Bad_Guy
      
def create_game(num_players):
    list_of_good_guys = []

    #Create good guys
    for i in range(num_players):
        gg = Good_Guy(i, 0, 0)
        gg.update_strat("1-2-1")
        gg.update_last_action("defense")
        gg.increase_attack_count()
        gg.increase_attack_count()

        #Print the good guy
        #print(gg.gg_id)
        
        list_of_good_guys.append(gg)
        

    return list_of_good_guys



def create_bad_guy():
    bg = Bad_Guy(0, 0, 0)
    return bg


#good guys consult their strategy to determine their action
def consult_strategy_gg(good_guy):
    
    #Will consult other file to determine action
    consult_strategy.ConsultStrategy.consult_strategy(good_guy)

    #Print the good guy and their strategy
    # print(good_guy.gg_id)
    # print(good_guy.strat)

    return 0

def consult_strategy_bg(bad_guy, strategy, attack, last_move):
    #Will consult other file to determine action
    #lowest hanging fruit always - picks lowest defense every time
    #Using the function "mathmatically" the best option - payoff = ggbank *.2 * (1 + (defense - attack))
    #Incognito attack - where bg attacks every 3 turn
    return 0

#good guys take their action and update their stats
def take_action_gg(player, action, turn):
    #update the dataframe for all attributes except for turn
    return 0

#bad guy takes their action and updates their stats along with the good guys
def take_action_bg(bad_guy, action, turn):
    #Will consult other file to determine action
    return 0

#Prints the game state for tracking
def print_game_state(good_guys, bad_guys):
    print("Good Guys")
    for gg in good_guys:
        print("Good guy ID:" + str(gg.gg_id))
        print("Bank:" + str(gg.bank))
        print("Defense Level:" + str(gg.def_lvl))
        print("Strategy:" + str(gg.strat))
        print("Last Action:" + str(gg.last_action))
        print("Attack Count:" + str(gg.attack_count))
        print("\n")

    print("Bad Guy")
    print("Bad guy ID:" + str(bad_guys.bg_id))
    print("Bank:" + str(bad_guys.bank))
    print("Attack Level:" + str(bad_guys.att_lvl))
    print("Last Action:" + str(bad_guys.last_action))
    print("\n")

    return 0



#Main function to run the game
def main():
    good_guys = create_game(5)
    bad_guys = create_bad_guy()

    for good_guy in good_guys:
        consult_strategy_gg(good_guy)
    print_game_state(good_guys, bad_guys)

main()


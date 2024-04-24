#MAIN FILE TO RUN THE GAME

import pandas as pd
import numpy as np
from helpers import consult_strategy
from Good_Guy import Good_Guy
from Bad_Guy import Bad_Guy

def create_game(num_players):
    list_of_good_guys = []
    #Create good guys
    for i in range(num_players):
        gg = Good_Guy(i, 0, 0)
        list_of_good_guys.append(gg)
    return list_of_good_guys



def create_bad_guy(num_bad):
    list_of_bad_guys = []
    #Create bad guys
    for i in range(num_bad):
        bg = Bad_Guy(i, 0, 0)
        list_of_bad_guys.append(bg)
    return list_of_bad_guys



def get_strategy_gg(good_guy):
    #This will assign each good guy a strategy
    consult_strategy.ConsultStrategy.consult_strategy(good_guy)
    return 0

def use_strategy_gg(good_guy):
    #This will use the strategy assigned to the good guy
    consult_strategy.ConsultStrategy.use_strategy(good_guy)
    return 0

def get_strategy_bg(bad_guy):
    #Will consult other file to get strategy assignment
    consult_strategy.ConsultStrategy.bad_guy_consult_strategy(bad_guy)
    return 0

def use_strategy_bg(bad_guy, good_guys, verbose):
    lowest_defenses = []
    for good_guy in good_guys:
        if good_guy.def_lvl == min([gg.def_lvl for gg in good_guys]):
            lowest_defenses.append(good_guy)
        # Reset all good guys to not being attacked last round
        good_guy.update_attacked_last_round(False)

    #THIS IS THE TARGET GOOD GUY
    good_guy = max(lowest_defenses, key=lambda x: x.bank)
    #print the action took by the bad guy
    if verbose:
        print("Bad guy: " + str(bad_guy.bg_id))
        print("Attacking target good guy: " + str(good_guy.gg_id))
        print("Turn: " + str(bad_guy.num_moves))
        print("Good guy def: " + str(good_guy.def_lvl))
        print("Good guy bank: " + str(good_guy.bank))
        print("Good guy strat: " + str(good_guy.strat))
        print("Bad guy att: " + str(bad_guy.att_lvl))
        print("Bad guy bank: " + str(bad_guy.bank))
        print("Bad guy strat: " + str(bad_guy.strat))
        print("Payout of this attack (no def upgrade): " + str(float(good_guy.bank) * (.2 + .1 * (float(bad_guy.att_lvl)-float(good_guy.def_lvl)))))
        print("\n")


    bad_guy.num_moves += 1
    #Will consult other file to determine action
    consult_strategy.ConsultStrategy.bad_guy_use_strategy(bad_guy, good_guy)
    return 0



#Prints the game state for tracking
def print_game_state(good_guys, bad_guys):
    print("------------Good Guys---------------")
    for gg in good_guys:
        print("Good guy ID:" + str(gg.gg_id))
        print("Bank:" + str(gg.bank))
        print("Defense Level:" + str(gg.def_lvl))
        print("Strategy:" + str(gg.strat))
        print("Last Action:" + str(gg.last_action))
        print("Attack Count:" + str(gg.attack_count))
        print("\n")

    print("--------------Bad Guys-----------------")
    for bg in bad_guys:
        print("Bad guy ID:" + str(bg.bg_id))
        print("Bank:" + str(bg.bank))
        print("Attack Level:" + str(bg.att_lvl))
        print("Strategy:" + str(bg.strat))
        print("Last Action:" + str(bg.last_action))
        print("\n")

    return 0


#Main function to run the game
def main():
    good_guys = create_game(2)
    bad_guys = create_bad_guy(1)
    verbose = True

    print("-------------------------------------------------------Start of game-----------------------------------------------------------------")
    print("\n")

    for good_guy in good_guys:
        get_strategy_gg(good_guy)

    for bad_guy in bad_guys:
        get_strategy_bg(bad_guy)
    
    print_game_state(good_guys, bad_guys)

    turns = 3
    for turn in range(turns):
        print("---------------------------------Turn " + str(turn) + "---------------------------------")
        for good_guy in good_guys:
            use_strategy_gg(good_guy)

        for bad_guy in bad_guys:
            use_strategy_bg(bad_guy, good_guys, verbose)


    print("------------------------------------------------------------------------End of game--------------------------------------------------------\n")
    print_game_state(good_guys, bad_guys)

main()



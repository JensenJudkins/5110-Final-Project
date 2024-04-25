#MAIN FILE TO RUN THE GAME
from multiprocessing.pool import ThreadPool
from helpers import consult_strategy
from Good_Guy import Good_Guy
from Bad_Guy import Bad_Guy
import sys

#Multithread imports
import threading
from multiprocessing import Process
from multiprocessing import Pool


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

def use_strategy_gg(good_guy,verbose, good_guys):
    #This will use the strategy assigned to the good guy
    consult_strategy.ConsultStrategy.use_strategy(good_guy,verbose, good_guys)
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
    bad_guy.num_moves += 1
    #Will consult other file to determine action
    consult_strategy.ConsultStrategy.bad_guy_use_strategy(bad_guy, good_guy, verbose, good_guys)
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


def save_results(good_guys, bad_guys):
    #Save good guy results to a csv file
    with open("good_guy_results.csv", "w") as file:
        file.write("Good Guy ID,Bank,Defense Level,Strategy,Last Action,Attack Count,Turns\n")
        for gg in good_guys:
            file.write(str(gg.gg_id) + "," + str(gg.bank) + "," + str(gg.def_lvl) + "," + str(gg.strat) + "," + str(gg.last_action) + "," + str(gg.attack_count) + "," + str(gg.num_moves) + "\n")

    #Save bad guy results to a csv file
    with open("bad_guy_results.csv", "w") as file:
        file.write("Bad Guy ID,Bank,Attack Level,Strategy,Last Action,Steals,Turns\n")
        for bg in bad_guys:
            file.write(str(bg.bg_id) + "," + str(bg.bank) + "," + str(bg.att_lvl) + "," + str(bg.strat) + "," + str(bg.last_action) + "," + str(bg.num_steals) + "," + str(bg.num_moves) + "\n")

    return 0


#Main function to run the game
def main(gg_count, bg_count,turn_count, verbose):
    good_guys = create_game(gg_count)
    bad_guys = create_bad_guy(bg_count)
    
    print("-------------------------------------------------------Start of game-----------------------------------------------------------------")
    print("\n")

    for good_guy in good_guys:
        get_strategy_gg(good_guy)

    for bad_guy in bad_guys:
        get_strategy_bg(bad_guy)
    
    print_game_state(good_guys, bad_guys)

    turns = turn_count
    pool = ThreadPool()
    for turn in range(turns):
        print("---------------------------------Turn " + str(turn) + "---------------------------------")
        # list_of_arguments = []
        # for good_guy in good_guys:
        #     list_of_arguments.append((good_guy, verbose, good_guys))
        # #Lets multithread this loop
        # with ThreadPool() as pool:
        #     pool.map(use_strategy_gg, list_of_arguments)
        #     pool.map(use_strategy_bg, [(bad_guy, good_guys, verbose) for bad_guy in bad_guys])

        #Single threaded original
        for good_guy in good_guys:
            use_strategy_gg(good_guy, verbose, good_guys)
        for bad_guy in bad_guys:
            use_strategy_bg(bad_guy, good_guys, verbose)

            

    #Close pool
    pool.close()

    print("\n")
    print("------------------------------------------------------------------------End of game--------------------------------------------------------\n")
    print_game_state(good_guys, bad_guys)
    save_results(good_guys, bad_guys)





#Make sure arguments are valid and catch exceptions
try:
    int(sys.argv[1])
    int(sys.argv[2])
    int(sys.argv[3])
except:
    print("Invalid arguments")
    print("Usage: python3 main.py [number of good guys] [number of bad guys] [number of turns] [verbose]")
    print("Example: python3 main.py 2 1 5 False")
    print("Example: python3 main.py 2 1 5 True")
    exit(0)




#Sets verbose default to false and will only work if there is a 4th argument provided and it must be 'True'
verbose = False
if len(sys.argv) >= 5:
    if sys.argv[4] == "True":
        verbose = True
    else:
        verbose = False
        
#Run the game
main(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), verbose)


    






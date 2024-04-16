

#Make strategies for the game, first is 1-2-1, 1 defense, 2 money, 1 defense


import pandas as pd
import numpy as np
import Good_Guy
import Bad_Guy
import Actions


def strat_1_2_1(gg):
    if gg.turn % 4 == 0 or gg.turn % 4 == 3:
        Actions.gg_choose_defense(gg)
    else:
        Actions.gg_choose_money(gg)


def find_next_move_gg(player, strategy, defense, action_last_took, been_attacked, turn):
    print("FInd next move")
    if strategy == "1-2-1":
        return strat_1_2_1(player, defense, action_last_took, been_attacked, turn)
    else:
        return 0
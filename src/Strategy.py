

#Make strategies for the game, first is 1-2-1, 1 defense, 2 money, 1 defense


import pandas as pd
import numpy as np
import Good_Guy
import Bad_Guy
import Actions


def modify_stats_gg(gg, add_def, add_money):
    #Modify pd to add defense and money
    gg['defense'] += add_def
    gg['bank'] += add_money
    return gg



def strat_1_2_1(gg):
    print(gg)
    pd = gg
    #If the good guy has 0 defense in the column 'defense', add 1 defense
    if pd['defense'] == 0:
        pd = modify_stats_gg(pd, 1, 0)

    return pd

def strat_2_1_1(gg):
    return

def strat_1_1_2(gg):
    return 



def find_next_move_gg(good_guys_df):
    for index, row in good_guys_df.iterrows():
        if row['strategy'] == '1-2-1':
            #Send entire row to the strategy
            temp_pd = pd.DataFrame(row).T
            new_row = strat_1_2_1(temp_pd)
            good_guys_df.loc[index] = new_row
        elif row['strategy'] == '2-1-1':
            temp_pd = pd.DataFrame(row).T
            strat_2_1_1(temp_pd)
        elif row['strategy'] == '1-1-2':
            temp_pd = pd.DataFrame(row).T
            strat_1_1_2(temp_pd)
        else:
            print("Strategy not found")
            return
#Game tracked by a pandas dataframe
#Game is played my multiple players which are rows in the dataframe
#Each 'good guy' has a column for bank money, defense level, strategy assigned, what action they last took, number of times they have been attacked
#Each 'bad guy' has a column for bank money, attack level, strategy assigned

import pandas as pd
import numpy as np

#Create a dataframe to track the game
#Dataframe example:
#   bank  defense  strategy  action_last_took  been_attacked   turn  
#0     0        0         0                 0              0      0            
#1     0        0         0                 0              0      0            
#2     0        0         0                 0              0      0            
#3     0        0         0                 0              0      0            
#4     0        0         0                 0              0      0           
def create_game(num_players, num_rounds):
    #Create the columns for the dataframe
    columns = ['bank', 'defense', 'strategy', 'action_last_took', 'been_attacked', 'turn']
    
    
    #Create the dataframe
    good_guys_df = pd.DataFrame(np.zeros((num_players, num_rounds + 5)), columns=columns)
    
    return good_guys_df


#Create a dataframe for the bad guy
#Dataframe example:
#   bank  last_move  strategy
#0     0          0         0
def create_bad_guy():
    #Create the columns for the dataframe
    columns = ['bank', 'attack', 'strategy']
    
    #Create the dataframe
    bad_guys_df = pd.DataFrame(np.zeros((1, 3)), columns=columns)
    
    return bad_guys_df


#good guys consult their strategy to determine their action
def consult_strategy_gg(player, strategy, defense, action_last_took, been_attacked, turn):
    #Will consult other file to determine action
    return 0

def consult_strategy_bg(bad_guy, strategy, attack, last_move):
    #Will consult other file to determine action
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
def print_game_state(good_guys_df, bad_guys_df):
    print(good_guys_df)
    print(bad_guys_df)




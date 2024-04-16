#Game tracked by a pandas dataframe
#Game is played my multiple players which are rows in the dataframe
#Each 'good guy' has a column for bank money, defense level, strategy assigned, what action they last took, number of times they have been attacked
#Each 'bad guy' has a column for bank money, attack level, strategy assigned

import pandas as pd
import numpy as np

import Strategy

#Create a dataframe to track the game
#Dataframe example:
#   bank  defense  strategy  action_last_took  been_attacked   turn  
#0     0        0         0                 0              0      0            
#1     0        0         0                 0              0      0            
#2     0        0         0                 0              0      0            
#3     0        0         0                 0              0      0            
#4     0        0         0                 0              0      0           
def create_game(num_players):
    #Create the columns for the dataframe
    columns = ['bank', 'defense', 'strategy', 'action_last_took', 'been_attacked', 'turn']
    
    
    #Create the dataframe using the columns and each row is a player
    good_guys_df = pd.DataFrame(np.zeros((num_players, 6)), columns=columns)
    
    #Change all columns to integers
    good_guys_df = good_guys_df.astype(int)
    

    #Change strategy column to a string
    good_guys_df['strategy'] = good_guys_df['strategy'].astype(str)

    #Assign '1-2-1' strategy
    good_guys_df.loc[0, 'strategy'] = '1-2-1'
    good_guys_df.loc[1, 'strategy'] = '1-2-1'
    good_guys_df.loc[2, 'strategy'] = '1-2-1'
    good_guys_df.loc[3, 'strategy'] = '1-2-1'
    good_guys_df.loc[4, 'strategy'] = '1-2-1'


    return good_guys_df


#Create a dataframe for the bad guy
#Dataframe example:
#   bank  last_move  strategy   turn
#0     0          0         0    0
def create_bad_guy():
    #Create the columns for the dataframe
    columns = ['bank', 'attack', 'strategy', 'turn']
    
    #Create the dataframe
    bad_guys_df = pd.DataFrame(np.zeros((1, 4)), columns=columns)
    
    #Change strategy column to a string
    bad_guys_df['strategy'] = bad_guys_df['strategy'].astype(str)

    #Assign '1-2-1' strategy


    return bad_guys_df


#good guys consult their strategy to determine their action
def consult_strategy_gg(good_guy_df):
    Strategy.find_next_move_gg(good_guy_df)
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
def print_game_state(good_guys_df, bad_guys_df):
    print(good_guys_df)
    print(bad_guys_df)



#Main function to run the game
def main():
    good_guys_df = create_game(5)

    print(good_guys_df.head())

    bad_guys_df = create_bad_guy()

    consult_strategy_gg(good_guys_df)

main()


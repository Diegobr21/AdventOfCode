#advent of code day 2
#Rock-Paper-Scissors strategy guide

import pandas as pd

#? Outcome values dictionaries
rock_paper_scissor = {'A':'rock', 'B':'paper', 'C':'scissors', 'X':'rock', 'Y':'paper', 'Z':'scissors'}
rock_paper_scissor_inv = {'rock':'X', 'paper':'Y', 'scissors':'Z'}

rps_result = {'rock':1, 'paper':2, 'scissors':3} #for round value calculation
desired_outcomes = {'X':'loose', 'Y':'draw', 'Z':'win'} #2nd part input values

#dicitonaries to map which selections beats the other
win_selection = {'rock':'paper', 'paper':'scissors', 'scissors':'rock'}
loose_selection = {'rock':'scissors', 'paper':'rock', 'scissors':'paper'}

#round values ----- > loose:0, draw:3, win:6 + rock/paper/scissors value

def play_result(opponent_play:str, my_play:str):
    plays = [opponent_play, my_play]
    if(opponent_play == my_play):
        return 3 + (rps_result[my_play])
    
    #rock > scissors
    elif('rock' in plays and 'scissors' in plays):
        if(opponent_play == 'rock'):
            #Lost
            return 0 + rps_result[my_play]
        else:
            #Won
            return 6 + rps_result[my_play]

    #scissors > paper
    elif('scissors' in plays and 'paper' in plays):
        if(opponent_play == 'scissors'):
            #Lost
            return 0 + rps_result[my_play]
        else:
            #Won
            return 6 + rps_result[my_play]

    #paper > rock
    elif('paper' in plays and 'rock' in plays):
        if(opponent_play == 'paper'):
            #Lost
            return 0 + rps_result[my_play]
        else:
            #Won
            return 6 + rps_result[my_play]

def who_beats_who(play, desired_result):
    #return which selection wins or looses depending on the play
    if(desired_result == 'win'):
        return rock_paper_scissor_inv[win_selection[rock_paper_scissor[play]]]

    if(desired_result == 'loose'):
        return rock_paper_scissor_inv[loose_selection[rock_paper_scissor[play]]]
    
    if(desired_result == 'draw'):
        return rock_paper_scissor_inv[rock_paper_scissor[play]]
    


#? strategy guide input
path = 'C:/Users/Diegob/Documents/pythonSnippets/aoc_input_day2.txt' #AOC input txt
strategy_guide_df = pd.read_csv(path, header=None, sep=' ' )
strategy_guide_df = strategy_guide_df.set_axis(['Opponent', 'Mine'], axis=1)
#print(strategy_guide_df)

strategy_guide_df['Result'] = strategy_guide_df.apply(lambda row: play_result(rock_paper_scissor[row['Opponent']], rock_paper_scissor[row['Mine']]), axis=1) #calculate the result of each round
#print(strategy_guide_df)
total = sum(strategy_guide_df['Result'].values.tolist())
#print(total)

#!---------PART TWO-----------
#Play by specific outcome desired
strategy_guide_df['Outcome desired'] = strategy_guide_df['Mine'].map(desired_outcomes) #map desired outcome of each round
strategy_guide_df['Mine new'] = strategy_guide_df.apply(lambda row: who_beats_who(row['Opponent'], row['Outcome desired']), axis=1) #get the play needed for the desired outcome
strategy_guide_df['Result new'] = strategy_guide_df.apply(lambda row: play_result(rock_paper_scissor[row['Opponent']], rock_paper_scissor[row['Mine new']]), axis=1) #Result of each round with the new plays given by the desired outcome
print(strategy_guide_df)
total_new = sum(strategy_guide_df['Result new'].values.tolist())
print(total_new)
import pandas as pd
# import numpy as np
import practice
ipl_match = pd.read_csv('ipl-matches_data.csv')
ipl = list(set(list(ipl_match['Team1'])+ list(ipl_match['Team2'])))
ipl2 = ipl
# print(ipl)
def teamsApi():
    teams = ipl2
    tean_dict ={
        'teams':teams
    }
    return tean_dict

# third 
# ///////////////////////////
# simple_data = pd.read_csv('simple.csv', encoding='latin-1')
# change = simple_data['Customer Name'],['City']

# ////////////////////////////////////////////////////////////////////////////////


# second featch api
data = pd.read_csv('ipl-matches_data.csv')
a = team1='Rajasthan Royals'
b = team2 ='Royal Challengers Bangalore'

value_c = data[
    (data['Team1'] == team1 )& (data['Team2'] == team2) |
    (data['Team1'] == team2 )& (data['Team2'] == team1) ]

total_match = value_c.shape[0]

match1_team1 = value_c['WinningTeam'].value_counts()[team1]
match2_team2 = value_c['WinningTeam'].value_counts()[team2]
match1 = str(match1_team1)
match2 = str(match2_team2)
drow = total_match-(match1_team1 +match2_team2)

# function 
def team_vs_team(team1,team2):
    value_c =data[(data['Team1'] == team1 )& (data['Team2'] == team2) |(data['Team1'] == team2 )& (data['Team2'] == team1) ]
    total_match = value_c.shape[0]

    match1_team1 = value_c['WinningTeam'].value_counts()[team1]
    match2_team2 = value_c['WinningTeam'].value_counts()[team2]

    drow = total_match-(match1_team1 +match2_team2)
    
    # convert dictionary
    respons = {
        # useing str because dend string formate
        'total_match':str(total_match),
        'team1':str(match1_team1),
        'team2':str(match2_team2),
        'drow':str(drow)

    }
    return respons
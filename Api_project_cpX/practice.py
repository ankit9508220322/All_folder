import pandas as pd
data = pd.read_csv('ipl-matches_data.csv')
a = team1='Rajasthan Royals'
b = team2 ='Royal Challengers Bangalore'

value_c = data[ (data['Team1'] == team1 )& (data['Team2'] == team2) | (data['Team1'] == team2 )& (data['Team2'] == team1) ]

total_match = value_c.shape[0]

match1_team1 = value_c['WinningTeam'].value_counts()[team1]
match2_team2 = value_c['WinningTeam'].value_counts()[team2]
drow = total_match -(match1_team1 +match2_team2)

# print("Total Match: ",total_match)
# print('Rajasthan Royals=: ',match1_team1)
# print('Royal Challengers Bangalore:= ',match2_team2)
# print("All drow Match:= ",drow)
# //////////////////////////////////////////////////////
# function 

def team_vs_team(team1,team2):
    value_c =data[(data['Team1'] == team1 )& (data['Team2'] == team2) |(data['Team1'] == team2 )& (data['Team2'] == team1) ]
    total_match = value_c.shape[0]

    match1_team1 = value_c['WinningTeam'].value_counts()[team1]
    match2_team2 = value_c['WinningTeam'].value_counts()[team2]

    drow = total_match-(match1_team1 +match2_team2)
    
    # convert dictionary
    respons = {
        'total_match':total_match,
        'team1':match1_team1,
        'team2':match2_team2,
        'drow':drow

    }
    return respons
obj = team_vs_team('Rajasthan Royals', 'Royal Challengers Bangalore')

# print(f"""
# Rajasthan Royals vs
# Royal Challengers Bangalore

# Total Match: {obj['total_match']}
# Team1 Wins: {obj['team1']}
# Team2 Wins: {obj['team2']}
# Drow: {obj['drow']}
# """)


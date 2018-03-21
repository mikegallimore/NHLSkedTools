# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 11:41:23 2018

@author: Michael
"""
import pandas as pd
import numpy as np
import file_param

team_list = ['ANA', 'ARI', 'BOS', 'BUF', 'CAR', 'CBJ', 'CGY', 'CHI', 'COL', 'DAL', 'DET', 'EDM', 'FLA', 'LAK', 'MIN', 'MTL', 'NJD', 'NSH', 'NYI', 'NYR', 'OTT', 'PHI', 'PIT', 'SJS', 'STL', 'TBL', 'TOR', 'VAN', 'VGK', 'WPG', 'WSH']

fileseason = file_param.fileseason

### convert the season value to string
fileseason = str(fileseason)

### establish the base path
base_path = '/Users/Michael/Desktop/NHL_SkedTools/'

### location the root version of the season schedule, prior to any manipulation
masterfile = base_path + 'Data/' + fileseason + '/Tables/Master/' + fileseason + '_' + 'schedule_regular_master.csv'
    
### create a dataframe object that reads in info from the .csv file identified by the 'masterfile' variable
schedule_df = pd.read_csv(masterfile)

### write each team's schedule to CSV and then reopen and write the game sequence to the same CSV file
for team in team_list:
    team_path = base_path + 'Data/' + fileseason + '/Tables/Teams/' + fileseason + '_' + team + '_' + 'schedule_regular.csv'
    team_schedule_df = schedule_df[(schedule_df['HOME_TEAM'] == team) | (schedule_df['AWAY_TEAM'] == team)]
    team_schedule_df.to_csv(team_path, encoding='utf-8', index=False)

    team_sequenced_df = pd.read_csv(team_path)
    team_sequenced_df['SEQUENCE'] = team_sequenced_df.index
    team_sequenced_df['SEQUENCE'] += 1
    team_sequenced_df.insert(loc=1, column='TEAM', value=team)
  
    winpoints = (np.where((team_sequenced_df['HOME_RESULT'] == 'WIN') & (team_sequenced_df['HOME_TEAM'] == team), int(2), 0) | np.where((team_sequenced_df['AWAY_RESULT'] == 'WIN') & (team_sequenced_df['AWAY_TEAM'] == team), int(2), 0)) / 2
    team_sequenced_df['W'] = winpoints.cumsum()
    losspoints = (np.where((team_sequenced_df['HOME_RESULT'] == 'LOSS') & (team_sequenced_df['HOME_TEAM'] == team), int(1), 0) | np.where((team_sequenced_df['AWAY_RESULT'] == 'LOSS') & (team_sequenced_df['AWAY_TEAM'] == team), int(1), 0))
    team_sequenced_df['L'] = losspoints.cumsum()
    regot_winpoints = (np.where((team_sequenced_df['HOME_RESULT'] == 'WIN') & (team_sequenced_df['HOME_TEAM'] == team) & (team_sequenced_df['GAME_TYPE'] != 'SHOOTOUT'), int(2), 0) | np.where((team_sequenced_df['AWAY_RESULT'] == 'WIN') & (team_sequenced_df['AWAY_TEAM'] == team) & (team_sequenced_df['GAME_TYPE'] != 'SHOOTOUT'), int(2), 0)) / 2
    team_sequenced_df['ROT_W'] = regot_winpoints.cumsum()    
    regot_losspoints = (np.where((team_sequenced_df['HOME_RESULT'] == 'LOSS') & (team_sequenced_df['HOME_TEAM'] == team) & (team_sequenced_df['GAME_TYPE'] != 'SHOOTOUT'), int(1), 0) | np.where((team_sequenced_df['AWAY_RESULT'] == 'LOSS') & (team_sequenced_df['AWAY_TEAM'] == team) & (team_sequenced_df['GAME_TYPE'] != 'SHOOTOUT'), int(1), 0))
    team_sequenced_df['ROT_L'] = regot_losspoints.cumsum()    
    reg_winpoints = (np.where((team_sequenced_df['HOME_RESULT'] == 'WIN') & (team_sequenced_df['HOME_TEAM'] == team) & (team_sequenced_df['GAME_TYPE'] == 'REGULATION'), int(2), 0) | np.where((team_sequenced_df['AWAY_RESULT'] == 'WIN') & (team_sequenced_df['AWAY_TEAM'] == team) & (team_sequenced_df['GAME_TYPE'] == 'REGULATION'), int(2), 0)) / 2
    team_sequenced_df['R_W'] = reg_winpoints.cumsum()    
    reg_losspoints = (np.where((team_sequenced_df['HOME_RESULT'] == 'LOSS') & (team_sequenced_df['HOME_TEAM'] == team) & (team_sequenced_df['GAME_TYPE'] == 'REGULATION'), int(1), 0) | np.where((team_sequenced_df['AWAY_RESULT'] == 'LOSS') & (team_sequenced_df['AWAY_TEAM'] == team) & (team_sequenced_df['GAME_TYPE'] == 'REGULATION'), int(1), 0))
    team_sequenced_df['R_L'] = reg_losspoints.cumsum()    
    ot_winpoints = (np.where((team_sequenced_df['HOME_RESULT'] == 'WIN') & (team_sequenced_df['HOME_TEAM'] == team) & (team_sequenced_df['GAME_TYPE'] == 'OVERTIME'), int(2), 0) | np.where((team_sequenced_df['AWAY_RESULT'] == 'WIN') & (team_sequenced_df['AWAY_TEAM'] == team) & (team_sequenced_df['GAME_TYPE'] == 'OVERTIME'), int(2), 0)) / 2
    team_sequenced_df['OT_W'] = ot_winpoints.cumsum()    
    ot_losspoints = (np.where((team_sequenced_df['HOME_RESULT'] == 'LOSS') & (team_sequenced_df['HOME_TEAM'] == team) & (team_sequenced_df['GAME_TYPE'] == 'OVERTIME'), int(1), 0) | np.where((team_sequenced_df['AWAY_RESULT'] == 'LOSS') & (team_sequenced_df['AWAY_TEAM'] == team) & (team_sequenced_df['GAME_TYPE'] == 'OVERTIME'), int(1), 0))
    team_sequenced_df['OT_L'] = ot_losspoints.cumsum()    
    so_winpoints = (np.where((team_sequenced_df['HOME_RESULT'] == 'WIN') & (team_sequenced_df['HOME_TEAM'] == team) & (team_sequenced_df['GAME_TYPE'] == 'SHOOTOUT'), int(2), 0) | np.where((team_sequenced_df['AWAY_RESULT'] == 'WIN') & (team_sequenced_df['AWAY_TEAM'] == team) & (team_sequenced_df['GAME_TYPE'] == 'SHOOTOUT'), int(2), 0)) / 2
    team_sequenced_df['SO_W'] = so_winpoints.cumsum()    
    so_losspoints = (np.where((team_sequenced_df['HOME_RESULT'] == 'LOSS') & (team_sequenced_df['HOME_TEAM'] == team) & (team_sequenced_df['GAME_TYPE'] == 'SHOOTOUT'), int(1), 0) | np.where((team_sequenced_df['AWAY_RESULT'] == 'LOSS') & (team_sequenced_df['AWAY_TEAM'] == team) & (team_sequenced_df['GAME_TYPE'] == 'SHOOTOUT'), int(1), 0))
    team_sequenced_df['SO_L'] = so_losspoints.cumsum()    

    gamepoints = np.where((team_sequenced_df['HOME_RESULT'] == 'WIN') & (team_sequenced_df['HOME_TEAM'] == team), int(2), 0) | np.where((team_sequenced_df['AWAY_RESULT'] == 'WIN') & (team_sequenced_df['AWAY_TEAM'] == team), int(2), 0) | np.where((team_sequenced_df['HOME_RESULT'] == 'LOSS') & (team_sequenced_df['HOME_TEAM'] == team) & (team_sequenced_df['GAME_TYPE'] != 'REGULATION'), int(1), 0) | np.where((team_sequenced_df['AWAY_RESULT'] == 'LOSS') & (team_sequenced_df['AWAY_TEAM'] == team) & (team_sequenced_df['GAME_TYPE'] != 'REGULATION'), int(1), 0)    
    team_sequenced_df['GAME_POINTS'] = gamepoints
    team_sequenced_df['TOTAL_POINTS'] = team_sequenced_df['GAME_POINTS'].cumsum()  

    goals_for = (np.where((team_sequenced_df['HOME_RESULT'] == 'WIN') & (team_sequenced_df['HOME_TEAM'] == team), team_sequenced_df['HOME_GOALS'], 0) | np.where((team_sequenced_df['HOME_RESULT'] == 'LOSS') & (team_sequenced_df['HOME_TEAM'] == team), team_sequenced_df['HOME_GOALS'], 0) | np.where((team_sequenced_df['AWAY_RESULT'] == 'WIN') & (team_sequenced_df['AWAY_TEAM'] == team), team_sequenced_df['AWAY_GOALS'], 0) | np.where((team_sequenced_df['AWAY_RESULT'] == 'LOSS') & (team_sequenced_df['AWAY_TEAM'] == team), team_sequenced_df['AWAY_GOALS'], 0))
    team_sequenced_df['GOALS_FOR'] = goals_for.cumsum()
    goals_against = (np.where((team_sequenced_df['HOME_RESULT'] == 'WIN') & (team_sequenced_df['HOME_TEAM'] != team), team_sequenced_df['HOME_GOALS'], 0) | np.where((team_sequenced_df['HOME_RESULT'] == 'LOSS') & (team_sequenced_df['HOME_TEAM'] != team), team_sequenced_df['HOME_GOALS'], 0) | np.where((team_sequenced_df['AWAY_RESULT'] == 'WIN') & (team_sequenced_df['AWAY_TEAM'] != team), team_sequenced_df['AWAY_GOALS'], 0) | np.where((team_sequenced_df['AWAY_RESULT'] == 'LOSS') & (team_sequenced_df['AWAY_TEAM'] != team), team_sequenced_df['AWAY_GOALS'], 0))
    team_sequenced_df['GOALS_AGAINST'] = goals_against.cumsum()
    team_sequenced_df['GOALS_DIFF'] = (goals_for - goals_against).cumsum()

    base_pace = team_sequenced_df['SEQUENCE'] * 1.2
    fiveover_pace = (team_sequenced_df['SEQUENCE'] * 1.26) - base_pace
    fiveunder_pace = (team_sequenced_df['SEQUENCE'] * -1.26) + base_pace
    team_sequenced_df['BASE_PACE'] = base_pace
    team_sequenced_df['5OVER_PACE'] = fiveover_pace
    team_sequenced_df['5UNDER_PACE'] = fiveunder_pace
    team_sequenced_df['DEVIATION'] = team_sequenced_df['TOTAL_POINTS'] - base_pace
    
    team_sequenced_df.to_csv(team_path, encoding='utf-8', index=False)

    print('Finished schedule + sequencing for: ' + team)
    
### load each team's csv
team_path = base_path + 'Data/' + fileseason + '/Tables/Teams/' + fileseason

ANA_schedule_df = pd.read_csv(team_path + '_ANA_schedule_regular.csv')
ARI_schedule_df = pd.read_csv(team_path + '_ARI_schedule_regular.csv')
BOS_schedule_df = pd.read_csv(team_path + '_BOS_schedule_regular.csv')
BUF_schedule_df = pd.read_csv(team_path + '_BUF_schedule_regular.csv')
CAR_schedule_df = pd.read_csv(team_path + '_CAR_schedule_regular.csv')
CBJ_schedule_df = pd.read_csv(team_path + '_CBJ_schedule_regular.csv')
CGY_schedule_df = pd.read_csv(team_path + '_CGY_schedule_regular.csv')
CHI_schedule_df = pd.read_csv(team_path + '_CHI_schedule_regular.csv')
COL_schedule_df = pd.read_csv(team_path + '_COL_schedule_regular.csv')
DAL_schedule_df = pd.read_csv(team_path + '_DAL_schedule_regular.csv')
DET_schedule_df = pd.read_csv(team_path + '_DET_schedule_regular.csv')
EDM_schedule_df = pd.read_csv(team_path + '_EDM_schedule_regular.csv')
FLA_schedule_df = pd.read_csv(team_path + '_FLA_schedule_regular.csv')
LAK_schedule_df = pd.read_csv(team_path + '_LAK_schedule_regular.csv')
MIN_schedule_df = pd.read_csv(team_path + '_MIN_schedule_regular.csv')
MTL_schedule_df = pd.read_csv(team_path + '_MTL_schedule_regular.csv')
NJD_schedule_df = pd.read_csv(team_path + '_NJD_schedule_regular.csv')
NSH_schedule_df = pd.read_csv(team_path + '_NSH_schedule_regular.csv')
NYI_schedule_df = pd.read_csv(team_path + '_NYI_schedule_regular.csv')
NYR_schedule_df = pd.read_csv(team_path + '_NYR_schedule_regular.csv')
OTT_schedule_df = pd.read_csv(team_path + '_OTT_schedule_regular.csv')
PHI_schedule_df = pd.read_csv(team_path + '_PHI_schedule_regular.csv')
PIT_schedule_df = pd.read_csv(team_path + '_PIT_schedule_regular.csv')
SJS_schedule_df = pd.read_csv(team_path + '_SJS_schedule_regular.csv')
STL_schedule_df = pd.read_csv(team_path + '_STL_schedule_regular.csv')
TBL_schedule_df = pd.read_csv(team_path + '_TBL_schedule_regular.csv')
TOR_schedule_df = pd.read_csv(team_path + '_TOR_schedule_regular.csv')
VAN_schedule_df = pd.read_csv(team_path + '_VAN_schedule_regular.csv')
VGK_schedule_df = pd.read_csv(team_path + '_VGK_schedule_regular.csv')
WPG_schedule_df = pd.read_csv(team_path + '_WPG_schedule_regular.csv')
WSH_schedule_df = pd.read_csv(team_path + '_WSH_schedule_regular.csv')

### make a compilation of the schedules for each team
allteams = base_path + 'Data/' + fileseason + '/Tables/Teams/Composite/' + fileseason + '_composite_' + 'schedule_regular.csv'
teams_sequenced_df = pd.concat([ANA_schedule_df, ARI_schedule_df, BOS_schedule_df, BUF_schedule_df, CAR_schedule_df, CBJ_schedule_df, CGY_schedule_df, CHI_schedule_df, COL_schedule_df, DAL_schedule_df, EDM_schedule_df, DET_schedule_df, FLA_schedule_df, LAK_schedule_df, MIN_schedule_df, MTL_schedule_df, NJD_schedule_df, NSH_schedule_df, NYI_schedule_df, NYR_schedule_df, OTT_schedule_df, PHI_schedule_df, PHI_schedule_df, PIT_schedule_df, SJS_schedule_df, STL_schedule_df, TBL_schedule_df, TOR_schedule_df, VAN_schedule_df, VGK_schedule_df, WPG_schedule_df, WSH_schedule_df])
teams_sequenced_df.to_csv(allteams, encoding='utf-8', index=False)

print('Finished compiling schedules + sequencing for: 31 teams.')
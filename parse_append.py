# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 20:40:14 2017

@author: Michael
"""
import requests
import csv
import file_param
from datetime import datetime

fileseason = file_param.fileseason
filegame1 = file_param.filegame1
filegame2 = file_param.filegame2

### convert the season and game values into strings
fileseason = str(fileseason)
filegame1 = str(filegame1)
filegame2 = str(filegame2)

regularseason = list(range(20001, 21231)) if fileseason < '20172018' else list(range(20001, 21272))

gamerange = regularseason
gamerange = (i for i in gamerange if i >= int(filegame1) and i <= int(filegame2))

for filegame in gamerange:
    infile = '/Users/Michael/Desktop/NHL_SkedTools/Data/' + fileseason + '/Tables/Master/' + fileseason + '_' + 'schedule_regular_master.csv'

    with open(infile, 'a', newline='') as inandoutFile:
        csvWriter = csv.writer(inandoutFile)

        ### locate and decode the league's json feed for the selected game in the selected season
        url = "http://statsapi.web.nhl.com/api/v1/game/" + fileseason[0:4] + "0" + str(filegame) + "/feed/live"
        url_in = requests.get(url)
        url_parsed = url_in.json()

        ### extracts a value that contains the season and game number (e.g. 2017020001)
        game = url_parsed["gamePk"]

        ### extract status of game play (IMPORTANT: a game should not be processed until its status is final)
        gamestatus = url_parsed["liveData"]["linescore"]["currentPeriodTimeRemaining"]

        ### extracts the season (e.g. 20172018)
        season = url_parsed["gameData"]["game"]["season"]

        ### extract the 5-digit game id
        gameid = str(game)[5:10]

        ### extract and format the date 
        date = url_parsed["gameData"]["datetime"]["dateTime"].split('T')[0]
        date = datetime.strftime(datetime.strptime(date, '%Y-%m-%d'), '%m/%d/%Y') # format conversion
        date = str(date)

        ### extract the 3-letter home and away abbreviations
        home = url_parsed["gameData"]["teams"]["home"]["triCode"]
        away = url_parsed["gameData"]["teams"]["away"]["triCode"]

        ### extract the number of goals for both the home and away team
        homegoals = url_parsed["liveData"]["boxscore"]["teams"]["home"]["teamStats"]["teamSkaterStats"]["goals"]
        awaygoals = url_parsed["liveData"]["boxscore"]["teams"]["away"]["teamStats"]["teamSkaterStats"]["goals"]

        ### determine whether the game ended in regulation, overtime or shootout
        gametype = str()

        currentperiod = url_parsed["liveData"]["linescore"]["currentPeriod"]

        if gamestatus == 'Final' and currentperiod < 4:
            gametype = 'REGULATION'
        elif gamestatus == 'Final' and currentperiod == 4:
            gametype = 'OVERTIME'
        elif gamestatus == 'Final' and currentperiod == 5:
            gametype = 'SHOOTOUT'

        ### determine the home and away result
        homeresult = str()
        awayresult = str()

        if homegoals > awaygoals:
            homeresult = 'WIN'
            awayresult = 'LOSS'
        elif awaygoals > homegoals:
            homeresult = 'LOSS'
            awayresult = 'WIN'

        ### make adjustments for games that end  in a shootout
        shootout_homegoals = int()
        shootout_awaygoals = int()
        
        if gametype == 'SHOOTOUT':
            shootout_homegoals = url_parsed["liveData"]["linescore"]["shootoutInfo"]["home"]["scores"]
            shootout_awaygoals = url_parsed["liveData"]["linescore"]["shootoutInfo"]["away"]["scores"]
        
        if shootout_homegoals > shootout_awaygoals:
            homegoals = homegoals + 1
            homeresult = 'WIN'
            awayresult = 'LOSS'
        if shootout_awaygoals > shootout_homegoals:
            awaygoals = homegoals + 1
            homeresult = 'LOSS'
            awayresult = 'WIN'
      
        ### arrange the output
        game_info = [season, '', gameid, date, home, away, homegoals, awaygoals, gametype, homeresult, awayresult]
    
        # write out the play-by-play in the desired, custom format
        csvWriter.writerow(game_info)

        print(game_info)
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 20:40:14 2017

@author: Michael
"""
import requests
from datetime import datetime

fileseason = 20172018
filegame = 20001

### convert the season and game values into strings
fileseason = str(fileseason)
filegame = str(filegame)

### locate and decode the league's json feed for the selected game in the selected season
url = "http://statsapi.web.nhl.com/api/v1/game/" + fileseason[0:4] + "0" + filegame + "/feed/live"
url_in = requests.get(url)
url_parsed = url_in.json()

### extracts a value that contains the season and game number (e.g. 2017020001)
game = url_parsed["gamePk"]

### extracts the season (e.g. 20172018)
season = url_parsed["gameData"]["game"]["season"]

### extract the 5-digit game id
gameid = str(game)[5:10]

### extract status of game play (IMPORTANT: a game should not be processed until its status is final)
gamestatus = url_parsed["liveData"]["linescore"]["currentPeriodTimeRemaining"]

### shorten the game id to the game's slot in the league calendar
gameseq = str()

if int(gameid) < 20010:
    gameseq = gameid[4:]
elif int(gameid) < 20100:
    gameseq = gameid[3:]
elif int(gameid) < 21000:
    gameseq = gameid[2:]
elif int(gameid) < 30000:
    gameseq = gameid[1:]

seasontype = url_parsed["gameData"]["game"]["type"]

if seasontype == 'R':
    seasontype = 'REGULAR'

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

### arrange the output
game_info = [season, gameseq, gameid, date, home, away, homegoals, awaygoals, gametype, homeresult, awayresult]

print(game_info)
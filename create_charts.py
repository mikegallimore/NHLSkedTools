# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 11:41:23 2018

@author: Michael
"""
import pandas as pd
import numpy as np
import file_param
import matplotlib.pyplot as plt

### Begin Micah's code

def formClusters(vals,e=3): #e is for epsilon
    if vals == {}: return []

    items = [(x,y) for x,(_,y) in sorted(vals.items(),key=lambda x:x[1])]

    def overlap(dist,gap):  #dist is the coord distance between them, gap the ordinal distance
        if gap == 1: return dist < e
        if gap == 2: return dist < 2.1*e
        if gap == 3: return dist < 2.7*e
        if gap == 4: return dist < 3.7*e
        if gap == 5: return dist < 4.8*e
        if gap == 6: return dist < 5.4*e
        if gap == 7: return dist < 6.8*e
        return dist < gap*e

    links = []

    for i,(x1,y1) in enumerate(items):
        for j,(x2,y2) in enumerate(items):
            if i >= j: continue

            if overlap(abs(y1-y2),abs(i-j)):
                links.append((x1,x2))

    marked = []
    clusters = []
    for x,y in items:
        if x in marked: continue    #got this one already

        cluster = [x]
        for a,b in links:
            if a in cluster: cluster.append(b); marked.append(b)
            if b in cluster: cluster.append(a); marked.append(a)

        clusters.append(list(set(cluster)))

    return clusters
    
### end Micah's code

team_list = ['ANA', 'ARI', 'BOS', 'BUF', 'CAR', 'CBJ', 'CGY', 'CHI', 'COL', 'DAL', 'DET', 'EDM', 'FLA', 'LAK', 'MIN', 'MTL', 'NJD', 'NSH', 'NYI', 'NYR', 'OTT', 'PHI', 'PIT', 'SJS', 'STL', 'TBL', 'TOR', 'VAN', 'VGK', 'WPG', 'WSH']

fileseason = file_param.fileseason

### convert the season value to string
fileseason = str(fileseason)

### establish the base path
base_path = '/Users/Michael/Desktop/NHL_SkedTools/'
    
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

### create line charts for each division
chart_path = base_path + 'Data/' + fileseason + '/Charts/Teams/' + fileseason

BOS_pointspace_chart = BOS_schedule_df.plot(x='SEQUENCE', y='DEVIATION', label='BOS', color = '#FCB514')
BUF_pointspace_chart = BUF_schedule_df.plot(x='SEQUENCE', y='DEVIATION', label='BUF', color = '#FCB514', ax=BOS_pointspace_chart)
DET_pointspace_chart = DET_schedule_df.plot(x='SEQUENCE', y='DEVIATION', label='DET', color = '#CE1126', ax=BOS_pointspace_chart)
FLA_pointspace_chart = FLA_schedule_df.plot(x='SEQUENCE', y='DEVIATION', label='FLA', color = '#B9975B', ax=BOS_pointspace_chart)
MTL_pointspace_chart = MTL_schedule_df.plot(x='SEQUENCE', y='DEVIATION', label='MTL', color = '#AF1E2D', ax=BOS_pointspace_chart)
OTT_pointspace_chart = OTT_schedule_df.plot(x='SEQUENCE', y='DEVIATION', label='OTT', color = '#000000', ax=BOS_pointspace_chart)
TBL_pointspace_chart = TBL_schedule_df.plot(x='SEQUENCE', y='DEVIATION', label='TBL', color = '#000000', ax=BOS_pointspace_chart)
TOR_pointspace_chart = TOR_schedule_df.plot(x='SEQUENCE', y='DEVIATION', label='TOR', color = '#003E7E', ax=BOS_pointspace_chart)

twentyover_x, twentyover_y = [-1,83],[0,20]
tenover_x, tenover_y = [-1,83],[0,10]
basepace_x, basepace_y = [-1,83],[0,0]
tenunder_x, tenunder_y = [-1,83],[0,-10]
twentyunder_x, twentyunder_y = [-1,83],[0,-20]
twentyover_pace = plt.plot(twentyover_x, twentyover_y, marker = 'o', linestyle = '--', color = 'green', alpha=0.25)
tenover_pace = plt.plot(tenover_x, tenover_y, marker = 'o', linestyle = '--', color = 'green', alpha=0.25)
basepace = plt.plot(basepace_x, basepace_y, marker = 'o', linestyle = '--', color = 'black', alpha=0.25)
tenunder_pace = plt.plot(tenunder_x, tenunder_y, marker = 'o', linestyle = '--', color = 'red', alpha=0.25)
twentyunder_pace = plt.plot(twentyunder_x, twentyunder_y, marker = 'o', linestyle = '--', color = 'red', alpha=0.25)
plt.text(85, 19, '20-over', fontsize=12, color='green', alpha=0.5)
plt.text(85, 9, '10-over', fontsize=12, color='green', alpha=0.5)
plt.text(85, -1, '96 pts', fontsize=12, color='black', alpha=0.5)
plt.text(85, -11, '10-under', fontsize=12, color='red', alpha=0.5)
plt.text(85, -21, '20-under', fontsize=12, color='red', alpha=0.5)

plt.title('Atlantic Division Playoffs Pacing')
plt.xlabel('Games Played')
plt.ylabel('')
plt.xlim(0,82)

ax = plt.subplot(111)
ax.spines["top"].set_visible(False)    
ax.spines["bottom"].set_visible(False)    
ax.spines["right"].set_visible(False)    
ax.spines["left"].set_visible(False)  

plt.tick_params(axis="both", which="both", bottom="off", top="off", labelbottom="on", left="off", right="off", labelleft="off") 

ax.legend_.remove()

BOS_x_pos = BOS_schedule_df.SEQUENCE.iat[-1] + 1
BOS_y_pos = BOS_schedule_df.DEVIATION.iat[-1] - 0.5
plt.text(BOS_x_pos, BOS_y_pos, 'BOS', fontsize=12, color='#FCB514')
BUF_x_pos = BUF_schedule_df.SEQUENCE.iat[-1] + 1
BUF_y_pos = BUF_schedule_df.DEVIATION.iat[-1] - 0.5
plt.text(BUF_x_pos, BUF_y_pos, 'BUF', fontsize=12, color='#FCB514')
DET_x_pos = DET_schedule_df.SEQUENCE.iat[-1] + 1
DET_y_pos = DET_schedule_df.DEVIATION.iat[-1] - 0.5
plt.text(DET_x_pos, DET_y_pos, 'DET', fontsize=12, color='#CE1126')
FLA_x_pos = FLA_schedule_df.SEQUENCE.iat[-1] + 1
FLA_y_pos = FLA_schedule_df.DEVIATION.iat[-1] - 0.5
plt.text(FLA_x_pos, FLA_y_pos, 'FLA', fontsize=12, color='#B9975B')
MTL_x_pos = MTL_schedule_df.SEQUENCE.iat[-1] + 1
MTL_y_pos = MTL_schedule_df.DEVIATION.iat[-1] - 0.5
plt.text(MTL_x_pos, MTL_y_pos, 'MTL', fontsize=12, color='#AF1E2D')
OTT_x_pos = OTT_schedule_df.SEQUENCE.iat[-1] + 1
OTT_y_pos = OTT_schedule_df.DEVIATION.iat[-1] - 0.5
plt.text(OTT_x_pos, OTT_y_pos, 'OTT', fontsize=12, color='#000000')
TBL_x_pos = TBL_schedule_df.SEQUENCE.iat[-1] + 1
TBL_y_pos = TBL_schedule_df.DEVIATION.iat[-1] - 0.5
plt.text(TBL_x_pos, TBL_y_pos, 'TBL', fontsize=12, color='#000000')
TOR_x_pos = TOR_schedule_df.SEQUENCE.iat[-1] + 1
TOR_y_pos = TOR_schedule_df.DEVIATION.iat[-1] - 0.5
plt.text(TOR_x_pos, TOR_y_pos, 'TOR', fontsize=12, color='#003E7E')

#plt.style.use('ggplot')

#plt.show()
plt.savefig(base_path +  'Data/' + fileseason + '/Charts/Division/' + fileseason + '_atlantic_pacing.jpg', bbox_inches='tight', pad_inches=0.2)

print('Finished points pace plot for: Atlantic Division')

CAR_pointspace_chart = CAR_schedule_df.plot(x='SEQUENCE', y='DEVIATION', label='CAR', color = '#CC0000')
CBJ_pointspace_chart = CBJ_schedule_df.plot(x='SEQUENCE', y='DEVIATION', label='CBJ', color = '#A4A9AD', ax=CAR_pointspace_chart)
NJD_pointspace_chart = NJD_schedule_df.plot(x='SEQUENCE', y='DEVIATION', label='NJD', color = '#000000', ax=CAR_pointspace_chart)
NYI_pointspace_chart = NYI_schedule_df.plot(x='SEQUENCE', y='DEVIATION', label='NYI', color = '#F26924', ax=CAR_pointspace_chart)
NYR_pointspace_chart = NYR_schedule_df.plot(x='SEQUENCE', y='DEVIATION', label='NYR', color = '#0038A8', ax=CAR_pointspace_chart)
PHI_pointspace_chart = PHI_schedule_df.plot(x='SEQUENCE', y='DEVIATION', label='PHI', color = '#F74902', ax=CAR_pointspace_chart)
PIT_pointspace_chart = PIT_schedule_df.plot(x='SEQUENCE', y='DEVIATION', label='PIT', color = '#FFB81C', ax=CAR_pointspace_chart)
WSH_pointspace_chart = WSH_schedule_df.plot(x='SEQUENCE', y='DEVIATION', label='WSH', color = '#CF0A2C', ax=CAR_pointspace_chart)

twentyover_x, twentyover_y = [-1,83],[0,20]
tenover_x, tenover_y = [-1,83],[0,10]
basepace_x, basepace_y = [-1,83],[0,0]
tenunder_x, tenunder_y = [-1,83],[0,-10]
twentyunder_x, twentyunder_y = [-1,83],[0,-20]
twentyover_pace = plt.plot(twentyover_x, twentyover_y, marker = 'o', linestyle = '--', color = 'green', alpha=0.25)
tenover_pace = plt.plot(tenover_x, tenover_y, marker = 'o', linestyle = '--', color = 'green', alpha=0.25)
basepace = plt.plot(basepace_x, basepace_y, marker = 'o', linestyle = '--', color = 'black', alpha=0.25)
tenunder_pace = plt.plot(tenunder_x, tenunder_y, marker = 'o', linestyle = '--', color = 'red', alpha=0.25)
twentyunder_pace = plt.plot(twentyunder_x, twentyunder_y, marker = 'o', linestyle = '--', color = 'red', alpha=0.25)
plt.text(85, 19, '20-over', fontsize=12, color='green', alpha=0.5)
plt.text(85, 9, '10-over', fontsize=12, color='green', alpha=0.5)
plt.text(85, -1, '96 pts', fontsize=12, color='black', alpha=0.5)
plt.text(85, -11, '10-under', fontsize=12, color='red', alpha=0.5)
plt.text(85, -21, '20-under', fontsize=12, color='red', alpha=0.5)

plt.title('Metropolitan Division Playoffs Pacing')
plt.xlabel('Games Played')
plt.ylabel('')
plt.xlim(0,82)

ax = plt.subplot(111)
ax.spines["top"].set_visible(False)    
ax.spines["bottom"].set_visible(False)    
ax.spines["right"].set_visible(False)    
ax.spines["left"].set_visible(False)  

plt.tick_params(axis="both", which="both", bottom="off", top="off", labelbottom="on", left="off", right="off", labelleft="off") 

ax.legend_.remove()

CAR_x_pos = CAR_schedule_df.SEQUENCE.iat[-1] + 1
CAR_y_pos = CAR_schedule_df.DEVIATION.iat[-1] - 0.5
plt.text(CAR_x_pos, CAR_y_pos, 'CAR', fontsize=12, color='#CC0000')
CBJ_x_pos = CBJ_schedule_df.SEQUENCE.iat[-1] + 1
CBJ_y_pos = CBJ_schedule_df.DEVIATION.iat[-1] - 0.5
plt.text(CBJ_x_pos, CBJ_y_pos, 'CBJ', fontsize=12, color='#A4A9AD')
NJD_x_pos = NJD_schedule_df.SEQUENCE.iat[-1] + 1
NJD_y_pos = NJD_schedule_df.DEVIATION.iat[-1] - 0.5
plt.text(NJD_x_pos, NJD_y_pos, 'NJD', fontsize=12, color='#000000')
NYI_x_pos = NYI_schedule_df.SEQUENCE.iat[-1] + 1
NYI_y_pos = NYI_schedule_df.DEVIATION.iat[-1] - 0.5
plt.text(NYI_x_pos, NYI_y_pos, 'NYI', fontsize=12, color='#F26924')
NYR_x_pos = NYR_schedule_df.SEQUENCE.iat[-1] + 1
NYR_y_pos = NYR_schedule_df.DEVIATION.iat[-1] - 0.5
plt.text(NYR_x_pos, NYR_y_pos, 'NYR', fontsize=12, color='#0038A8')
PHI_x_pos = PHI_schedule_df.SEQUENCE.iat[-1] + 1
PHI_y_pos = PHI_schedule_df.DEVIATION.iat[-1] - 0.5
plt.text(PHI_x_pos, PHI_y_pos, 'PHI', fontsize=12, color='#F74902')
PIT_x_pos = PIT_schedule_df.SEQUENCE.iat[-1] + 1
PIT_y_pos = PIT_schedule_df.DEVIATION.iat[-1] - 0.5
plt.text(PIT_x_pos, PIT_y_pos, 'PIT', fontsize=12, color='#FFB81C')
WSH_x_pos = WSH_schedule_df.SEQUENCE.iat[-1] + 1
WSH_y_pos = WSH_schedule_df.DEVIATION.iat[-1] - 0.5
plt.text(WSH_x_pos, WSH_y_pos, 'WSH', fontsize=12, color='#CF0A2C')

#plt.style.use('ggplot')

#plt.show()
plt.savefig(base_path +  'Data/' + fileseason + '/Charts/Division/' + fileseason + '_metropolitan_pacing.jpg', bbox_inches='tight', pad_inches=0.2)

print('Finished points pace plot for: Metropolitan Division')

CHI_pointspace_chart = CHI_schedule_df.plot(x='SEQUENCE', y='DEVIATION', label='CHI', color = '#000000')
COL_pointspace_chart = COL_schedule_df.plot(x='SEQUENCE', y='DEVIATION', label='COL', color = '#6F263D', ax=CHI_pointspace_chart)
DAL_pointspace_chart = DAL_schedule_df.plot(x='SEQUENCE', y='DEVIATION', label='DAL', color = '#006847', ax=CHI_pointspace_chart)
MIN_pointspace_chart = MIN_schedule_df.plot(x='SEQUENCE', y='DEVIATION', label='MIN', color = '#C51230', ax=CHI_pointspace_chart)
NSH_pointspace_chart = NSH_schedule_df.plot(x='SEQUENCE', y='DEVIATION', label='NSH', color = '#FFB81C', ax=CHI_pointspace_chart)
STL_pointspace_chart = STL_schedule_df.plot(x='SEQUENCE', y='DEVIATION', label='STL', color = '#002F87', ax=CHI_pointspace_chart)
WPG_pointspace_chart = WPG_schedule_df.plot(x='SEQUENCE', y='DEVIATION', label='WPG', color = '#8E9090', ax=CHI_pointspace_chart)

twentyover_x, twentyover_y = [-1,83],[0,20]
tenover_x, tenover_y = [-1,83],[0,10]
basepace_x, basepace_y = [-1,83],[0,0]
tenunder_x, tenunder_y = [-1,83],[0,-10]
twentyunder_x, twentyunder_y = [-1,83],[0,-20]
twentyover_pace = plt.plot(twentyover_x, twentyover_y, marker = 'o', linestyle = '--', color = 'green', alpha=0.25)
tenover_pace = plt.plot(tenover_x, tenover_y, marker = 'o', linestyle = '--', color = 'green', alpha=0.25)
basepace = plt.plot(basepace_x, basepace_y, marker = 'o', linestyle = '--', color = 'black', alpha=0.25)
tenunder_pace = plt.plot(tenunder_x, tenunder_y, marker = 'o', linestyle = '--', color = 'red', alpha=0.25)
twentyunder_pace = plt.plot(twentyunder_x, twentyunder_y, marker = 'o', linestyle = '--', color = 'red', alpha=0.25)
plt.text(85, 19, '20-over', fontsize=12, color='green', alpha=0.5)
plt.text(85, 9, '10-over', fontsize=12, color='green', alpha=0.5)
plt.text(85, -1, '96 pts', fontsize=12, color='black', alpha=0.5)
plt.text(85, -11, '10-under', fontsize=12, color='red', alpha=0.5)
plt.text(85, -21, '20-under', fontsize=12, color='red', alpha=0.5)

plt.title('Central Division Playoffs Pacing')
plt.xlabel('Games Played')
plt.ylabel('')
plt.xlim(0,82)

ax = plt.subplot(111)
ax.spines["top"].set_visible(False)    
ax.spines["bottom"].set_visible(False)    
ax.spines["right"].set_visible(False)    
ax.spines["left"].set_visible(False)  

plt.tick_params(axis="both", which="both", bottom="off", top="off", labelbottom="on", left="off", right="off", labelleft="off") 

ax.legend_.remove()

CHI_x_pos = CHI_schedule_df.SEQUENCE.iat[-1] + 1
CHI_y_pos = CHI_schedule_df.DEVIATION.iat[-1] - 0.5
plt.text(CHI_x_pos, CHI_y_pos, 'CHI', fontsize=12, color='#000000')
COL_x_pos = COL_schedule_df.SEQUENCE.iat[-1] + 1
COL_y_pos = COL_schedule_df.DEVIATION.iat[-1] - 0.5
plt.text(COL_x_pos, COL_y_pos, 'COL', fontsize=12, color='#6F263D')
DAL_x_pos = DAL_schedule_df.SEQUENCE.iat[-1] + 1
DAL_y_pos = DAL_schedule_df.DEVIATION.iat[-1] - 0.5
plt.text(DAL_x_pos, DAL_y_pos, 'DAL', fontsize=12, color='#006847')
MIN_x_pos = MIN_schedule_df.SEQUENCE.iat[-1] + 1
MIN_y_pos = MIN_schedule_df.DEVIATION.iat[-1] - 0.5
plt.text(MIN_x_pos, MIN_y_pos, 'MIN', fontsize=12, color='#C51230')
NSH_x_pos = NSH_schedule_df.SEQUENCE.iat[-1] + 1
NSH_y_pos = NSH_schedule_df.DEVIATION.iat[-1] - 0.5
plt.text(NSH_x_pos, NSH_y_pos, 'NSH', fontsize=12, color='#FFB81C')
STL_x_pos = STL_schedule_df.SEQUENCE.iat[-1] + 1
STL_y_pos = STL_schedule_df.DEVIATION.iat[-1] - 0.5
plt.text(STL_x_pos, STL_y_pos, 'STL', fontsize=12, color='#002F87')
WPG_x_pos = WPG_schedule_df.SEQUENCE.iat[-1] + 1
WPG_y_pos = WPG_schedule_df.DEVIATION.iat[-1] - 0.5
plt.text(WPG_x_pos, WPG_y_pos, 'WPG', fontsize=12, color='#8E9090')

#plt.style.use('ggplot')

#plt.show()
plt.savefig(base_path +  'Data/' + fileseason + '/Charts/Division/' + fileseason + '_central_pacing.jpg', bbox_inches='tight', pad_inches=0.2)

print('Finished points pace plot for: Central Division')

ANA_pointspace_chart = ANA_schedule_df.plot(x='SEQUENCE', y='DEVIATION', label='ANA', color = '#F95602')
ARI_pointspace_chart = ARI_schedule_df.plot(x='SEQUENCE', y='DEVIATION', label='ARI', color = '#8C2633', ax=ANA_pointspace_chart)
CGY_pointspace_chart = CGY_schedule_df.plot(x='SEQUENCE', y='DEVIATION', label='CGY', color = '#B72B35', ax=ANA_pointspace_chart)
EDM_pointspace_chart = EDM_schedule_df.plot(x='SEQUENCE', y='DEVIATION', label='EDM', color = '#041E41', ax=ANA_pointspace_chart)
LAK_pointspace_chart = LAK_schedule_df.plot(x='SEQUENCE', y='DEVIATION', label='LAK', color = '#000000', ax=ANA_pointspace_chart)
SJS_pointspace_chart = SJS_schedule_df.plot(x='SEQUENCE', y='DEVIATION', label='SJS', color = '#006D75', ax=ANA_pointspace_chart)
VAN_pointspace_chart = VAN_schedule_df.plot(x='SEQUENCE', y='DEVIATION', label='VAN', color = '#008852', ax=ANA_pointspace_chart)
VGK_pointspace_chart = VGK_schedule_df.plot(x='SEQUENCE', y='DEVIATION', label='VGK', color = '#B4975A', ax=ANA_pointspace_chart)

twentyover_x, twentyover_y = [-1,83],[0,20]
tenover_x, tenover_y = [-1,83],[0,10]
basepace_x, basepace_y = [-1,83],[0,0]
tenunder_x, tenunder_y = [-1,83],[0,-10]
twentyunder_x, twentyunder_y = [-1,83],[0,-20]
twentyover_pace = plt.plot(twentyover_x, twentyover_y, marker = 'o', linestyle = '--', color = 'green', alpha=0.25)
tenover_pace = plt.plot(tenover_x, tenover_y, marker = 'o', linestyle = '--', color = 'green', alpha=0.25)
basepace = plt.plot(basepace_x, basepace_y, marker = 'o', linestyle = '--', color = 'black', alpha=0.25)
tenunder_pace = plt.plot(tenunder_x, tenunder_y, marker = 'o', linestyle = '--', color = 'red', alpha=0.25)
twentyunder_pace = plt.plot(twentyunder_x, twentyunder_y, marker = 'o', linestyle = '--', color = 'red', alpha=0.25)
plt.text(85, 19, '20-over', fontsize=12, color='green', alpha=0.5)
plt.text(85, 9, '10-over', fontsize=12, color='green', alpha=0.5)
plt.text(85, -1, '96 pts', fontsize=12, color='black', alpha=0.5)
plt.text(85, -11, '10-under', fontsize=12, color='red', alpha=0.5)
plt.text(85, -21, '20-under', fontsize=12, color='red', alpha=0.5)

plt.title('Pacific Division Playoffs Pacing')
plt.xlabel('Games Played')
plt.ylabel('')
plt.xlim(0,82)

ax = plt.subplot(111)
ax.spines["top"].set_visible(False)    
ax.spines["bottom"].set_visible(False)    
ax.spines["right"].set_visible(False)    
ax.spines["left"].set_visible(False)  

plt.tick_params(axis="both", which="both", bottom="off", top="off", labelbottom="on", left="off", right="off", labelleft="off") 

ax.legend_.remove()

ANA_x_pos = ANA_schedule_df.SEQUENCE.iat[-1] + 1
ANA_y_pos = ANA_schedule_df.DEVIATION.iat[-1] - 0.5
plt.text(ANA_x_pos, ANA_y_pos, 'ANA', fontsize=12, color='#F95602')
ARI_x_pos = ARI_schedule_df.SEQUENCE.iat[-1] + 1
ARI_y_pos = ARI_schedule_df.DEVIATION.iat[-1] - 0.5
plt.text(ARI_x_pos, ARI_y_pos, 'ARI', fontsize=12, color='#8C2633')
CGY_x_pos = CGY_schedule_df.SEQUENCE.iat[-1] + 1
CGY_y_pos = CGY_schedule_df.DEVIATION.iat[-1] - 0.5
plt.text(CGY_x_pos, CGY_y_pos, 'CGY', fontsize=12, color='#B72B35')
EDM_x_pos = EDM_schedule_df.SEQUENCE.iat[-1] + 1
EDM_y_pos = EDM_schedule_df.DEVIATION.iat[-1] - 0.5
plt.text(EDM_x_pos, EDM_y_pos, 'EDM', fontsize=12, color='#041E41')
LAK_x_pos = LAK_schedule_df.SEQUENCE.iat[-1] + 1
LAK_y_pos = LAK_schedule_df.DEVIATION.iat[-1] - 0.5
plt.text(LAK_x_pos, LAK_y_pos, 'LAK', fontsize=12, color='#000000')
SJS_x_pos = SJS_schedule_df.SEQUENCE.iat[-1] + 1
SJS_y_pos = SJS_schedule_df.DEVIATION.iat[-1] - 0.5
plt.text(SJS_x_pos, SJS_y_pos, 'SJS', fontsize=12, color='#006D75')
VAN_x_pos = VAN_schedule_df.SEQUENCE.iat[-1] + 1
VAN_y_pos = VAN_schedule_df.DEVIATION.iat[-1] - 0.5
plt.text(VAN_x_pos, VAN_y_pos, 'VAN', fontsize=12, color='#008852')
VGK_x_pos = VGK_schedule_df.SEQUENCE.iat[-1] + 1
VGK_y_pos = VGK_schedule_df.DEVIATION.iat[-1] - 0.5
plt.text(VGK_x_pos, VGK_y_pos, 'VGK', fontsize=12, color='#B4975A')

#plt.style.use('ggplot')

#plt.show()
plt.savefig(base_path +  'Data/' + fileseason + '/Charts/Division/' + fileseason + '_pacific_pacing.jpg', bbox_inches='tight', pad_inches=0.2)

print('Finished points pace plot for: Pacific Division')
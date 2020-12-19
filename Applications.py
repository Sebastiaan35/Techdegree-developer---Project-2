import constants
import pprint
import sys

TEAMS2 = constants.TEAMS
PLAYERS2 = []
DicTemp = {}
TeamEx = {}
TeamExp = {}
TeamInExp = {}

def clean_data():
#Prepare a local and cleaned up copy of the teams and players CONSTANTS data (PLAYERS2) & deduce TeamEx (Teams divided equally by experience)
    for player in constants.PLAYERS:
        DicTemp = {}
        v3 = []
        for k,v in player.items():
            if k == 'guardians':
                if ' and ' in v:
                    v3 = v.split(' and ')
                else:
                    v3.append(v)
                v2 = v3
            elif k == 'height':
                v2 = int(v.replace(' inches',''))
            elif k == 'experience':
                if v == 'YES':
                    v2 = True
                elif v == 'NO':
                    v2 = False
            else:
                v2 = v
            DicTemp[k] = v2
        PLAYERS2.append(DicTemp)
    #pprint.pprint(PLAYERS2)


def balance_teams():
    i = 0
    j = 0 
    for player in PLAYERS2:
        for k,v in player.items():
            if k == 'experience':
                #Prepare dictionaries of teams and players
                #(gradually add more experienced and inexperience players to the teams)
                #TeamEx has the balanced teams
                #TeamExp has the teams with only experienced players
                #TeamInExp has the teams with only inexperienced players
                if v:
                    TeamEx.setdefault(TEAMS2[i], []).append(player['name'])
                    #Create a dictionary of experienced players
                    TeamExp.setdefault(TEAMS2[i], []).append(player['name'])
                    i += 1
                    if i == 3:
                        i = 0
                else:
                    TeamEx.setdefault(TEAMS2[j], []).append(player['name'])
                    #Create a dictionary of inexperienced players
                    TeamInExp.setdefault(TEAMS2[j], []).append(player['name'])
                    j += 1
                    if j == 3:
                        j = 0

def Menu1():
    print('\n---- MENU----\n\n Here are your choices: \n\
        1) Display Team Stats\n\
        2) Quit')

def GetInput(Max):
    #This function is for making sure the user provides valid input
    InvalidEntryMsg = "Sorry, I didn't get you there. Could you please enter a valid number?"
    while True:
        try:
            inp = int(input('\nEnter an option > '))
            Temppp = Max + 1
            if 0 < inp < (Max + 1):
                return inp
            else:
                print(InvalidEntryMsg)
        except:
            print(InvalidEntryMsg)


#In order to prevent that code runs when this file is imported I add this dundermain
if __name__ == "__main__":
    print("BASKETBALL TEAM STATS TOOL\n\nBy Sebastiaan van Vugt\n\nDisclaimer: I'm going to assume that the total number of players and \
their experience can be perfectly divided over the different teams (i.e. no remainders)\n")

    clean_data()
    balance_teams()

    while True:
        Menu1()
        
        #get & process first choice
        inp = GetInput(2)
        if inp == 1:
            for number, team in enumerate(TEAMS2):
                print(str(number + 1) + ')', team)
        elif inp == 2:
            sys.exit()
            
        #get & process second choice
        inp = GetInput(len(TEAMS2))

        #get list of players of chosen team and convert to string
        ChosenTeam = (TeamEx[TEAMS2[inp-1]])
        ChosenTeamExp = len(TeamExp[TEAMS2[inp-1]])
        ChosenTeamInExp = len(TeamInExp[TEAMS2[inp-1]])
        
        AllPlayersStri = ''
        TeamHeightTot = 0
        AllGuardians  = []

        AllPlayersStri = ', '.join(ChosenTeam)

        for player in ChosenTeam:
            for player2 in PLAYERS2:
                for k,v in player2.items():
                    if k == 'name' and v == player:
                        add = True
                    elif k == 'name' and v != player:
                        add = False
                    elif k == 'height':
                        HeightTemp = v
                    elif k == 'guardians':
                        GuardianTemp = v
                if add:
                    for guardian in GuardianTemp:
                            if guardian not in AllGuardians:
                                AllGuardians.append(guardian)
                    TeamHeightTot += HeightTemp

        AllGuardiansStri = ', '.join(AllGuardians)
        TeamHeightAvg = round(TeamHeightTot/ len(ChosenTeam),1)

        print('\nTeam: {} Stats'.format(TEAMS2[inp-1]))
        print('--------------------')
        print('Total players:', len(ChosenTeam))
        print('Total experienced: {}'.format(ChosenTeamExp))
        print('Total inexperienced: {}'.format(ChosenTeamInExp))
        print('Average height: {}'.format(TeamHeightAvg),'\n')
        
        print('\nPlayers on Team:\n{}\n'.format(AllPlayersStri))
        print('Guardians:\n {}'.format(AllGuardiansStri))
        
        input('\nPress ENTER to continue...')

sys.exit()



__author__ = 'gamargam'

# first file
import json
import sys
import scrapy
import prettytable


print "Hello world"

json_string = '{"first_name": "Guido", "last_name":"Rossum"}'
new_dict1 = {"first_name1": "Guido1", "Last_name1": "Rossum1"}

# json_string = '{ "away": "TEN","day": 3,"eid": "2016010305","gamekey": "56752","home": "IND","month": 1,"season_type": "REG","time": "1:00","wday": "Sun","week": 17,"year": 2015}'
parsed_json = json.loads(json_string)
print(parsed_json['first_name'])
print(new_dict1["first_name1"])
global home_team
global away_team

# Week 1 schedule - Aug 11

'''
week1_games = {"game1_away": "PIT", "game1_home": "NE", "game2_away": "GB", "game2_home": "CHI",
               "game3_away": "KC", "game3_home": "HOU", "game4_away": "CLE", "game4_home": "NYJ",
               "game5_away": "IND", "game5_home": "BUF", "game6_away": "MIA", "game6_home": "WAS",
               "game7_away": "CAR", "game7_home": "JAX", "game8_away": "SEA", "game8_home": "STL",
               "game9_away": "NO", "game9_home": "ARI", "game10_away": "DET", "game10_home": "SD",
               "game11_away": "TEN", "game11_home": "TB", "game12_away": "CIN", "game12_home": "OAK",
               "game13_away": "BAL", "game13_home": "DEN", "game14_away": "NYG", "game14_home": "DAL",
               "game15_away": "PHI", "game15_home": "ATL", "game16_away": "MIN", "game16_home": "SF"
               }
'''

week1_games = {"game1_away": "PIT", "game1_home": "NE", "game2_away": "GB", "game2_home": "CHI",
               "game3_away": "KC", "game3_home": "HOU", "game4_away": "CLE", "game4_home": "NYJ",
               }


# print(week1_games["game16_home"])

# Display formatting - Aug 12
# print(sorted(week1_games.keys()))
# print(len(week1_games))
# print(week1_games.values())

# Comments:
# start for loop
# first pass assign value to temp_var_1
# second pass assign next value to temp_var_2
# print these values and continue with for loop

global i
i = 1

print '\n WEEK 1 NFL SCHEDULE'
print '========================\n'
print '----------------'
print "\n This Program is about Projecting Scores and Comparing Scores from Week #1 NFL \n"

from prettytable import PrettyTable
global table
table = PrettyTable(["Away Team", "Home Team"])

for key_val in sorted(week1_games.iterkeys()):  # i = week1_games[key_val]
    if i == 1:
        away_team = week1_games[key_val]
        i += 1
    elif i == 2:
        home_team = week1_games[key_val]
        i = 1

        #print ("| {} | v/s | {} |".format(away_team, home_team))
        #print '----------------'

        table.add_row([away_team, home_team])

print table

# Aug 25 - No clean-up attempted. Still struggling with basics on Input, Display

home_list = []
away_list = []
counter = 0

score_table = PrettyTable(["Away Team", "Away Est. Score", "Home Team", "Home Est. Score"])

for key_val in sorted(week1_games.iterkeys()):  # i = week1_games[key_val]

    if i == 1:
        away_team = week1_games[key_val]
        i += 1
    elif i == 2:
        home_team = week1_games[key_val]
        i = 1

        #print ' %s \t v/s \t %s \n' % (away_team, home_team)
        # Attempting str.format() instead of % string formatting literal - Aug 18
        #print ("| {} | v/s | {} |".format(away_team, home_team))
        #print '----------------'
        #print "Enter Home Team's score:  " - Aug 19
        #print "Enter %s (home team) projected score" % home_team - Aug 26

        counter += 1
        print "\n Game # ", counter
        print "============"

        print("\n Enter home team score {} ".format(home_team)),
        # Exception handling required for input function
        try:
            temp_home_score = int(input(": "))
        except SyntaxError:
            print("\nPlease only use integers")
            raise
        home_list.append(temp_home_score)

        print(" Enter away team score {} ".format(away_team)),

        # Basic exception handling - Sep 5
        try:
            temp_away_score = int(input(": "))
        except SyntaxError:
            print('\nYOU DID NOT ENTER A VALUE ... ENTER AN INTEGER for AWAY TEAM \n')
            raise
        away_list.append(temp_away_score)
        score_table.add_row([away_team, temp_away_score, home_team, temp_home_score])


print '\n'

print score_table

print "Work In Progress...\n"

#print home_list
#print away_list

print (sys.version)
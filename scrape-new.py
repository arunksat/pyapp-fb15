
__author__ = 'gamargam'


import requests
from bs4 import BeautifulSoup
from prettytable import PrettyTable

url = 'http://www.nfl.com/scores'
url_pre = 'http://www.nfl.com/scores/2015/PRE4'
url_reg = 'http://www.nfl.com/scores/2015/REG1'
#response = requests.get(url_reg)
#html = response.content
#soup = BeautifulSoup(html, "lxml")

soup = BeautifulSoup(open("week10-scores.html").read(), "lxml")
print type(soup)
soup.prettify()
print soup.title.string

global table
score_table = PrettyTable(["Away Team", "Away Actual Score", "Home Team", "Home Actual Score"])

f_project = open("nfl2015-scores.txt", "a")
print "Name of the file: ", f_project.name

link_away = soup.findAll('div', {"class" : ['away-team']})
link_home = soup.findAll('div', {"class" : ['home-team']})

#for link_val1 in link_away and for link_val2 in link_home:
for link_val1, link_val2 in zip(link_away, link_home):
    divlinks_name1 = link_val1.findAll('p', {'class' : 'team-name'})
    away_team = divlinks_name1[0].get_text()
    divlinks_score1 = link_val1.findAll('p', {'class' : 'total-score'})
    temp_away_score = str(divlinks_score1[0].get_text())
    divlinks_name2 = link_val2.findAll('p', {'class' : 'team-name'})
    home_team = divlinks_name2[0].get_text()
    divlinks_score2 = link_val2.findAll('p', {'class' : 'total-score'})
    temp_home_score =  str(divlinks_score2[0].get_text())
    score_table.add_row([away_team, temp_away_score, home_team, temp_home_score])

print score_table
#f_project.write(score_table)


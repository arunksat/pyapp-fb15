
__author__ = 'gamargam'


import requests
#from BeautifulSoup import BeautifulSoup
from bs4 import BeautifulSoup

url = 'http://www.nfl.com/scores'
url_pre = 'http://www.nfl.com/scores/2015/PRE4'
url_reg = 'http://www.nfl.com/scores/2015/REG1'
response = requests.get(url_reg)
html = response.content
soup = BeautifulSoup(html, "lxml")
print type(soup)

print soup.title.string

#sibling_soup.b.next_sibling

# Testing code.

#for td in soup.select('div class > p class > p class:nth-of-type(2)'):
#    print td.text
#    print "hello inside"


#table = soup.find('div', attrs={'class': 'scorebox-wrapper'}) #this statement works
#table = soup.findAll(['div', 'p ']) # this also works
#table = soup.findAll(['div', 'p'])
#table = soup.find_all('div', class_='scorebox-wrapper')

#print type(table)
#print table

#manga_img = soup.findAll ('a', {'class' : 'manga_img'}, limit=None)
#2 for loops: one for team name and one for total-score

#for row in soup.find_all("p", attrs={"class": "team-name"}):
#    print row.prettify()

#for row in soup.findAll('p', {'class': 'team-name'}, limit=None): #prints scores alone# #
#   print row.prettify()

#rank = soup.find("div", {"class": "team-name"}).p.contents


#teaminfo = soup.find("p", {"class": "team-name"}).contents
#score = soup.find("p", {"class": "total-score"}).contents
#print teaminfo
#print score

#rating = teaminfo.p.contents
#print rating


#for row in soup.findAll(True, {"class":["team-name", "total-score"]}):
#    print row.prettify()

total_score = len(soup.findAll(True, {"class" : ["team-name"]}))
print int(total_score)

for num in [2,3]:
    print soup.select('.team-name')[num].contents[0]
    print soup.select('.total-score')[num].contents[0]


#for title in soup.findAll('p', {'class': 'team-name'}, limit=None):
#    print title

count = 0


link = soup.findAll('div', {"class" : ['home-team']})

for link_val in link:
    divlinks = link_val.findAll('p', {'class' : 'team-name'})
    for divlink_val in divlinks:
        team_url = divlink_val.find('a', href=True)['href']
        print team_url

print "+++++++++++++++++"
print "-----------------"
print "+++++++++++++++++"


linknew = soup.findAll('div', {"class" : ['home-team']})

for link_newval in linknew:
    divnewlinks = link_newval.findAll('p', {'class' : 'total-score'})
    print divnewlinks

print "+++++++++++++++++"
print "-----------------"
print "+++++++++++++++++"

link = soup.findAll('div', {"class" : ['away-team']})

for link_val in link:
    divlinks = link_val.findAll('p', {'class' : 'team-name'})
    for divlink_val in divlinks:
        team_url = divlink_val.find('a', href=True)['href']
        print team_url

print "+++++++++++++++++"
print "-----------------"
print "+++++++++++++++++"


linknew = soup.findAll('div', {"class" : ['away-team']})

for link_newval in linknew:
    divnewlinks = link_newval.findAll('p', {'class' : 'total-score'})
    print divnewlinks

print "+++++++++++++++++"
print "-----------------"
print "+++++++++++++++++"


scores = soup.select('.total-score')
print scores

print scores[1].contents[0]
print scores[2].contents[0]
print scores[4].contents[0]
print scores[5].contents[0]


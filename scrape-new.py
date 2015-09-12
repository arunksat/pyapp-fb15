__author__ = 'gamargam'


import requests
from BeautifulSoup import BeautifulSoup

url = 'http://www.nfl.com/scores'
url_pre = 'http://www.nfl.com/scores/2015/PRE4'
response = requests.get(url_pre)
html = response.content
soup = BeautifulSoup(html)
print type(soup)

#table = soup.find('div', attrs={'class': 'scorebox-wrapper'}) #this statement works
#table = soup.findAll(['div', 'p ']) # this also works
#table = soup.findAll(['div', 'p'])
#table = soup.find_all('div', class_='scorebox-wrapper')

#print type(table)
#print table

#manga_img = soup.findAll ('a', {'class' : 'manga_img'}, limit=None)
#2 for loops: one for team name and one for total-score

for row in soup.findAll('p', {'class': 'total-score'}, limit=None): #prints scores alone
#for row in soup.findAll('p', {'class': 'new-score-box'}, limit=None): #this does not work
   print row.prettify()
#   for cell in row.findAll('total-score'):
#      print cell.prettify()
import requests
from bs4 import  BeautifulSoup
import pprint
Url=get('https://news.ycombinator.com/news')
res =requests.Url
#print(res.text)
soup =BeautifulSoup(res.text,'html.parser')
links=soup.select('.titleline')
#votes= soup.select('.score')
subtext= soup.select('.subtext')
#print(votes[0])
def sort_stories_by_votes(hnlist):
	return sorted(hnlist,key=lambda k:k['vote'],reverse=True)

def create_custom_hn(links,subtext):
	hn= []
	for idx,item in enumerate(links):
		title = links[idx].getText()
		href = links[idx].get('href',None)
		vote = subtext[idx].select('.score')
		if len(vote):
		    points = int(vote[0].getText().replace(' points',''))
		    if points > 99:
		   #print(points)
		      hn.append({'title':title,'link':href,'vote':points})
	return sort_stories_by_votes(hn)

pprint.pprint(create_custom_hn(links,subtext))
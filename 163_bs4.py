#-*- coding:utf8 -*-
import urllib2
from bs4 import BeautifulSoup as bs

url='http://goal.sports.163.com/39/stat/standings/2016_3.html'
url_doc=urllib2.urlopen(url).read()
html=bs(url_doc,"html.parser")
#html=bs(open('/tmp/pl.html'),"html.parser")
table=html.table
tr=table.find_all('tr')
rank=['排名']
club=['球队']
rounds=['场次']
wins=['胜']
draws=['平']
loses=['负']
gs=['进球']
gc=['失球']
gd=['净胜球']
points=['积分']
for i in tr[1:21]:
	td=i.find_all('td')
	rank.append(td[0].string.encode('utf8'))
	club.append(td[1].string.encode('utf8'))
	rounds.append(td[2].string.encode('utf8'))
	wins.append(td[3].string.encode('utf8'))
	draws.append(td[4].string.encode('utf8'))
	loses.append(td[5].string.encode('utf8'))
	gs.append(td[6].string.encode('utf8'))
	gc.append(td[7].string.encode('utf8'))
	gd.append(td[8].string.encode('utf8'))
	points.append(td[10].string.encode('utf8'))
for i in range(21):
	if club[i] == '托特纳姆热刺':
		club[i]='热刺'
	if club[i] == '米德尔斯堡':
		club[i]='米堡'

for i in range(21):
	if len(club[i]) < 10:
		print rank[i]+'\t'+club[i]+'\t\t'+points[i]+'\t'+rounds[i]+'\t'+wins[i]+'\t'+draws[i]+'\t'+loses[i]+'\t'+gs[i]+'\t'+gc[i]+'\t'+gd[i]
	if len(club[i]) > 10:
		print rank[i]+'\t'+club[i]+'\t'+points[i]+'\t'+rounds[i]+'\t'+wins[i]+'\t'+draws[i]+'\t'+loses[i]+'\t'+gs[i]+'\t'+gc[i]+'\t'+gd[i]

#for i in range(21):
#	print club[i],len(club[i])

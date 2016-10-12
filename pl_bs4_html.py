import urllib2
from bs4 import BeautifulSoup

url='https://www.premierleague.com/tables'
html=urllib2.urlopen(url).read()
soup=BeautifulSoup(html,"lxml")
#soup=BeautifulSoup(open('/tmp/premier'),"lxml")

table=soup.table
title=table.summary.string
print title
#temp_clubnames=table.find_all(attrs={"class":"team"})
#for i in temp_clubnames:
#    if len(i.contents) == 1:
#        #print temp_string
#        clubnames.append(i.string.encode('utf8'))
#    else:
#        print i.a.contents[-2].string
#        clubnames.append(i.a.contents[-2].string.encode('utf8'))
#print clubnames
result=table.find_all('tr',attrs={"data-compseason":"54"})
clubnames=['Club']
rounds=['rounds']
wins=['wins']
loses=['loses']
draws=['draws']
gs=['gs']
gc=['gc']
points=['points']
rank=['rank']
for i in result:
    td=i.find_all('td')
    clubnames.append(td[2].a.contents[-1].string.encode('utf8'))
    rounds.append(td[3].string.encode('utf8'))
    wins.append(td[4].string.encode('utf8'))
    draws.append(td[5].string.encode('utf8'))
    loses.append(td[6].string.encode('utf8'))
    gs.append(td[7].string.encode('utf8'))
    gc.append(td[8].string.encode('utf8'))
    points.append(td[10].string.encode('utf8'))
for i in range(21):
    rank.append(i+1)
    if i == 0:
        print str(rank[i])+'\t'+clubnames[i]+'\t'+points[i]+'\t'+wins[i]+'\t'+draws[i]+'\t'+loses[i]+'\t'+gs[i]+'\t'+gc[i]+'\t'+'gd'
    if i > 0:
        print str(rank[i])+'\t'+clubnames[i]+'\t'+points[i]+'\t'+wins[i]+'\t'+draws[i]+'\t'+loses[i]+'\t'+gs[i]+'\t'+gc[i]+'\t'+str(int(gs[i])-int(gc[i]))

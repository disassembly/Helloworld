#! /usr/bin/python
# -*- coding: utf-8 -*-
import argparse
import fileinput
import locale
import re
import sys

class MatchResult(object):
    """Soccer match result."""
    def __init__(self, line):
        """Parse a match result string into teams and scores."""
        self.teams = ()
        self.scores = ()
        for teamResult in line.split(','):
            self.teams += re.search("(\S+.*?)\s+\d+\s*$", teamResult).group(1),
            self.scores += int(re.search("(\d+)\s*$", teamResult).group(1)),

class Wins(object):
    def _record_win(self, team):
        self.teams[team] += 1

    def __init__(self):
        self.teams = {}

    def record_result(self, result):
        """Update the table's teams and their points based on a match result."""
        for name in result.teams:
            if name not in self.teams:
                self.teams[name] = 0
        team1, team2 = result.teams
        score1, score2 = result.scores
        if score1 > score2:
			self._record_win(team1)
        elif score1 < score2:
			self._record_win(team2)
        return self.teams

class Loses(object):
    def _record_lose(self, team):
        self.teams[team] += 1

    def __init__(self):
        self.teams = {}

    def record_result(self, result):
        """Update the table's teams and their points based on a match result."""
        for name in result.teams:
            if name not in self.teams:
                self.teams[name] = 0
        team1, team2 = result.teams
        score1, score2 = result.scores
        if score1 > score2:
			self._record_lose(team2)
        elif score1 < score2:
			self._record_lose(team1)
        return self.teams

class Draws(object):
    def _record_draw(self, team):
        self.teams[team] += 1

    def __init__(self):
        self.teams = {}

    def record_result(self, result):
        """Update the table's teams and their points based on a match result."""
        for name in result.teams:
            if name not in self.teams:
                self.teams[name] = 0
        team1, team2 = result.teams
        score1, score2 = result.scores
        if score1 == score2:
            self._record_draw(team1)
            self._record_draw(team2)
        return self.teams

class GoalS(object):
    def __init__(self):
        self.teams = {}

    def record_result(self, result):
        """Update the table's teams and their points based on a match result."""
        for name in result.teams:
            if name not in self.teams:
                self.teams[name] = 0
        team1, team2 = result.teams
        score1, score2 = result.scores
        self.teams[team1] += score1
        self.teams[team2] += score2
        return self.teams

class GoalC(object):
    def __init__(self):
        self.teams = {}

    def record_result(self, result):
        """Update the table's teams and their points based on a match result."""
        for name in result.teams:
            if name not in self.teams:
                self.teams[name] = 0
        team1, team2 = result.teams
        score1, score2 = result.scores
        self.teams[team1] += score2
        self.teams[team2] += score1
        return self.teams


def get_input():
    """Do arg parsing. Return generator for input lines."""
    parser = argparse.ArgumentParser(description='Output the ranking table for a soccer league.')
    parser.add_argument(
        'file', nargs='?', help=(
            "File containing match results. If not specified, "
            "the same format is expected via standard input pipe. "
            "See README.md for format details."
        ))

    args = parser.parse_args()
    if args.file:
        def lineGenerator():
            with open(args.file) as f:
                for line in f:
                    yield line
        return lineGenerator()
    elif not sys.stdin.isatty():
        return (line for line in fileinput.input())
    else:
        parser.print_help()
        exit()

def merge_dict(dict1,dict2):
	newdict={}
	for k,v in dict1.items():
			newdict[k]=v
	for k,v in dict2.items():
		if k in newdict.keys():
			newdict[k] +=v
		else:
			newdict[k]=v
	return newdict

def minus_dict(dict1,dict2):
	newdict={}
	for k,v in dict1.items():
			newdict[k] = v
	for k,v in dict2.items():
		if k in newdict.keys():
			newdict[k] -= v
		else:
			newdict[k] = -v
	return newdict

def count_scores(dict1,dict2):
	newdict={}
	for k,v in dict1.items():
			newdict[k] =  v
	for k,v in dict2.items():
		if k in newdict.keys():
			newdict[k] += 3 * v
		else:
			newdict[k] += 3*v
	return newdict

wins={}
draws={}
loses={}
goals={}
goalc={}
for line in get_input():
	matchresult=MatchResult(line)
	winresult=Wins()
	drawresult=Draws()
	loseresult=Loses()
	goalsresult=GoalS()
	goalcresult=GoalC()
	wins=merge_dict(wins,winresult.record_result(matchresult))
	loses=merge_dict(loses,loseresult.record_result(matchresult))
	draws=merge_dict(draws,drawresult.record_result(matchresult))
	goals=merge_dict(goals,goalsresult.record_result(matchresult))
	goalc=merge_dict(goalc,goalcresult.record_result(matchresult))

goald=minus_dict(goals,goalc)
scores=count_scores(draws,wins)
roundn=merge_dict(wins,merge_dict(draws,loses))
table=[]
for teamname in scores:
	table += [{'teamname':teamname,'score':scores[teamname],'rounds':roundn[teamname],'wins':wins[teamname],'draws':draws[teamname],'loses':loses[teamname],'goals':goals[teamname],'goalc':goalc[teamname],'goald':goald[teamname]}]
for i in range(0,len(table)):
	for j in range(i,len(table)):
		if table[j]['score'] > table[i]['score']:
			rank=table[i]
			table[i]=table[j]
			table[j]=rank
		elif table[j]['score'] == table[i]['score'] and table[j]['goald'] > table[i]['goald']:
			rank=table[i]
			table[i]=table[j]
			table[j]=rank
		elif table[j]['score'] == table[i]['score'] and table[j]['goald'] == table[i]['goald'] and table[j]['goals'] > table[i]['goals']:
			rank=table[i]
			table[i]=table[j]
			table[j]=rank
print u'排名\t球队\t\t积分\t场次\t胜\t平\t负\t进球\t失球\t净胜球'.encode('utf8')
for i in range(0,len(table)):
	if len(table[i]['teamname']) > 9 :
		print str(i+1)+'\t'+table[i]['teamname']+'\t'+str(table[i]['score'])+'\t'+str(table[i]['rounds'])+'\t'+str(table[i]['wins'])+'\t'+str(table[i]['draws'])+'\t'+str(table[i]['loses'])+'\t'+str(table[i]['goals'])+'\t'+str(table[i]['goalc'])+'\t'+str(table[i]['goald'])
	else:
		print str(i+1)+'\t'+table[i]['teamname']+'\t\t'+str(table[i]['score'])+'\t'+str(table[i]['rounds'])+'\t'+str(table[i]['wins'])+'\t'+str(table[i]['draws'])+'\t'+str(table[i]['loses'])+'\t'+str(table[i]['goals'])+'\t'+str(table[i]['goalc'])+'\t'+str(table[i]['goald'])

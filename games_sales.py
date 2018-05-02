#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

months = {"Jan" : 1, "Feb" : 2, "Mar" : 3, "Apr" : 4, "May" : 5, "Jun" : 6,
          "Jul" : 7, "Aug" : 8, "Sep" : 9, "Oct" : 10, "Nov" : 11, "Dec" : 12}

def fs(sales):
    if sales != "N/A":
        return float(sales[:-1])
    else:
        return None

def fg(genre):
    if genre == "None":
        return None
    else:
        return genre

def fc(score):
    if score != "N/A":
        return float(score)
    else:
        return None

def fd(date):
    if date != "N/A":
        d,m,y = date.split()
        d = int(d[:-2])
        m = months[m]
        if y > "30":
            y = 1900 + int(y)
        else:
            y = 2000 + int(y)
        return (y,m,d)
    else:
        return None

games = list()
a = open("Game_Sales.csv")
header = False
for line in a:
    if header:
        line = line.strip().split(',')
        name = line[1].decode("utf-8")
        name = name.encode("ascii","ignore")
        games.append((name,line[2],line[3],fg(line[4]),fc(line[5]),fs(line[6]),fs(line[7]),fs(line[8]),fs(line[9]),fd(line[10])))
    else:
        header = True

random.shuffle(games)
aux_games = list()
sales = dict()
for i,g in enumerate(games):
    aux_games.append((i,g[0],g[1],g[2],g[3],g[4],g[9]))
    sales[i] = (g[5],g[6],g[7],g[8])

games = aux_games

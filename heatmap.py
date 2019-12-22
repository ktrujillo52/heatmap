#!/usr/bin/python
#Global trade analysis WITS data 

import pandas as pd
import os
import networkx as nx
import csv
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.axes_grid1 import make_axes_locatable
from matplotlib import pyplot, patches
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
# -*- coding: iso-8859-15 -*-

#Plotly credentials
plotly.tools.set_credentials_file(username='username', api_key='key')


#Change directory
os.chdir("../data/wits_summary_10")
#Get directory
path = os.getcwd()
#Get contents of directory
contents = []
tot = os.listdir(path)
for item in tot:
	contents.append(item)
#Read CSV
#Create array and dictionary
countries = []
data = []
count = 0
#Create a directed graph called G
G = nx.DiGraph()
for item in contents:
	with open(item, "r+") as f:
		#text = pd.read_csv(csv)
		text = csv.reader(f)
		#Read all countries into array
		for row in text:
			print row
			if (row[0] not in countries):
				countries.append(row[0])
		f.close()

for item in contents:
	with open(item, "r+") as f:
		text = csv.reader(f)
		#Collect all data
		for row in text:
			data.append(row)
		
		count += 1
		f.close()		
#Build dictionary
dic = {}
for i in countries:
	dic[i] = {key : float(0) for key in countries}

for i in data:
	if (str(i[0]) in countries):
				if (i[1] in countries):
					if (str(i[2]) == "All Products"):
						try:					
							dic[i[0]][i[1]] += float(i[5])	
						except:
							print "Error"
						#print dic[i[0]][i[1]]
#Test
"""Check to see if all files opened"""
print "Length contents:"+str(len(contents))
print "Opened: "+str(count)



#Generate heatmap with categorical axis labels
country = []
partner = []
trade = []

k = 0

while (k < len(dic)):
	array = []
	trade.append(array)
	k += 1
k = 0
while (k < len(dic)):
	for i in dic:
		for j in dic[i]:
			trade[k].append(dic[i][j])
		k += 1


trace = go.Heatmap(z=trade, x=countries, y=countries)

data = [trace]
py.iplot(data, filename='labelled-heatmap')

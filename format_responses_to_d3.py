import csv
import pandas as pd
import numpy as np
import json


df 			= pd.read_csv("survey-responses.csv")
qnos 		= df.columns[10:26]
questions 	= df.loc[0, "Q13":"Q29"]
responses 	= df.loc[1:,"Q13":"Q29"]

labels = ["Minimum wage", "Transgender rights", "Marijuana legalization", "University policy", "Healthcare", "Mandatory minimum sentence", "Iran deal", "TPP", "Assault weapons", "Voter IDs", "Affirmative action", "Refugees", "Energy", "Israel", "Saudi Arabia", "Divestment"]

for i,qno in enumerate(qnos):
	data = list(responses.loc[:,qno])
	histogram = np.histogram(data, bins=[1,2,3,4,5,6])
	print questions[i]
	print labels[i]
	with open(labels[i]+".tsv", "w+") as f:
		f.write("opposition level\tcount\n")
		for i,(count, level) in enumerate(zip(histogram[0], histogram[1])):
			f.write("%i\t%i\n" %(i+1, count))


print json.dumps(dict(zip(labels, questions)), indent=2)



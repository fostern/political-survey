import csv
import pandas as pd
import numpy as np
import json


labels = ["Minimum wage", "Transgender rights", "Marijuana legalization", "University policy", "Healthcare", "Mandatory minimum sentence", "Iran deal", "TPP", "Assault weapons", "Voter IDs", "Affirmative action", "Refugees", "Energy", "Israel", "Saudi Arabia", "Divestment"]


for label in labels:
	with open(label+".tsv", "r") as f:
		tsvin = csv.reader(f, delimiter='\t')
		count = 0
		for i,row in enumerate(tsvin):
			print row
			if i != 0:
				count += int(row[1])
		f.seek(0)
		tsvin2 = csv.reader(f, delimiter='\t')

		with open(label+"1.tsv", "w") as f2:
			tsvout = csv.writer(f2, delimiter='\t')

			for j,row in enumerate(tsvin2):
				print row
				if j == 0:
					tsvout.writerow(row)
				else:
					tsvout.writerow([row[0], (int(row[1])/float(count)) * 100 ])


		

		



import pickle
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd


class recommend:
	def __init__(self):
		self.df = pd.read_csv('data.csv')
		self.df.fillna(2,inplace=True)
		self.features = self.df.iloc[:,2:].values
		self.features = list(self.features)
		# print(features.head())
		self.events = pickle.load(open('events.pickle','rb'))
		self.domains = pickle.load(open('domains.pickle','rb'))
		self.evs = []
		self.dom = None
		# s = input('Enter the sentence:')

	def predict(self,s,n):

		for j in self.domains.keys():
		    if j in s:
		    	z = self.domains[j.lower()]
		    	self.evs.append(z)
		    	self.dom = j

		for i in self.events.keys():
			if i in s:
				z = self.events[i.lower()]
				self.evs.append(z)

		self.result = np.where(self.features == self.evs)[0]
		print(self.result)
		print(self.evs)
		# print(len(self.result))
		# print(self.features[0])
		if len(self.result) == 0:
			# print(self.evs)
			self.features.append(self.evs)
			self.result = -1
			similar_metrics = cosine_similarity(self.features)
			self.result = list(enumerate(similar_metrics[self.result]))
			self.result = sorted(self.result,key= lambda x: x[1],reverse=True)
			return self.result
		else:
			similar_metrics = cosine_similarity(self.features)
			self.result = np.where(self.features == self.evs)[0][0]
			print(self.result)
			self.result = list(enumerate(similar_metrics[self.result]))
			self.result = sorted(self.result,key= lambda x: x[1],reverse=True)
			return self.result

	def close(self):
		self.evs = []



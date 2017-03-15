#this module handles the cluster for each category:
#encoding=utf-8
import sys
from pprint import pprint as pprint

class data:

	def __init__ (self, path):

		#file_name=sys.argv[1]
		#file_name=file[0]
		#print file_name[-3:]
		self.data_dict={}
		if path[-3:]=='csv':
			#print 'gggggggg'
			import csv
			count=0
			with open(file_name, 'rb') as csvfile:
				reader = csv.reader(csvfile)
				count+=1
				#keys=reader.keys()
				for row in reader:
					#print len(row) 
					#if count==1: continue
					self.data_dict[row[1]]=row[2:]
				#print self.data_dict

	def get_data_by_category(self,category_name):
		temp_dict={}
		for barcode in self.data_dict:
			item=self.data_dict[barcode]
			#pprint (item[-1])
			#print 'category_name', category_name
			if category_name == item[-1]:
				#returns tuple of (price per unit, price for product):
				temp_dict[barcode]=(float(item[-4]),float(item[-5]))
		return temp_dict

def cluster(data):
	import numpy as np
	from sklearn.cluster import  KMeans
	#from sklearn.datasets.samples_generator import make_blobs
	import matplotlib.pyplot as plt

	datush= data.get_data_by_category('deodorant')

	datush_X=np.zeros((len(datush),2))
	datush_Y=np.zeros((len(datush),1))
	
	count=0
	# this is because SK-learn recieves np array:
	for key in datush:
		datush_X[count][0]=datush[key][0]
		datush_X[count][1]=datush[key][1]
		datush_Y[count][0]=key
		count+=1
	
	#X=datush_X
	
	y_pred = KMeans(n_clusters=3).fit_predict(datush_X)
	print long(datush_Y[-18]),datush_X[-18][0],datush_X[-18][1]
	
	# number of features, in our case 2:price per unit and price for product
	plt.scatter(datush_X[:, 0],datush_X[:, 1], c=y_pred)
	plt.title("Anisotropicly Distributed Blobs")
	plt.show()

if __name__ == '__main__' :
	file_name=sys.argv[1]
	data=data(file_name)
	cluster(data)


					

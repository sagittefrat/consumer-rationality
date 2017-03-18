#this module handles the cluster for each category:
#encoding=utf-8
import sys
import os
from data import Data
from pprint import pprint  
from copy import deepcopy
import csv

class Cluster:

	def __init__ (self, data,categories=None):

		self.data=data
		self.chosen_categories=('cucumber','milk','toothpaste')
		#categories is a tuple of strings
		self.categories=categories
		if self.categories==None:
			 self.categories=self.data.categories

		self.category_cluster_centers={}
		self.category_barcodes={}
		self.barcode_category={}

		for category_name in self.categories:
			pass
		self.super_name=self.data.get_super_name()


	def cluster_category(self,category_name, super_name):

		import numpy as np
		from sklearn.cluster import KMeans
		import matplotlib.pyplot as plt

		datush=self.data.get_data_by_category(category_name)

		if len(datush)<3: return np.zeros((len(datush),2))

		datush_X=np.zeros((len(datush),2))
		datush_Y=np.zeros((len(datush),1))
		
		count=0
		# this is because SK-learn recieves np array:
		for key in datush:
			datush_X[count][0]=datush[key][0]
			datush_X[count][1]=datush[key][1]
			datush_Y[count][0]=key
			count+=1

		
		y = KMeans(n_clusters=3).fit(datush_X)

		y_pred= y.predict(datush_X)
		
		#sort the centers so 0-discount, 2-premium:
		pred=[0,0,0]
		center=[ 
		[y.cluster_centers_[0][0],y.cluster_centers_[0][1],0], 
		[y.cluster_centers_[1][0],y.cluster_centers_[1][1],1],
		[y.cluster_centers_[2][0],y.cluster_centers_[2][1],2] 
		]
	
		centers=sorted(center, key=lambda t: t[0])
		for i in xrange(0,2):
			if centers[0][2]==i : pred[i]=0
			elif centers[1][2]==i: pred[i]=1
			else: pred[i]=2


		temp_dict={}
		barcode_category_dict={ }
		for i in xrange(0, len(datush_X[:,0])-1):
			temp_dict[int(datush_Y[i,0])]=(pred[y_pred[i]], datush_X[i, 0],datush_X[i, 1])
			self.barcode_category[int(datush_Y[i,0])]=(pred[y_pred[i]],category_name)
		
		
		# number of features, in our case 2:price per unit and price for product
		plt.scatter(datush_X[:, 0],datush_X[:, 1], c=y_pred,s=200)
		title=self.super_name+', category:'+category_name
		plt.title(title)
		if category_name in self.chosen_categories:
			plt.savefig(' '+title+'.png')
		self.category_cluster_centers[category_name]=y.cluster_centers_
		self.category_barcodes[category_name]=temp_dict
		

	def cluster(self,dict_x,categories=None):

		if categories==None:
			categories=self.categories

		for category_name in categories:
			#print 'category_name',category_name
			super_name=self.data.super_name
			self.cluster_category(category_name,super_name)
	

def cluster_the_supermarkets_by_category_and_position():

	super_category_cluster_centers={}

	with open('category_position_centers.csv', 'rb') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			print row
			if (row[0],row[1]) not in super_category_cluster_centers:
				super_category_cluster_centers[(row[0],row[1])]={}
			
			super_category_cluster_centers[(row[0],row[1])][row[4]]=(row[2],row[3])
			
		pprint (super_category_cluster_centers)


		import numpy as np
		from sklearn.cluster import KMeans
		import matplotlib.pyplot as plt


		for category in super_category_cluster_centers:
			#print category
			#print super_category_cluster_centers[category]
			datush=super_category_cluster_centers[category]
			if len(datush)<3: return np.zeros((len(datush),2))
			# this is because SK-learn recieves np array:
			datush_X=np.zeros((len(datush),2))
			datush_Y=np.zeros((len(datush),1))
			#print 'len(datush)',len(datush)
			count=0
			for super_name in super_category_cluster_centers[category]:
				datush_X[count][0]=super_category_cluster_centers[category][super_name][0]
				datush_X[count][1]=super_category_cluster_centers[category][super_name][1]
				datush_Y=super_name
				count+=1
		
			y = KMeans(n_clusters=3).fit(datush_X)

			y_pred= y.predict(datush_X)
			print y_pred
		
			#sort the centers so 0-discount, 2-premium:
			pred=[0,0,0]
			center=[ 
			[y.cluster_centers_[0][0],y.cluster_centers_[0][1],0], 
			[y.cluster_centers_[1][0],y.cluster_centers_[1][1],1],
			[y.cluster_centers_[2][0],y.cluster_centers_[2][1],2] 
			]
		
			centers=sorted(center, key=lambda t: t[0])
			for i in xrange(0,2):
				if centers[0][2]==i : pred[i]=0
				elif centers[1][2]==i: pred[i]=1
				else: pred[i]=2

			temp_dict={ }
			for i in xrange(0, len(datush_X[:,0])-1):
				temp_dict[]=

			# number of features, in our case 2:price per unit and price for product
			if category[0] in ('cucumber','milk','toothpaste'):
				plt.scatter(datush_X[:, 0],datush_X[:, 1], c=y_pred,s=200)
				title='category:'+category[0]+category[1]
				plt.title(title)
				#plt.savefig(' '+title+'.png')
				plt.show()
				
		
	
def cluster_on_all_files(path_name):
	

	tasks_list=[]
	# a folder was sepcified
	if os.path.isdir(path_name):
		for filename in os.listdir(path_name):
			# create all the files to convert: 
			tasks_list.append(os.path.join(path_name,filename))

	else: tasks_list.append(path_name)
	#print tasks_list
	super_barcode_category={}
	super_category_cluster_centers={}

	with open('barcode_super_category_position.csv', 'wb') as csvfile1:
		with open('category_position_centers.csv', 'wb') as csvfile2:
			#fieldnames = ['barcode','supermarket','category', 'position']
			writer1 = csv.writer(csvfile1)
			writer2 = csv.writer(csvfile2)
			#writer.writeheader()

			for task in tasks_list:
				#print task
				data=Data(task)
				clusti=Cluster(data)
				results={}
				super_name=data.get_super_name()
				super_barcode_category[super_name]={}
				clusti.cluster(super_barcode_category[super_name])
				super_category_cluster_centers={}
				#super_category_barcodes={}
				super_category_cluster_centers[super_name]=clusti.category_cluster_centers
				#pprint(clusti.barcode_category)
				#super_category_barcodes[super_name]=results[1]
				super_barcode_category[super_name]=clusti.barcode_category
				#pprint (super_barcode_category[super_name])

				for barcode in clusti.barcode_category:
					tup=clusti.barcode_category[barcode]
					writer1.writerow([barcode,super_name,tup[1],tup[0]])

				for category in clusti.category_cluster_centers:
					for i in xrange(0,3):
						tup=clusti.category_cluster_centers[category]
						writer2.writerow([category,i,tup[1,0],tup[0,0],super_name])




if __name__ == '__main__' :
	'''file_name=sys.argv[1]
	data=Data(file_name)
	clusti=Cluster(data)
	clusti.cluster(('bread',))
	#cluster_on_all_files(file_name)'''
	cluster_the_supermarkets_by_category_and_position()
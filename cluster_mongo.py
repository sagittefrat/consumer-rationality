#this module handles the cluster for each category:
#encoding=utf-8
import sys,os,csv
from data import Data
from pprint import pprint  
#from copy import deepcopy
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


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

		datush=self.data.get_data_by_category(category_name)

		

		X=np.zeros((len(datush),2))
		Y=np.zeros((len(datush),1))
		
	
		count=0
		# this is because SK-learn recieves np array:
		for key in datush:
			if datush[key][0]==0 or datush[key][1]==0: continue
			X[count][0]=datush[key][0]
			X[count][1]=datush[key][1]
			Y[count][0]=key
			count+=1
		if count<3: return 
		datush_X=np.zeros((count,2))
		datush_Y=np.zeros((count,1))

		for j in xrange(0,count):
			datush_X[j][0]=X[j][0]
			datush_X[j][1]=X[j][1]
			datush_Y[j][0]=Y[j][0]
			
		
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
		
		for i in xrange(0,3):
			if centers[0][2]==i : pred[i]=0
			elif centers[1][2]==i: pred[i]=1
			else: pred[i]=2

		temp_dict={}
		barcode_category_dict={ }
		for i in xrange(0, count):
			y_pred[i]=pred[y_pred[i]]

		for i in xrange(0, count):

			temp_dict[datush_Y[i,0]]=(str(y_pred[i]), str(datush_X[i, 0]),str(datush_X[i, 1]))
			self.barcode_category[str(int(datush_Y[i,0]))]=(str(y_pred[i]),category_name)
		
		if self.super_name=='Shupersal-Shelly_Ziv' and category_name=='coffee':
			# number of features, in our case 2:price per unit and price for product
			plt.scatter(datush_X[:, 0],datush_X[:, 1], c=y_pred,s=200)
			title=self.super_name+', category:'+category_name
			plt.title(title)
			plt.text( 15,30,'Nescafe_Tasters-choice')
			plt.show()

	
		sorted_centers=sorted(y.cluster_centers_, key=lambda t: t[0])
		self.category_cluster_centers[category_name]=[]
		for i in (0,1,2):
			self.category_cluster_centers[category_name].append(str(sorted_centers[i]))
			
		self.category_barcodes[category_name]=temp_dict
		

	def cluster(self,categories=None):

		if categories==None:
			categories=self.categories

		for category_name in categories:
			super_name=self.data.super_name
			self.cluster_category(category_name,super_name)
			#return
	

def cluster_the_supermarkets_by_category_and_position():

	super_category_cluster_centers={}
	'''
	with open('category_position_centers.csv', 'rb') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			if (row[0],row[1]) not in super_category_cluster_centers:
				super_category_cluster_centers[(row[0],row[1])]={}
			super_category_cluster_centers[(row[0],row[1])][row[4]]=(row[2],row[3])'''
	
	db = mongo.Database()
	db.read_super_category_cluster_centers()
		
	temp_dict={ }
	for category in super_category_cluster_centers:
		
		datush=super_category_cluster_centers[category]
		if len(datush)<3: return 

		# this is because SK-learn recieves np array:
		datush_X=np.zeros((len(datush),2))
		datush_Y=[]
		
		count=0
		x,j=(0,0),0
		s='Shupersal-Shelly_Ziv'
		for super_name in super_category_cluster_centers[category]:
			if super_name==s:
				x=super_category_cluster_centers[category][super_name]
				#print category,x
				#raw_input()
				j=count
			
			datush_X[count][0]=super_category_cluster_centers[category][super_name][0]
			datush_X[count][1]=super_category_cluster_centers[category][super_name][1]
			datush_Y.append(super_name)
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
		for i in xrange(0,3):
			if centers[0][2]==i : pred[i]=0
			elif centers[1][2]==i: pred[i]=1
			else: pred[i]=2

		for i in xrange(0, len(datush_X[:,0])-1):
			#if datush_Y[i]=='Shupersal-Deal_Haifa-mall':	
			writer1.writerow([category[0],int(category[1]),datush_Y[i], pred[y_pred[i]],datush_X[i, 0],datush_X[i, 1]])

		# number of features, in our case 2:price per unit and price for product
		if category[0] in ('tomato','toothpaste','coffee'):
			plt.scatter(datush_X[:, 0],datush_X[:, 1], c=y_pred,s=200)
			title='category:'+category[0]+category[1]
			plt.title(title)
			plt.text(x[0], x[1],s)
			#plt.savefig(' '+title+'.png')
			plt.show()


if __name__ == '__main__' :
	'''file_name=sys.argv[1]
	data=Data(file_name)
	clusti=Cluster(data)
	clusti.cluster(('bread',))
	#cluster_on_all_files(file_name)'''
	cluster_the_supermarkets_by_category_and_position()

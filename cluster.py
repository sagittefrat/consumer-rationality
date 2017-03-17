#this module handles the cluster for each category:
#encoding=utf-8
import sys
import os


#this class handles the data, recieves csv and keep it in a dictionary
class Data:

	def __init__ (self, path):

		self.data_dict={}
		if path[-3:]=='csv':	
			import csv
			count=0
			with open(path, 'rb') as csvfile:
				reader = csv.reader(csvfile)
				
				for row in reader:
					count+=1
					if count==1: continue
					# if there is no category, continue:
					if row[-1]=='': continue
					self.data_dict[row[1]]=row[2:]

		self.categories=self.get_categories()
		print self.categories

	def get_data_by_category(self,category_name):
		temp_dict={}
		for barcode in self.data_dict:
			item=self.data_dict[barcode]
			if category_name == item[-1]:
				#returns tuple of (price per unit, price for product):
				temp_dict[barcode]=(float(item[-4]),float(item[-5]))
		return temp_dict


	# this func finds all the categories and returns them as a tuple
	def get_categories(self):
		
		categories=[]
		for barcode in self.data_dict:
			item=self.data_dict[barcode]
			categories.append(item[-1])
			#print 'category',categories[-1]
		return set(categories)



class Cluster:

	def __init__ (self, data,categories=None):

		self.data=data
		#categories is a tuple of strings
		self.categories=categories
		if self.categories==None:
			 self.categories=self.data.categories

		self.data_category={}
		for category_name in self.categories:
			#self.data_category[category_name]={}
			pass


	def cluster_category(self,category_name):

		import numpy as np
		from sklearn.cluster import KMeans
		import matplotlib.pyplot as plt

		datush=self.data.get_data_by_category(category_name)
		#print datush

		datush_X=np.zeros((len(datush),2))
		datush_Y=np.zeros((len(datush),1))
		
		count=0
		# this is because SK-learn recieves np array:
		for key in datush:
			#print key
			datush_X[count][0]=datush[key][0]
			datush_X[count][1]=datush[key][1]
			datush_Y[count][0]=key
			count+=1

		
		y = KMeans(n_clusters=3).fit(datush_X)
		#print y.cluster_centers_
		y_pred= y.predict(datush_X)

		temp_dict={}
		for i in xrange(0, len(datush_X[:,0])-1):
			temp_dict[str(datush_Y[i])]=(y_pred[i], datush_X[i, 0],datush_X[i, 1])
		#print long(datush_Y[-18]),datush_X[-18][0],datush_X[-18][1]
		
		# number of features, in our case 2:price per unit and price for product
		plt.scatter(datush_X[:, 0],datush_X[:, 1], c=y_pred)
		plt.title("Anisotropicly Distributed Blobs")
		return y.cluster_centers_
		#plt.show()

	def cluster(self,categories=None):

		if categories==None:
			categories=self.categories

		for category_name in categories:
			#print 'category_name',category_name
			
			self.data_category[category_name]=self.cluster_category(category_name)
		#print self.data_category
		return self.data_category


def get_super_name(task):
	
	print task
	if 'cat' in task:
		
		task=task.split('-')
		task=task[2:-4]
		super_name=task
		print super_name
		return super_name


def cluster_on_all_files(path_name):

	tasks_list=[]
	# a folder was sepcified
	if os.path.isdir(path_name):
		for filename in os.listdir(path_name):
			# create all the files to convert 
			tasks_list.append(os.path.join(path_name,filename))

	else: tasks_list.append(path_name)
	#print tasks_list

	for task in tasks_list:
		print task
		data=Data(task)
		clusti=Cluster(data)
		results={}
		super_name=str(get_super_name(task))
		results[super_name]=clusti.cluster()


if __name__ == '__main__' :
	file_name=sys.argv[1]
	#data=Data(file_name)
	#clusti=Cluster(data)
	#clusti.cluster()
	cluster_on_all_files(file_name)

					

import config
#this class handles the data, recieves csv and keep it in a dictionary
class Data:

	def __init__ (self, path):

		self.file_name=path
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
		self.super_name=self.get_super_name()

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
			if item[-1]=='1':continue
			categories.append(item[-1])
		return set(categories)


	def get_super_name(self):
		
		# if there are already categories in the file:
		if 'cat' in self.file_name :
			task=self.file_name.split('-')
			task=task[2:5]
			super_id=(int(task[0]),int (task[1]), int (task[2]))
			super_name=config.CHAINS[super_id[0]][super_id[1]]
			#print 'super_name1',super_name
			if super_id[0]==7290027600007:
				super_name=super_name+'_'+config.SHUPERSAL_BRANCHES[super_id[2]]
			elif super_id[0]==7290058179503:
				super_name=super_name+'_'+config.LAHAV_BRANCHES[super_id[2]]


			print 'super_name2',super_name
			return super_name


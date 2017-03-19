#this class handles the Interface
import sys,os,csv
from data import Data
import config
import xml_to_csv
from cluster import Cluster

def main():

	option = config.Program_Options(sys.argv[1:])
	if option.existence_path!=None:
		run_on_all_xml(option.existence_path)

	if option.csv_file_path!=None:
	
		file_name=option.csv_file_path
		super_barcode_dict=cluster_on_all_files(file_name)
		#print super_barcode_dict


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
			super_category_cluster_centers={}
			#super_category_barcodes={}

			for task in tasks_list:
				#print task
				data=Data(task)
				clusti=Cluster(data)
				super_name=data.get_super_name()
				super_barcode_category[super_name]={}
				clusti.cluster(super_barcode_category[super_name])
				#super_category_barcodes[super_name]=results[1]
				super_category_cluster_centers[super_name]=clusti.category_cluster_centers
				super_barcode_category[super_name]=clusti.barcode_category

				for barcode in clusti.barcode_category:
					tup=clusti.barcode_category[barcode]
					writer1.writerow([barcode,super_name,tup[1],tup[0]])

				for category in clusti.category_cluster_centers:
					for i in xrange(0,3):
						tup=clusti.category_cluster_centers[category]
						writer2.writerow([category,i,tup[1,0],tup[0,0],super_name])




if __name__ == '__main__' :
	main()





# this class handles the Interface
import sys, os, csv
from data import Data
import config
import xml_to_csv
import cluster_mongo 
import mongo
from pprint import pprint

def main():
	option = config.Program_Options(sys.argv[1:])
	if option.existence_path != None:
		run_on_all_xml(option.existence_path)

	if option.csv_file_path != None:
		file_name = option.csv_file_path
		super_barcode_dict = cluster_mongo.cluster_on_all_files(file_name)
		# print super_barcode_dict
	if option.clustering_supermarkets==True:
		print '$$$$$$$$$$$'
		cluster_mongo.cluster_the_supermarkets_by_category_and_position()
	

 
if __name__ == '__main__':
	main()




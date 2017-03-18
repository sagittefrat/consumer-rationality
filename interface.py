#this class handles the Interface
import sys,os
from data import Data
import config
import xml_to_csv
from cluster import cluster_on_all_files

def main():

	option = config.Program_Options(sys.argv[1:])
	if option.existence_path!=None:
		run_on_all_xml(option.existence_path)

	if option.csv_file_path!=None:
	
		file_name=option.csv_file_path
		super_barcode_dict=cluster_on_all_files(file_name)
		#print super_barcode_dict
	



if __name__ == '__main__' :
	main()


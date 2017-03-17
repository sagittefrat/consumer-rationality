import sys,os	
import config


def run_on_all_xml(path_name,destination_path=None) :
	
	from xmlutils.xml2csv import xml2csv
	path_name=os.path.abspath(path_name)
	#------open files: 
	if os.path.exists(path_name)==None:
		print "ilegal path!"
		return

	# get all the xml from the folder
	tasks_list = []
	# a folder was sepcified
	if os.path.isdir(path_name):
		for filename in os.listdir(path_name):
			# create all the files to convert
			tasks_list.append(os.path.join(path_name,filename))

	#Perform the specified command on all specified tasks
	for task in tasks_list:
		
		if task[-3:]=='xml':
			
			task_full_path=os.path.join(path_name,task)
			task_to_create=task_full_path[:-3]+'csv'

			#if needs a name change:
			if task[-6:-4]=='gz':
				task_to_create=change_xml_name(path_name,task)	

			# if a destination was mentioned
			if destination_path!=None:
				task_csv=task[-3:]+'csv'
				task_to_create=os.path.join(destination_path,task_csv)

			#actual converting from xml to csv:
			converter = xml2csv(task_full_path, task_to_create, encoding="utf-8")
			task=task.split('-')
			if task[1]=='7290027600007':
				converter.convert(tag="Item")
			else: converter.convert(tag="Product")
			os.remove(task_full_path)

			


		elif filename[-4:]=='json':
			'''from xmlutils.xml2json import xml2json
			print "xml2json(",task_to_convert," ", task_to_create, "encoding=utf-8)"
			converter = xml2json(task_to_convert, task_to_create, encoding="utf-8")
			converter.convert()
			print converter.get_json()'''


def change_xml_name(task_path,task_old_name):
	import xml.etree.ElementTree as ET
	et = ET.parse(task_old_name)
	root=et.getroot()
	
	if root.find('ChainId')==None:
		# not shupersal
		chain_id=root.find('ChainID').text 
		sub_chain=root.find('SubChainID').text
		store_id=root.find('StoreID').text 
	else:
		chain_id=root.find('ChainId').text  
		sub_chain=root.find('SubChainId').text
		store_id=root.find('StoreId').text 
	task_name="prices-"+chain_id+"-"+sub_chain+"-"+store_id+"-"+config.time+'.csv'
	return os.path.join(task_path,task_name) 


if __name__ == '__main__' :
	option = config.Program_Options(sys.argv[1:])
	run_on_all_xml(option.existence_path)
	
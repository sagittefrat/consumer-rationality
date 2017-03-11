import sys,os
import options	


def run_on_all_xml(option):
	
	from xmlutils.xml2csv import xml2csv

	#------open files: 
	path_name = os.path.abspath(option.existence_path)
	print path_name
	if os.path.exists(path_name)==None:
		print "ilegal path!"
		return

	

	# get all the xml from the folder
	tasks_list = []
	# a folder was sepcified
	if os.path.isdir(path_name):
		for filename in os.listdir(path_name):
			print "filename[-4:]",filename[-4:]
			if filename[-4:]!='.xml': continue
			tasks_list.append(os.path.join(path_name,filename))
			#print tasks_list



	#Perform the specified command on all specified tasks
	for task in tasks_list:
		print "task name:", task

		import xml.etree.ElementTree as ET
		et = ET.parse(os.path.join(path_name,task))
		root=et.getroot()
		print "root",root
		if root.find('ChainId')==None:
			print "not shupersal"
			chain_id=root.find('ChainID').text 
			sub_chain=root.find('SubChainID').text
			store_id=root.find('StoreID').text 
		else:
			chain_id=root.find('ChainId').text  
			sub_chain=root.find('SubChainId').text
			store_id=root.find('StoreId').text
		print "chain_id",chain_id
		print "store_id",store_id
		print "sub_chain", sub_chain

		task_new_name="prices"+chain_id+"-"+sub_chain+"-"+store_id+"-"+"20170305.csv"

		task_full_path=os.path.join(path_name,task)[:-4]
	
		task_to_convert=task_full_path+".xml"

		task_to_create=os.path.join(path_name,task_new_name)


		'''from xmlutils.xml2json import xml2json
		print "xml2json(",task_to_convert," ", task_to_create, "encoding=utf-8)"
		converter = xml2json(task_to_convert, task_to_create, encoding="utf-8")
		converter.convert()
		print converter.get_json()'''

		print "xml2csv(",task_to_convert," ", task_to_create, "encoding=utf-8)"
		converter = xml2csv(task_to_convert, task_to_create, encoding="utf-8")
		converter.convert(tag="Item")
		print "succsefuly created: ", task_to_create
		os.remove(task_to_convert)



if __name__ == '__main__' :
	option = options.Program_Options(sys.argv[1:])
	run_on_all_xml(option)
	
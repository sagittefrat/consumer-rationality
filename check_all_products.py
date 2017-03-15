
import options

def get_basket(option):
	path_name = os.path.abspath(option.existence_path)

	# get all the basket in the folder
	baskets_list = []
	# a folder was sepcified:
	if os.path.isdir(path_name):
		for filename in os.listdir(path_name):
			baskets_list.append(os.path.join(path_name,filename))

	else: baskets_list.append(path_name)

	for basket in baskets_list:
		#get chain id, sub chain id, store id :
		if 'reciept' in basket:
                        #orig_name=basket
                        basket=basket.split('-')
                        chain_id=basket[1]
                        sub_chain=basket[2]
                        store_id=basket[3]
                        date=basket[4]


		import csv
		with open('basket', 'rb') as csvfile:
			spamreader = csv.reader(csvfile, delimiter='')
			for row in spamreader:



def check_all(option):
	get_basket(option)


if __name__ == '__main__' :
	option = options.Program_Options(sys.argv[1:])
	check_all(option)
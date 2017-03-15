#encoding=utf-8
import sys

categories_names={'משחת שיניים':('שיניים','משחת שיניים'), 'חטיף בוטנים':('חטיף בוטנים','במבה'),'המבורג':'המבורג', 'טמפונים':('טמפונים','טמפון','טמפוני'),'אקונומיקה':('אקונומיקה'), 'מסיר כתמים':('מסיר כתמים'),'מסיר שומנים':('מסיר שומנים'),}

def create_categories():
	file_name=sys.argv[1]
	
	if file_name[-3:]=='csv':
		import csv
		with open(file_name, 'rb') as csvfile:
			spamreader = csv.reader(csvfile)
			for row in spamreader:
				for name in categories_names:
					for synonum in categories_names[name]:
						if synonum in row:
							print 'found: ', name
							print 'row: ', row
							break



if __name__ == '__main__' :
	create_categories()


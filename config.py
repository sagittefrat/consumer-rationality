# supermarket spider configuration file
# author Gal

from datetime import datetime
import pytz
import getopt

time = datetime.now(tz=pytz.timezone('Asia/Jerusalem')).strftime("%Y%m%d")
home_dir = "/home/gal"


class Program_Options :
	
	def __init__( self, args ) :

		self.gal_home='../scrapedfiles/'
		try:
			opts, args = getopt.getopt(	args,
				"e:d:b",
				["existence-path=",
				"destination-folder",
				"basket-name" 		
				] )
		except getopt.GetoptError :
			print "Missing or incorrect parameters specified!",sys.stderr
			usage()
			sys.exit(1)

		self.existence_path= None
		self.destination_folder = None	

		for opcode, oparg in opts :
			print "opcode:", opcode
			print"oparg:", oparg	

			if opcode in ('-e', '--existence path' ) :
				self.existence_path = oparg
			

			if opcode in ('-b', '--basket name' ) :
				self.basket_name = oparg
			

			if opcode in ('-d','--destination folder'):
				self.destination_folder = opcode
			else:
				self.destination_folder = ''
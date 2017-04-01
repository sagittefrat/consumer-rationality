# supermarket spider configuration file
# author Gal

from datetime import datetime
import pytz
import getopt
import sys

time = datetime.now(tz=pytz.timezone('Asia/Jerusalem')).strftime("%Y%m%d")
home_dir = "/home/gal"
CHAINS = {7290027600007: {1: 'Shupersal-Shelly', 2: 'Shupersal-Deal', 4: 'Shupersal-Deal-Extra', 5: 'Yesh',
                          7: 'Shupersal-Express'},
          7290696200003: {1: 'Victory_Haifa'}, 7290058179503: {1: 'Lahav'}, 7290661400001: {1: 'Shuk_Haifa'}}
SHUPERSAL_BRANCHES = {4: 'Carmel', 17: 'Horev', 19: 'Ziv', 33: 'Stela', 38: 'Denia', 71: 'Tel-Hanan', 212: 'Vardia',
                      258: 'Admirality', 302: 'Keler', 306: 'Hanita', 312: 'Eliezer', 314: 'France', 327: 'Raul',
                      330: 'Nativ-Hen', 336: 'Sapir',
                      352: 'Haifa-mall', 359: 'Grand-mall', 368: 'Marganit', 387: 'Rambam'}
LAHAV_BRANCHES = {30: 'Haifa', 63: 'Remez'}


class Program_Options:
    def __init__(self, args):

        '''parser = argparse.ArgumentParser(description='Process some integers.')
        parser.add_argument('--existence-path', default='', help='path for csv files')
        parser.add_argument('--destination-folder',  default='',help='destination for out csv files')
        parser.add_argument('--clustering supermarkets',  default='',help='destination for out csv files')

        args = parser.parse_args()
        print(args.accumulate(args.integers))'''

    
        try:
            opts, args = getopt.getopt(args,
                                       "e:d:p:c:s:b",
                                       ["existence-path=",
                                        "destination-folder=",
                                        "clustering supermarkets=",
                                        "clustering-files_path",
                                        "supermarket-list",
                                        "basket-name"
                                        ])
        except getopt.GetoptError:
            print "Missing or incorrect parameters specified!", sys.stderr
            usage()
            sys.exit(1)

        self.existence_path = None
        self.destination_folder = None
        self.clustering_supermarkets = None
        self.csv_file_path = None
        self.supermarkets_dict = None

        for opcode, oparg in opts:
            print "opcode:", opcode
            print"oparg:", oparg

            if opcode in ('-e', '--existence path'):
                self.existence_path = oparg

            if opcode in ('-d', '--destination folder'):
                self.destination_folder = oparg

            if opcode in ('-c', '--clustering-files_path'):
                self.csv_file_path = oparg

            if opcode in ('-p', '--clustering supermarkets'):
                self.clustering_supermarkets = True

            if opcode in ('-s', '--supermarket-list'):
                self.supermarkets_dict = self.get_super_from_list(oparg)
            else:
                self.supermarkets_dict = CHAINS

            if opcode in ('-b', '--basket-name'):
                self.basket_name = oparg

    
    this func recieves a text file and names the different supermarkets:
    '''

    def get_super_from_list(self, file_name):
        pass
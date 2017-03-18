import config
import os
import csv
from pprint import pprint

receipts_path = config.home_dir + '/scrapedfiles/reciets/'

receipts = []


def process_receipt(branches, file_name):
    filename_details = file_name.split('-')
    branch_code = filename_details[1] + '-' + filename_details[1] + '-' + filename_details[2] + '-' + filename_details[3]
    branch = branches[branch_code]
    with open(receipts_path + file_name, 'rb') as input_file:
        reader = csv.reader(input_file)

        total_weight = 0
        for i, row in enumerate(reader):
            if i == 0: continue
            total_weight += row[2]

        for i, row in enumerate(reader):
            if i == 0: continue
            print 'branch code', branch_code, 'row:'
            pprint (row)
            receipts.append((branch[row[0]],row[2]/total_weight))
    print 'receipt:'
    pprint(receipts)
    raw_input('PAUSE')



def run_on_all_files(branches):
    for filename in os.listdir(receipts_path):
        process_receipt(branches, filename)
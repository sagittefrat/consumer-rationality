import config
import os
import csv
from pprint import pprint

receipts_path = config.home_dir + '/scrapedfiles/receipts/'
cat_path = config.home_dir + '/scrapedfiles/cat/'
data_file = config.home_dir + '/scrapedfiles/misc/barcode_super_category_position.csv'
receipts = []
branches = {}
branches_prices = {}


def build_branches_dict():
    print 'build dict'
    with open(data_file, 'rb') as input_file:
        reader = csv.reader(input_file)
        for row in reader:
            barcode = row[0]
            branch_code = row[1]
            category = row[2]
            position = row[3]
            if branch_code not in branches:
                branches[branch_code] = {}
                # print 'first barcode for branch ' + branch_code + ':'
            branches[branch_code][barcode] = (category, position)
            # print 'branch:'
            # pprint(branches[branch_code])
            # pprint(branches)


def process_receipt(file_name):
    receipt = []
    print 'filename', file_name
    filename_details = file_name.split('_')
    branch_code = filename_details[1] + '_' + filename_details[2]
    # if we want to branch code instead of names
    # branch_code = filename_details[1] + '-' + filename_details[2] + '-' + filename_details[3]
    branch = branches[branch_code]
    with open(receipts_path + file_name, 'rb') as input_file:
        reader = csv.reader(input_file)

        total_price = 0
        # print 'summing'
        for i, row in enumerate(reader):
            if i == 0 or row[0] not in branch:
                continue
            # print 'add', row[2]
            total_price += float(row[2])

    with open(receipts_path + file_name, 'rb') as input_file:
        reader = csv.reader(input_file)
        for i, row in enumerate(reader):
            if i == 0:
                continue
            if row[0] not in branch:
                print 'category for', row[0], row[1], 'is not varied enough, ignoring'
                continue
            # print 'branch code', branch_code, 'row:'
            # pprint (row)
            barcode = row[0]
            category_and_position = branch[row[0]]
            price = float(row[2])
            weight = price / total_price
            receipt.append((barcode, category_and_position, weight, price))
    print 'receipt summary:'
    pprint(receipt)
    pprint(rational_choice(receipt))
    raw_input('PAUSE')
    receipts.append((file_name, receipt))


def build_branch_prices(file_name):
    print 'building price list for file', file_name
    branch = {}
    if file_name[-3:] == 'csv':
        with open(cat_path + file_name, 'rb') as csvfile:
            reader = csv.reader(csvfile)
            for i, row in enumerate(reader):
                if i == 0:
                    continue
                branch[row[1]] = row[12]
    return branch


def build_branches_prices():
    print 'build price lists'
    for filename in os.listdir(cat_path):
        branch = build_branch_prices(filename)
        filename_details = filename.split('-')
        branch_code = filename_details[2] + '-' + filename_details[3] + '-' + filename_details[4]
        branches_prices[branch_code] = branch


def receipt_in_branch(receipt, branch_code, branch):
    
    print 'calculate receipt for', branch_code
    print 'branch:'
    pprint(branch)
    total_price = 0
    for row in receipt:
        barcode = row[0]
        price = float(branch[row[0]])
        row[3] =
        if barcode not in branch:
            print 'item', row[0], 'not in branch'
            return None
        total_price +=  * price
    return total_price


def rational_choice(receipt):
    print 'choose cheapest branch'
    total_prices = []
    for branch_code in branches_prices:
        total_prices = (branch_code, receipt_in_branch(receipt, branch_code, branches_prices[branch_code]))
    print 'total prices'
    pprint(total_prices)


def run_on_all_files():
    print 'running on all files'
    for filename in os.listdir(receipts_path):
        process_receipt(filename)
    pprint(receipts)


def main():
    build_branches_prices()
    build_branches_dict()
    run_on_all_files()


if __name__ == "__main__":
    main()

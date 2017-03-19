# consumer-rationality
=====================================
This ia a final project of the course "Social Choice" at the Technion

### How to run:

If you dont have csv files with categories:
  you can use 'scrapy' in order to download the supermarket's data, this script will download the data, convert it from xml to csv for each supermarket and add a category for each product(barcode)
  $$$ gal
  then, continue with the bext steps:

If you have csv files with categories:
  1) run 
  '''
  Interface.py -c [folder of the categorized data]
  '''
    you will recieve two files: 'category_position_centers.csv','barcode_super_category_position.csv' and some clustering images for chosen caategories
    'category_position_centers.csv' - this file holds the 3 clustering centers(price per unit, price per product) for each supermarket and category. 
    barcode_super_category_position.csv' - this file holds the cluster position for each product in aech supermarket
  2) run 
  '''
  Interface.py -b [barcode_super_category_position.csv path] -e [folder of the categorized data] -d [destination folder of the categorized data]
  '''
    you will recieve results for $$$$gal
    3)  run 
    '''Interface.py [category_position_centers.csv path] 
    '''
      you will recieve results: for each supermarket what its ranking for each category and position
      for example:  'Yesh_France' is at position 0 in category milk - meaning it is in the 'discount' cluster for milk
                    'Deal_Haifa-mall' is at position 2 in category milk - meaning it is in the 'premium' cluster for milk 

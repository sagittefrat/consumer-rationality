from pymongo import MongoClient
from pprint import pprint


class DatabaseConnection:
    client = MongoClient('mongodb://prices_db_user:okmjmkol@ds137090.mlab.com:37090/prices_db')
    db = client.prices_db

    def __init__(self):
        pass


class Database:
    def __init__(self):
        self.db = DatabaseConnection.db

    def write_pricelists_one_by_one(self, pricelists):   #slow but with indication
        length = len(pricelists)
        for i, pricelist in enumerate(pricelists):
            print 'save pricelists', i+1, 'of', length, ': branch code', \
                pricelist["branch_code"], 'date', pricelist["date"]
            self.db.priclists.update_one(
                {"_id": pricelist["_id"]},
                {
                    "$set": pricelist
                },
                upsert=True
            )


    def write_one_pricelist(self, pricelist):
        self.db.priclists.update_one(
            {"_id": pricelist["_id"]},
            {
                "$set": pricelist
            },
            upsert=True
        )


    def write_pricelists_of_date(self, date, pricelists):   #another approach I might try
        self.db.priclists.update_many(
            {"date": date},
            {
                "$set": pricelist
            },
            upsert=True
        )


    def write_pricelists(self, pricelists): #too slow with no progress indication
        try:
            self.db.priclists.insert_many(pricelists)
        except:
            print "error writing to db"

    def read_pricelists(self):
        pricelists = []
        results = self.db.priclists.find()
        for doc in results:
            pricelists.append(doc)
            print 'load doc', doc["_id"]

    def write_items(self, items):
        self.db.items.update_one(
            {"name": "items"},
            {
                "$set": {"data": items}
            },
            upsert=True
        )


    def read_items(self):
        return self.db.items.find_one({"name":"items"})["data"]


    def write_barcode_super_category_position(self, barcode_super_category_position, branch_code):
        node = {"_id": branch_code, "data": barcode_super_category_position}
        self.db.barcode_super_category_position.update_one(
            {"_id": node["_id"]},
            {
                "$set": node
            },
            upsert=True
        )


    def read_barcode_super_category_position(self):
        return self.db.barcode_super_category_position.find()


    def write_super_category_cluster_centers(self, super_category_cluster_centers):
        self.db.cluster.update_one(
            {"name": "super_category_cluster_centers"},
            {
                "$set": {"data": super_category_cluster_centers}
            },
            upsert=True
        )


    def read_super_category_cluster_centers(self):
        return self.db.cluster.find_one({"name":"super_category_cluster_centers"})["data"]



if __name__ == '__main__':
    db = Database()
    db.read_pricelists()
import os
import sys
import json
import numpy as np
import pandas as pd
import pymongo

from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)

import certifi # Just to make an secure HTTP Connection, In this case with MongoDB so that, mongodb knows that it is the valid request. 
certificate_authority = certifi.where()

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

# ETL Pipeline: Read csv data and convert into json format. 
class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
    
    def csv_to_json_converter(self, file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)
            records = list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e, sys)
    
    def insert_data_to_mongodb(self, records, database, collection): 
        try:
            self.database = database
            self.collection = collection
            self.records = records

            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)

            self.database = self.mongo_client[self.database]
            self.collection = self.database[self.collection]
            self.collection.insert_many(self.records)
            
            return (len(self.records))
        
        except Exception as e:
            raise NetworkSecurityException(e, sys)

if __name__ == '__main__':
    FILE_PATH = "Network_Data/phisingData.csv"
    DATABASE = "NETRA"
    Collection = "NetworkData"
    
    networkobj = NetworkDataExtract()
    records = networkobj.csv_to_json_converter(file_path=FILE_PATH)
    print(records)
    no_of_records = networkobj.insert_data_to_mongodb(records, DATABASE, Collection)
    print(no_of_records)
import pymongo

import json


import os
load_dotenv()


DB_HOST = os.getenv('DATABASE_HOST')

DB_USERNAME = os.getenv('DATABASE_USERNAME')
DB_PASSWORD = os.getenv('DATABASE_PASSWORD')


with open('../state_Data/state_district.json') as f:
   data_1 = json.load(f)
   state_block_data = data_1




try:
    myclient = pymongo.MongoClient( DB_HOST )
    myclient.test.authenticate( DB_USERNAME , DB_PASSWORD )
    print("[+] Database connected!")

    mydb = myclient["state"]
    district_collection = mydb["district"]

    # State Toppper 

    # print(state_block_data[0])
    for data in state_block_data:
        # print(data)
        # print(type(data))
        #    break
        insertable_data = data

        district_collection.insert_one(insertable_data)
        print("data_inserted_successfully")

except Exception as e:
    print("[+] Database connection error!")
    raise e






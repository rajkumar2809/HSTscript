import pymongo
import json
from dotenv import load_dotenv
import os


load_dotenv()


DB_HOST = os.getenv('DATABASE_HOST')

DB_USERNAME = os.getenv('DATABASE_USERNAME')
DB_PASSWORD = os.getenv('DATABASE_PASSWORD')


with open("../blockDetails/blockDetails.json", "r") as jsonFile:
    data = json.load(jsonFile)

try:
    myclient = pymongo.MongoClient( DB_HOST )
    myclient.test.authenticate( DB_USERNAME , DB_PASSWORD )
    print("[+] Database connected!")

    for i in range (len(data)):
        print(data[i])
        db_name = "BLOCK_" + data[i]["blockID"]
        print(db_name)
        try: 
            mydb = myclient[db_name]
            block_details_col = mydb["blockDetails"]
            x = block_details_col.insert_one(data[i])
        except Exception as e:
            print("some exception occured...")


except Exception as e:
    print("[+] Database connection error!")
    raise e




    
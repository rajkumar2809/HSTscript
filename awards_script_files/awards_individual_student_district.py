import pymongo

# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
import os
import json

from dotenv import load_dotenv

load_dotenv()


DB_HOST = os.getenv('DATABASE_HOST')

DB_USERNAME = os.getenv('DATABASE_USERNAME')
DB_PASSWORD = os.getenv('DATABASE_PASSWORD')



with open('../awards/district_topper.json') as f:
   data_2 = json.load(f)
   district_topper_data = data_2


district_topper_data[0]["statusOfPublication"] = 0
district_topper_data[0]["actionLog"] = [{
    "userID": "111",
    "timestamp": 1212,
    "remark" : "Some remark"
    }]
district_topper_data[0]["docPath"] = ""
district_topper_data[0]["finalcount"] = 98

try:
    myclient = pymongo.MongoClient( DB_HOST )
    myclient.test.authenticate( DB_USERNAME , DB_PASSWORD )
    mydb = myclient["AWARDS"]
    individual_collection = mydb["INDIVIDUAL_STUDENT_DISTRICT"]
    print("[+] Database connected!")

    for data in district_topper_data:
        data["statusOfPublication"] = 0
        data["actionLog"] = [{
            "userID": "111",
            "timestamp": 1212,
            "remark" : "Some remark"
            }]
        data["docPath"] = ""
        data["finalcount"] = 98

        individual_collection.insert_one(data)

    print("data_inserted_successfully")


except Exception as e:
    print("[+] Database connection error!")
    raise e




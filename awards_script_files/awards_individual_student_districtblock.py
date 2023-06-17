import pymongo

# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
import os
import json


from dotenv import load_dotenv

load_dotenv()


DB_HOST = os.getenv('DATABASE_HOST')

DB_USERNAME = os.getenv('DATABASE_USERNAME')
DB_PASSWORD = os.getenv('DATABASE_PASSWORD')


with open('../awards/district_block_toppers.json') as f:
   data_1 = json.load(f)
   block_topper_data = data_1

try:
    myclient = pymongo.MongoClient( DB_HOST )
    myclient.test.authenticate( DB_USERNAME , DB_PASSWORD )
    mydb = myclient["AWARDS"]
    individual_collection = mydb["INDIVIDUAL_STUDENT_DISTRICTBLOCK"]
    print("[+] Database connected!")

    
    for district_wise_data in block_topper_data:
        print(type(district_wise_data))
        print(district_wise_data.keys())
        district_wise_data["statusOfPublication"] = 0
        district_wise_data["actionLog"] = [{
            "userID": "111",
            "timestamp": 1212,
            "remark" : "Some remark"
            }]
        district_wise_data["docPath"] = ""
        district_wise_data["finalcount"] = 98
        print(district_wise_data.keys())

        individual_collection.insert_one(district_wise_data)
        print("Data inserted successfully")


except Exception as e:
    print("[+] Database connection error!")
    raise e


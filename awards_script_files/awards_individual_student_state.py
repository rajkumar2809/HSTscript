import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
import os
import json


from dotenv import load_dotenv

load_dotenv()


DB_HOST = os.getenv('DATABASE_HOST')

DB_USERNAME = os.getenv('DATABASE_USERNAME')
DB_PASSWORD = os.getenv('DATABASE_PASSWORD')



with open('../awards/state_topper.json') as f:
   data_3 = json.load(f)
   state_topper_data = data_3


state_topper_data["statusOfPublication"] = 0
state_topper_data["actionLog"] = [{
    "userID": "",
    "timestamp": 1212,
    "remark" : "Some remark"
    }]
state_topper_data["docPath"] = ""
state_topper_data["finalcount"] = 98




try:
    myclient = pymongo.MongoClient( DB_HOST )
    myclient.test.authenticate( DB_USERNAME , DB_PASSWORD )
    mydb = myclient["AWARDS"]
    individual_collection = mydb["INDIVIDUAL_STUDENT_STATE"]
    print("[+] Database connected!")

    insertable_data = {
    "sessionYear": 2022,
    "userType": "Student",
    "state" : state_topper_data      
}

    individual_collection.insert_one(insertable_data)

    
   
    print("Data inserted successfully")


except Exception as e:
    print("[+] Database connection error!")
    raise e






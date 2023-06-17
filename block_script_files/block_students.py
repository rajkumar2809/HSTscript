import pymongo
import json
import os
load_dotenv()


DB_HOST = os.getenv('DATABASE_HOST')

DB_USERNAME = os.getenv('DATABASE_USERNAME')
DB_PASSWORD = os.getenv('DATABASE_PASSWORD')

file_names = os.listdir("../teacher-school/")



# print(os.listdir("block-wise-student-list_original/"))
file_names = os.listdir("../blockwise_students/")




try:
    myclient = pymongo.MongoClient( DB_HOST )
    myclient.test.authenticate( DB_USERNAME , DB_PASSWORD )
    print("[+] Database connected!")

    for d in file_names:

        sep = '.'
        block_sc_name = d.split(sep, 1)[0]
        print(block_sc_name)
        sep_2 = '-'
        block_sc_name_list = block_sc_name.split(sep_2 ,1)
        print(block_sc_name_list)
        block_name = block_sc_name_list[0]
        print(block_name)

        db_name = "BLOCK_"+block_name
        print(db_name)
        try:
            mydb = myclient[db_name]
            student_col = mydb["Students"]
            # block_details_col = mydb["blockDetails"]
            school_teacher_list_col = mydb["schoolTeacherList"]

            folder_file_name = "../blockwise_students/" + d
            with open(folder_file_name, "r") as jsonFile:
                data = json.load(jsonFile)
            # with open("school-teacher.json", "r") as jsonFile:
            #     teacher_Data = json.load(jsonFile)  
            
            student_data = data

            x = student_col.insert_one(student_data)

        except Exception as e:
            print("This is from exception")
            print(db_name)
            break



except Exception as e:
    print("[+] Database connection error!")
    raise e

    



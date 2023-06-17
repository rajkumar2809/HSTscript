import pymongo
import json
import os
load_dotenv()


DB_HOST = os.getenv('DATABASE_HOST')

DB_USERNAME = os.getenv('DATABASE_USERNAME')
DB_PASSWORD = os.getenv('DATABASE_PASSWORD')

file_names = os.listdir("../teacher-school/")


try:
    myclient = pymongo.MongoClient( DB_HOST )
    myclient.test.authenticate( DB_USERNAME , DB_PASSWORD )
    print("[+] Database connected!")

    for d in file_names:
        # print(d)
        sep = '_'
        block_id = d.split(sep, 1)[0]
        # print(block_id)
        dirs = '../teacher-school/' +  d + '/'
        # print(dirs)
        block_floder_names = os.listdir(dirs)
        # print(block_floder_names)
        for data in block_floder_names:
            # print(data)

            db_name = "BLOCK_"+block_id
            # print(db_name)
            try:
                mydb = myclient[db_name]

                school_teacher_list_col = mydb["schoolTeacherList"]

                folder_file_name = "../teacher-school/" + d + "/" + data
                print("FOlder file name is" ,  folder_file_name)
                with open(folder_file_name, "r") as jsonFile:
                    teacher_data = json.load(jsonFile)


                student_teacher_Data = teacher_data  
                x = school_teacher_list_col.insert_one(student_teacher_Data)

                # break


            except Exception as e:
                print("Exception occurred ...../")
                print(db_name)
                break



except Exception as e:
    print("[+] Database connection error!")
    raise e




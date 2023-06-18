import os 

print("Starting the script....")

# Awards state student data
print("State topper data inserting ...")
os.system('python awards_script_files/awards_individual_student_state.py')


#  Awards District student data
print("District topper data inserting ...")
os.system('python awards_script_files/awards_individual_student_district.py')



# Awards DistrictBllock student data
print("District block topper data inserting ...")
os.system('python awards_script_files/awards_individual_student_districtblock.py')


# Block Student Details
print("BLock student  data inserting ...")
os.system('python block_script_files/block_students.py')

# SchoolTeacher Student Details
print("Block schoolTeacherlist data inserting ...")
os.system('python block_script_files/block_schoolTeachers.py')

# Block Details
print("Block block details  data inserting ...")
os.system('python block_script_files/block_block_Details.py')

# State Block Details
print("State block  data inserting ...")
os.system('python state_script_files/state_block.py')

# State District Details
print("State district  data inserting ...")
os.system('python state_script_files/state_district.py')

# State Users
print("State user  data inserting ...")
os.system('python state_script_files/state_users.py')



print("Script completed......")




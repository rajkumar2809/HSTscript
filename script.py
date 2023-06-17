import os 

print("Starting the script....")

# Awards state student data
os.system('python awards_script_files/awards_individual_student_state.py')


#  Awards District student data
os.system('python awards_script_files/awards_individual_student_district.py')



# Awards DistrictBllock student data
os.system('python awards_script_files/awards_individual_student_districtblock.py')


# Block Student Details
os.system('python block_script_files/block_students.py')

# SchoolTeacher Student Details
os.system('python block_script_files/block_schoolTeachers.py')

# Block Details
os.system('python block_script_files/block_block_Details.py')

# State Block Details
os.system('python state_script_files/state_block.py')

# State District Details
os.system('python state_script_files/state_district.py')

# State Users
os.system('python state_script_files/state_users.py')



print("Script completed......")




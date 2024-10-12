# list comprehension

# numbers=[1,2,3,4]
# new_list=[n+1 for n in numbers]
# print(new_list)


# syntax
# newlist=[newitem for item in list]
# names=["shuja","Mariyam","Aqsa"]
# new_list=[name for name in names if len(name)<5]
# print(new_list)

# syntx
# newitem for item in list if test

# dictionary comprehension 
# new_dict={newkey : new_value for item in list }
# new_dict={new_key:new_value for (key,value) in dict.items() if test }

# names=["shuja","Mariyam","Aqsa"]
# import random
# student_scores={student:random.randint(1,100) for student in names}
# print(student_scores)


# passed_students={student:score for (student,score) in student_scores.items() if score>=40}

# print(passed_students)


student_dict={
    "student":["shuja","yusuf","saud"],
    "score":[56,76,80]
}

# for (key,value) in student_dict.items():
#     print(key)

import pandas


student_data_frame=pandas.DataFrame(student_dict)
print(student_data_frame)
# Loop through a dataframe 
# for (key,value) in student_data_frame.items():
#     print(value)


for index,row in student_data_frame.iterrows():
    # print(index)
    # print(row)
    # print(row.score)
    if row.student=="shuja":
        print(row.score)
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

names=["shuja","Mariyam","Aqsa"]
import random
student_scores={student:random.randint(1,100) for student in names}
print(student_scores)


passed_students={student:score for (student,score) in student_scores.items() if score>=40}

print(passed_students)


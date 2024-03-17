
# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇
total_heights=0
no_of_students=0
for height in student_heights:
  total_heights+=height
  no_of_students+=1 
print("total height = "+str(total_heights))
print("number of students = "+str(no_of_students))
average_height=total_heights/no_of_students
print(f"average height = {str(round(average_height))}")
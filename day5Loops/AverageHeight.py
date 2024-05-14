# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
total = 0
for i in student_heights:
    total += i

avg = round(total / len(student_heights))
print("total height = " + str(total))
print("number of students = " + str(len(student_heights)))
print("average height = " + str(avg))
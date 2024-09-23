# numbers = [1,2,3]
# new_numbers = [ n + 1 for n in numbers]
# print(new_numbers)
import random

# name = "Angela"
# new_list = [letter for letter in name]
# print(new_list)

# double_list = [i*2 for i in range(1, 5)]
# print(double_list)
#
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# list_names = [i.upper() for i in names if len(i) > 5]
# print(list_names)

# list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
# numbers = [n for n in list_of_strings if int(n) % 2 != 0]
# result = [n for n in numbers if int(n) % 2 != 0]
# print(result)

# with open("file1.txt") as file1:
#     file1_txt = file1.read()
#     serie_1 = [int(n) for n in file1_txt if n != '\n']
#
#
# with open("file2.txt") as file2:
#     file2_txt = file2.read()
#     serie_2 = [int(n) for n in file2_txt if n != '\n']
#
# result = [n for n in serie_1 and serie_2 if n in serie_1 and serie_2]
#
# print(result)


# with open("file1.txt") as file1:
#     list1 = file1.readlines()
#
# with open("file2.txt") as file2:
#     list2 = file2.readlines()
#
# result = [int(num) for num in list1 if num in list2]
#
# print(result)

# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# students_score = {student: random.randint(1,100) for student in names}
# print(students_score)
# passed_students = {student:score  for student, score in students_score.items() if score > 60}
# print(passed_students)


# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# result = {word:len(word) for  word in sentence.split()}
# print(result)

# weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
#
# weather_f = {day: ((temp * 9/5) + 32) for day, temp in weather_c.items()}
#
# print(weather_f)

import pandas
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# for (key, value) in student_dict.items():
#     print(value)

student_dataframe = pandas.DataFrame(student_dict)
for (key, value) in student_dataframe.iterrows():
     if value.student == "Angela":
         print(value.score)

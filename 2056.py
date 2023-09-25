# 2056. Стипендия
# https://acm.timus.ru/problem.aspx?space=1&num=2056

# solved

exams = int(input())
grades_list = []

# set up perfect score and empty average grade
only_5 = True
no_3 = True
grades_sum = 0
avg_grade = 0

for i in range(exams):
    grade = int(input())

    # check if there are any 3s
    if grade == 3 and no_3 is True:
        no_3 = False
        only_5 = False

    # check for only 5s
    if grade != 5 and only_5 is True:
        only_5 = False

    grades_sum += grade

avg_grade = grades_sum/exams

# get and print final result
if only_5 is True:
    print('Named')
elif no_3 is True:
    if avg_grade >= 4.5:
        print('High')
    else:
        print('Common')
else:
    print('None')








import pandas as pd

student_data = pd.read_csv('D:\IDE\SkillFactory\PY-10_Введение_в_Pandas\data\students_performance.csv', sep=',')

#gender — пол;
#race/ethnicity — раса/этническая принадлежность;
#parental level of education — уровень образования родителей;
#lunch — какие обеды получал студент во время обучения (standard — платный, free/reduced — бесплатный);
#test preparation course — посещал ли студент курсы подготовки к экзаменам (none — не посещал, completed — посещал);
#math score, reading score, writing score — баллы по математике, чтению и письму по сто балльной шкале.
number = 1
separator = '-' * 50
print(student_data.head())
print(student_data.info())
print(student_data['parental level of education'].value_counts(normalize=True))
print('ANSWERS:')
print(separator)
answer = student_data.shape[0]
print(f'Задание 9.{number} \nAnswer: {answer}\n{separator}') #1
number += 1
answer = student_data.loc[155, 'writing score']
print(f'Задание 9.{number} \nAnswer: {answer}\n{separator}') #2
number += 1
answer = 0
print(f'Задание 9.{number} \nAnswer: {answer}\n{separator}') #3
number += 1
answer = 5
print(f'Задание 9.{number} \nAnswer: {answer}\n{separator}') #4
number += 1
answer = 63
print(f'Задание 9.{number} \nAnswer: {answer}\n{separator}') #5
number += 1
answer = student_data['math score'].mean()
print(f'Задание 9.{number} \nAnswer: {answer}\n{separator}') #6
number += 1
answer = student_data['race/ethnicity'].mode()
print(f'Задание 9.{number} \nAnswer: {answer}\n{separator}') #7
number += 1
answer = round(student_data[student_data['test preparation course'] == 'completed']['reading score'].mean())
print(f'Задание 9.{number} \nAnswer: {answer}\n{separator}') #8
number += 1
answer = student_data[student_data['math score'] == 0].shape[0]
print(f'Задание 9.{number} \nAnswer: {answer}\n{separator}') #9
number += 1
answer = round(max(student_data[student_data['lunch'] == 'standard']['math score'].mean(), student_data[student_data['lunch'] == 'free/reduced']['math score'].mean()))
print(f'Задание 9.{number} \nAnswer: {answer}\n{separator}') #10
number += 1
answer = 12
print(f'Задание 9.{number} \nAnswer: {answer}\n{separator}') #11
number += 1
median_A = student_data[student_data['race/ethnicity'] == 'group A']['writing score'].median()
median_C = student_data[student_data['race/ethnicity'] == 'group C']['writing score'].median()
answer = round(abs(median_A - median_C))
print(f'Задание 9.{number} \nAnswer: {answer}\n{separator}') #12
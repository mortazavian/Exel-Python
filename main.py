from openpyxl.chart import BarChart, Series, Reference
from openpyxl import Workbook
import pandas as pd
import openpyxl
from openpyxl.chart import BarChart, Reference


def custom_sort_key(value):
    prefix = value[:3]
    remaining_part = value[3:]
    return (prefix, remaining_part)


print("Please put the excel file in the same folder as main.py")

user_choice = input("What is the extension of the file? \n1.xlsx \n2.csv\n")

name_of_the_file = input("Please enter the name of the file: ")

if int(user_choice) == 1:
    data = pd.read_excel(name_of_the_file)
elif int(user_choice) == 2:
    data = pd.read_csv(name_of_the_file)

# To read the excel file

lst = []

# Add different words to a list(lst)
for i, row in data.iterrows():

    temp = row['ANALYSIS']

    if temp in lst:
        continue
    else:
        lst.append(temp)

print(lst)

rows_to_work_with = []

for i, row in data.iterrows():

    if 'AV' in row['COMPONENT_NAME']:
        rows_to_work_with.append(row)

    if 'SIG' in row['COMPONENT_NAME']:
        rows_to_work_with.append(row)


print(type(rows_to_work_with))

rows_to_work_with = pd.DataFrame(rows_to_work_with)

temp_lst = rows_to_work_with.sort_values(['ANALYSIS', 'TEST_TEMP', 'CONDITION', 'COMPONENT_NAME', 'SEQUENCE_NO'], ascending=[
                                         True, True, True, True, True], na_position='first')


for i, row in temp_lst.iterrows():
    if "AV" in row['COMPONENT_NAME']:
        temp_lst.at[i, 'COMPONENT_NAME'] = temp_lst.at[i,
                                                       'COMPONENT_NAME'][2:] + temp_lst.at[i, 'COMPONENT_NAME'][0:2]
    if "SIG" in row['COMPONENT_NAME']:
        temp_lst.at[i, 'COMPONENT_NAME'] = temp_lst.at[i,
                                                       'COMPONENT_NAME'][3:] + temp_lst.at[i, 'COMPONENT_NAME'][0:3]

# temp_lst = rows_to_work_with.sort_values(['ANALYSIS','TEST_TEMP','CONDITION','COMPONENT_NAME','SEQUENCE_NO'], ascending=[True,True,True,True,True],na_position='first')

temp_lst = temp_lst.sort_values(['ANALYSIS', 'TEST_TEMP', 'CONDITION', 'COMPONENT_NAME', 'SEQUENCE_NO'], ascending=[
                                True, True, True, True, True], na_position='first')

for i, row in temp_lst.iterrows():
    if "AV" in row['COMPONENT_NAME']:
        temp_lst.at[i, 'COMPONENT_NAME'] = temp_lst.at[i,
                                                       'COMPONENT_NAME'][-2:] + temp_lst.at[i, 'COMPONENT_NAME'][0:-2]
    if "SIG" in row['COMPONENT_NAME']:
        temp_lst.at[i, 'COMPONENT_NAME'] = temp_lst.at[i,
                                                       'COMPONENT_NAME'][-3:] + temp_lst.at[i, 'COMPONENT_NAME'][0:-3]

temp_lst = temp_lst[['ANALYSIS', 'SEQUENCE_NO', 'COMPONENT_NAME',
                     'RESULT_VALUE', 'UNITS', 'TEST_TEMP', 'CONDITION']]


temp_lst.insert(4, "SIG-RES", 0)

lst_sig = []

for i, row1 in temp_lst.iterrows():
    found = False
    if 'AV' in row1['COMPONENT_NAME']:
        for j, row2 in temp_lst.iterrows():
            if row2['COMPONENT_NAME'][3:] == row1['COMPONENT_NAME'][2:]:
                lst_sig.append(row2['RESULT_VALUE'])
                found = True
                break
        if not found:
            temp_lst = temp_lst.drop(i)


# for i, row1 in temp_lst.iterrows():
#     found = False
#     if 'SIG' in row1['COMPONENT_NAME']:
#         for j, row2 in temp_lst.iterrows():
#             if row2['COMPONENT_NAME'][3:] == row1['COMPONENT_NAME'][2:]:
#                 lst_sig = lst_sig.append(row2)
#                 found = True
#                 break
#         if not found:
#             temp_lst.drop(row1)


for i, row in temp_lst.iterrows():
    if "SIG" in row['COMPONENT_NAME']:
        temp_lst = temp_lst.drop(i)


temp_lst['SIG-RES'] = lst_sig

temp_lst.to_excel("output.xlsx")


print("============================")
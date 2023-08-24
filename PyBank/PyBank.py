#!/usr/bin/env python
# coding: utf-8

# In[22]:


import os
import csv

csvpath = os.path.join('.', 'Resources', 'budget_data.csv')

with open(csvpath, 'r') as file_handler:
    csvreader = csv.reader(file_handler, delimiter=',')
    csv_header = next(csvreader)

    dates_list = []
    gains_list = []

    for row in csvreader:
        date = row[0]
        gain = row[1]
    
        dates_list.append(date)
        gains_list.append(float(gain))

delta_list_2 = []

for i in range(len(gains_list)-1):

    delta_2 = gains_list[i+1] - gains_list[i]
    delta_list_2.append(delta_2)

output = (
    f"Total Months: {len(dates_list)}\n"
    f"Total: {sum(gains_list)}\n"
    f"Average Change: {round((sum(delta_list_2) / len(delta_list_2)),2)}\n"
    f"Total: {dates_list[delta_list_2.index(max(delta_list_2))+1]} {max(delta_list_2)}\n"
    f"Total: {dates_list[delta_list_2.index(min(delta_list_2))+1]} {min(delta_list_2)}\n"
)

print(output)

txt_file_path = os.path.join("./analysis/PyBank_Analysis.txt")

# print(txt_file_path)

with open(txt_file_path, 'w') as txt_file:
    txt_file.write(output)
    
    


# In[ ]:





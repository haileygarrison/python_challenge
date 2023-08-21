#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import csv

csvpath = os.path.join('.', 'Resources', 'budget_data.csv')

with open(csvpath, 'r') as file_handler:
    lines = file_handler.read()
  


# In[2]:


dates_list = []
gains_list = []

chopped_into_rows = lines.split("\n")


for row in chopped_into_rows:
    
    chopped_into_cols = row.split(",")
    date = chopped_into_cols[0]
    gain = chopped_into_cols[1]
    

    if "Date" in date:
        continue
    if "Profit/Losses" in gain:
        continue
    
    dates_list.append(date)
    gains_list.append(float(gain))
  


# In[3]:


delta_list = []

for i in range(len(gains_list)-1):
        
    delta = gains_list[i] - gains_list[i-1] 
    delta_list.append(delta)
    
    


# In[4]:


output = (
    f"Total Months: {len(dates_list)}\n"
    f"Total: {sum(gains_list)}\n"
    f"Average Change: {round(sum(delta_list) / len(delta_list),2)}\n"
    f"Total: {dates_list[delta_list.index(max(delta_list))]} {max(delta_list)}\n"
    f"Total: {dates_list[delta_list.index(min(delta_list))]} {min(delta_list)}\n"
)


# In[5]:


print(output)


# In[6]:


txt_file_path = os.path.join("./analysis/PyBank_Analysis.txt")

# print(txt_file_path)

with open(txt_file_path, 'w') as txt_file:
    txt_file.write(output)
    
    
    


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import csv

csv_path = os.path.join('.','Resources','election_data.csv')

total_votes = 0

c = []
d = {}

with open(csv_path, 'r') as file_handler:
    
    csvreader = csv.reader(file_handler, delimiter=',')
    csv_header = next(csvreader)
    for row in csvreader:
        total_votes+=1
        c_name = row[2]
        if c_name not in c:
            c.append(c_name)
            d[c_name]=1
        else:d[c_name] += 1

max_val = 0
output_1 =""
for key,value in d.items():
    if value > max_val:
        max_val = value
        winner = key
    
    percent = round((value / total_votes) * 100) 
    output_1 += (f"{key}: {percent}% ({value})\n")

output_2 = (f"The winner is {winner}!")    

print(f"Total Votes: {total_votes}")
print(output_1)
print(output_2)

txt_file_path = os.path.join("./analysis/PyPoll_Analysis.txt")

with open(txt_file_path, 'w') as txt_file:
    
    txt_file.write(f"Total Votes: {total_votes}\n")
    txt_file.write(output_1)
    txt_file.write(output_2)
        


# In[ ]:





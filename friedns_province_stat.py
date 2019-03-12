# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 15:07:52 2019

@author: Ken

Name: receiving the information, mainly the province,  from your frineds list 
    in wechat with plotting in pie chart.
    
input:
    1. login in with QRcode
    2. the boundary of defining as 'others' in pie chart
        ( in the mid-part of the code with ******)

output:
    1. 'friends_province_total.csv'
    2. 'friends_province_count.csv'
    3. 'frineds_province_pie_chart.png'
     
"""

import itchat 

itchat.login()

friends = itchat.get_friends(update=True)[0:]

def get_var(var):
    variable = []
    for i in friends:
        value = i[var]
        variable.append(value)
    return variable

# receiving data
NickName = get_var("NickName")
Sex = get_var("Sex")
Province = get_var("Province")
#City = get_var("City")
#Signature = get_var("Signature")


# saving as csv file.
from pandas import DataFrame
data = {'NickName':NickName,'Sex':Sex, 
        'Province':Province
        #,'City':City,'Signature' : Signature
        }

frame = DataFrame(data)
frame.to_csv('friends_province_total.data.csv', index = True, encoding='utf-32')

# counting the number of people in each province.
prov_data = frame['Province'].value_counts()

prov_count = prov_data.tolist()
prov_name = prov_data.index.tolist()

prov_name[prov_name.index('')] = 'Unknown'    # emending the '' , 
# which means the person do not provide the province, into 'Unknown'
prov_data = {"ProvName" : prov_name, 'ProvCount' : prov_count }
frame_p = DataFrame(prov_data)
frame_p.to_csv('friends_province_count.csv', index = False, encoding='utf-32')

#plotting
import matplotlib.pyplot as plt 

plt.rcParams['font.sans-serif']=['SimHei']  # to solve the problem of displaying chinese

# set up a variable 'other'n.
other_count = 0
other_list = []
for x,y in list(zip(prov_name,prov_count)):
    if y <= 5 :     # aggragating the provinces that is below than 5 people into one part.
        # *****you can change the parameter above.
        other_count += 1
        other_list.append(x)
print(other_list)

# rearrage the labels and sizes for plotting pie chart
labels = [ x for x in prov_name if x not in other_list]
labels.append('others')
sizes = prov_count[0:len(labels)-1]
sizes.append(other_count)

fig1, ax1 = plt.subplots()
patches, wages , autotexts = ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.setp(autotexts, size=8, weight="bold")
ax1.set_title("Frineds' Province Ratio")
plt.savefig('frineds_province_pie_chart.png',dpi = 250)
plt.show()


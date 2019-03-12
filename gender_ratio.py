# -*- coding: utf-8 -*-
import itchat
itchat.login()

friends = itchat.get_friends(update=True)[0:]

male = female =other = 0

for i in friends[1:]:   # the f[0] is yourself
    sex = i["Sex"]
    if sex ==1:
        male+=1
    elif sex==2:
        female+=1
    else:
        other+=1
    
total = len(friends[1:])

print("male friends : {}".format(male))
print("female friends : {}".format(female))
print("unknown gender friends : {}".format(other))

import numpy as np
import matplotlib.pyplot as plt

labels = ['male','female','unknown']
X = [male,female,other]

fig = plt.figure() # The purpose of using plt.figure() is to create a figure object.

plt.pie(X,labels = labels, autopct = '%.2f %%' )
# "autopct" enables you to display the percent value using Python string formatting 

plt.title('gender ratio')
plt.savefig("gender_ratio.png",dpi = 250)
itchat.send_image("gender_ratio.png",toUserName='filehelper')
plt.show()

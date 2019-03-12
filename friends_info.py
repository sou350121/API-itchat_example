# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 12:52:26 2019

@author: Ken

Name: receiving the information from your frineds list in wechat 
    
input:
    1. login in with QRcode
output:
    1. 'friends_stat_data.csv'
     
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
City = get_var("City")
Signature = get_var("Signature")


# saving as csv file.
from pandas import DataFrame
data = {'NickName':NickName,'Sex':Sex, 'Province':Province,'City':City,
        'Signature' : Signature}

frame = DataFrame(data)
frame.to_csv('friends_stat.data.csv', index = True, encoding='utf-32')


# done 



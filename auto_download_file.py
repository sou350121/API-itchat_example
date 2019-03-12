# -*- coding: utf-8 -*-

import itchat


from itchat.content import *

@itchat.msg_register([PICTURE,RECORDING, ATTACHMENT,VIDEO])
def download_file(msg):
    # msg['Text'] is a function that download the file accoring to the name.
    msg['Text'](msg['FileName'])
    print(msg['FileName'], msg.fromUserName)

   #return '@%s@%s' % ({'Picture':'img','Video','vid'}.get(msg['Type'],'fil'),
                      #msg['FileName'])
    
itchat.auto_login()
itchat.run()


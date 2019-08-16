import itchat

'''
给别人发消息
'''
import itchat
import time

i = 0
itchat.auto_login()
while i < 60:
    user2 = itchat.search_friends(name=u'XXX') #  UserName
    print(user2)
    userName2 = user2[0]['UserName']
    msg = ''
    itchat.send(msg, toUserName=userName2)
    time.sleep(1)
    i += 1
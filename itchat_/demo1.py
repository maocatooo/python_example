import itchat

'''
别人给你发消息时候会自动回复！
群聊没效果
监测不到表情包的发送
'''
@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    message = msg['Text']
    print(msg)
    print(message)
    replay = message

    return replay


itchat.auto_login()
itchat.run()

import smtplib
from email import utils
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# 发件人地址，通过控制台创建的发件人地址
username = ''
# 发件人密码，通过控制台创建的发件人密码
password = ''
replyto = ''
SMTP_HOST = "smtpdm.aliyun.com"


def send_mail(email, content):

    # 自定义的回复地址

    # 收件人地址或是地址列表，支持多个收件人，最多30个
    # receivers = ['zk246422@163.com']
    # rcptto = ','.join(receivers)
    rcptto = email
    # 构建alternative结构
    msg = MIMEMultipart('alternative')
    msg['Subject'] = Header('早上好！').encode()
    msg['From'] = '%s <%s>' % (Header('邮件').encode(), username)
    msg['To'] = rcptto
    msg['Reply-to'] = replyto
    msg['Message-id'] = utils.make_msgid()
    msg['Date'] = utils.formatdate()
    # 构建alternative的text/plain部分
    # textplain = MIMEText('你好哦1', _subtype='plain', _charset='UTF-8')
    # msg.attach(textplain)
    # 构建alternative的text/html部分
    texthtml = MIMEText(content, _subtype='html', _charset='UTF-8')
    msg.attach(texthtml)
    # 发送邮件
    try:
        # client = smtplib.SMTP()
        # python 2.7以上版本，若需要使用SSL，可以这样创建client
        client = smtplib.SMTP_SSL(host=SMTP_HOST)
        # smtplib.SMTP_SSL(host='smtp.gmail.com').connect(host='smtp.gmail.com', port=465)
        # SMTP普通端口为25或80
        client.connect(SMTP_HOST, 465)
        # 开启DEBUG模式
        client.set_debuglevel(0)
        client.login(username, password)
        # 发件人和认证地址必须一致
        # 备注：若想取到DATA命令返回值,可参考smtplib的sendmaili封装方法:
        #      使用SMTP.mail/SMTP.rcpt/SMTP.data方法
        client.sendmail(username, rcptto, msg.as_string())
        # 支持多个收件人
        # client.sendmail(username, receivers, msg.as_string())
        client.quit()
        print('邮件发送成功！')
    except smtplib.SMTPConnectError as e:
        print('邮件发送失败，连接失败:', e.smtp_code, e.smtp_error)
    except smtplib.SMTPAuthenticationError as e:
        print('邮件发送失败，认证错误:', e.smtp_code, e.smtp_error)
    except smtplib.SMTPSenderRefused as e:
        print('邮件发送失败，发件人被拒绝:', e.smtp_code, e.smtp_error)
    except smtplib.SMTPRecipientsRefused as e:
        print('邮件发送失败，收件人被拒绝:', e.smtp_code, e.smtp_error)
    except smtplib.SMTPDataError as e:
        print('邮件发送失败，数据接收拒绝:', e.smtp_code, e.smtp_error)
    except smtplib.SMTPException as e:
        print('邮件发送失败, ', e.message)
    except Exception as e:
        print('邮件发送异常, ', str(e))


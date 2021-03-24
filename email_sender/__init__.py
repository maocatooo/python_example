from email_sender.render import render
from email_sender.sender import send_mail

params = {
    "h1": "this is h1 label",
    "content": " hi , it's test send email",
    "url": "https://www.baidu.com/"
}
if __name__ == "__main__":
    content = render(params)
    send_mail("zk246422@163.com", content)


import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.image import MIMEImage
import mimetypes
import os



# 第三方 SMTP 服务
mail_host = "smtp.qq.com"  # 设置服务器
mail_user = "xxx"  # 用户名
mail_pass = "xxx"  # 口令

sender = 'xxx'
receivers = ['xxx']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

# 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
# message = MIMEText('Python邮件', 'plain', 'utf-8')
#创建一个带附件的实例
message = MIMEMultipart()
message['From'] = Header("xxx", 'utf-8')
message['To'] = Header("xxx", 'utf-8')
# 邮件主题
subject = '邮件'
message['Subject'] = Header(subject, 'utf-8')
# 邮件正文内容
message.attach(MIMEText('这是Python 邮件发送附件内容……', 'plain', 'utf-8'))

'''
在python中，MIME的这些对象的继承关系如下。
MIMEBase
    |-- MIMENonMultipart
        |-- MIMEApplication
        |-- MIMEAudio
        |-- MIMEImage
        |-- MIMEMessage
        |-- MIMEText
    |-- MIMEMultipart
构造MIMEApplication对象做为文件附件内容并附加到根容器
#不管什么类型的附件，都用MIMEApplication，MIMEApplication默认子类型是application/octet-stream。
'''
def getAttachment(FilePath):  # 获取附件，参数：文件路径
    contentType, encoding = mimetypes.guess_type(FilePath)  # 根据 guess_type方法判断文件的类型和编码方式

    if contentType is None or encoding is not None:  # 如果根据文件的名字/后缀识别不出是什么文件类型
        contentType = 'application/octet-stream'   # 使用默认类型，usable for a MIME content-type header.

    mainType, subType = contentType.split('/', 1)  # 根据contentType 判断主类型与子类型
    if mainType == 'image':  # 图片
        fileApart = MIMEImage(open(FilePath, 'rb').read())
    else:
        fileApart = MIMEApplication(open(FilePath, 'rb').read())
    fileApart.add_header('Content-Disposition', 'attachment', filename=os.path.basename(FilePath))
    return fileApart


for attachmentFilePath in ['1547530138133.jpg','SearchCount.txt','python.pdf']:  # 判断添加哪些附件
    message.attach(getAttachment(attachmentFilePath))

#message.attach(fileApart) #如果入参给定附件文件，使用attach 发放添加msg头信息

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    smtpObj.close()  # 关闭邮件发送服务
    print("邮件发送成功")
except smtplib.SMTPException as e:
    print(e)
    print("Error: 无法发送邮件")

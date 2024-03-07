import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from datetime import datetime, timedelta
from settings import Config
import random
import string
import uuid

# app配置信息
config = Config

'''
项目中使用的的一些工具函数
'''
# 检测上传文件扩展名是否合法
def upload_testing(filename:str):
    if filename == '' or '.' not in filename:
        return 0
    ext = filename.rsplit('.', 1)[1].lower() # 获取文件扩展名
    if ext not in config.ALLOWED_EXTENSIONS:
        return 0
    return ext

# 生成邮箱验证码（默认5位，字母+数字）
def generate_vrfcode(length:int=5):
    num_count = random.randint(2, 3)
    char_count = length - num_count

    nums = [random.choice(string.digits) for _ in range(num_count)]
    chars = [random.choice(string.ascii_uppercase) for _ in range(char_count)]

    vrfcode = ''.join(random.sample(nums + chars, length))

    return vrfcode

# 生成指定长度的随机字符串
def generate_string(length:int):
    abstring = str(uuid.uuid4().hex)[:length]
    return abstring

# 服务器发送验证码邮件
def send_email(receiver:str):
    vrfcode = generate_vrfcode()
    try:
        content = f'This is your verification code: {vrfcode}. It will expire in 5 minutes.' # content内容可使用HTML代码进行填充
        msg = MIMEText(content, 'html', 'utf-8')
        msg['From'] = formataddr(['VoxTracerWeb', config.SERVER_EMAIL_ADDRESS]) # 发送者
        msg['To'] = formataddr([receiver, receiver]) # 接收者
        msg['Subject'] = 'VoxTracerWeb Register Verification' # 邮件主题

        server = smtplib.SMTP_SSL('smtp.163.com', 465)
        server.login(config.SERVER_EMAIL_ADDRESS, config.SERVER_EMAIL_PASSWORD)
        server.sendmail(config.SERVER_EMAIL_ADDRESS, [receiver], msg.as_string())
        server.quit()
        send_time = datetime.now()
        return vrfcode, send_time
    except Exception:
        return 0
    
# 检查验证码有效时间
def check_expire(send_time:str, limit:int):
    if datetime.now() - send_time.replace(tzinfo=None) <= timedelta(seconds=limit):
        return 1
    return 0
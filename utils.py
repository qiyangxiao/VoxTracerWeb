from datetime import datetime, timedelta
from email.mime.text import MIMEText
from email.utils import formataddr
import hashlib
from jinja2 import Environment, FileSystemLoader
import random
import smtplib
import string
import uuid

from config import Config

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
def generate_captcha(length:int=5):
    num_count = random.randint(2, 3)
    char_count = length - num_count

    nums = [random.choice(string.digits) for _ in range(num_count)]
    chars = [random.choice(string.ascii_uppercase) for _ in range(char_count)]

    captcha = ''.join(random.sample(nums + chars, length))

    return captcha

# 生成指定长度的随机字符串
def generate_abstring(length:int):
    abstring = str(uuid.uuid4().hex)[:length]
    return abstring

# 服务器发送验证码邮件
def send_email(receiver:str):
    captcha = generate_captcha()
    try:
        content = templateHTML({'captcha':captcha}, './templates')
        msg = MIMEText(content, 'html', 'utf-8')
        msg['From'] = formataddr(['VoxTracerWeb', config.SERVER_EMAIL_ADDRESS]) # 发送者
        msg['To'] = formataddr([receiver, receiver]) # 接收者
        msg['Subject'] = 'VoxTracerWeb Register Verification' # 邮件主题

        server = smtplib.SMTP_SSL('smtp.163.com', 465)
        server.login(config.SERVER_EMAIL_ADDRESS, config.SERVER_EMAIL_PASSWORD)
        server.sendmail(config.SERVER_EMAIL_ADDRESS, [receiver], msg.as_string())
        server.quit()
        send_time = datetime.now()
        return captcha, send_time
    except Exception:
        return 0
    
# 检查验证码有效时间
def check_expire(send_time:str, limit:int):
    if datetime.now() - send_time.replace(tzinfo=None) <= timedelta(seconds=limit):
        return 1
    return 0

# 密码转化为sha256字符串
def sha256str(input:str):
    output = hashlib.sha256(input.encode('utf-8')).hexdigest()
    return output

def templateHTML(input:str, template_path:str):
    env = Environment(loader=FileSystemLoader(template_path))
    template = env.get_template('captcha.html')
    html_content = template.render(input)
    return html_content


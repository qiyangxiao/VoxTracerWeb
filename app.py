import hashlib
import os
import shutil

from flask import Flask, jsonify, redirect, render_template, request, send_file, session, url_for
from flask_migrate import Migrate
from werkzeug.utils import secure_filename

from models import User, db
from settings import Config
from utils import generate_string, send_email, upload_testing

# 创建Flask应用
app = Flask(__name__)
# 加载配置信息
app.config.from_object(Config)
# 初始化数据库
db.init_app(app)
migrate = Migrate(app, db)
with app.app_context():
    db.create_all()

'''
网站路由逻辑函数
'''
# 根目录访问
@app.route('/')
def index():
    uid = session.get('uid')
    return render_template('index.html', uid=uid)

# 上传音频处理
@app.route('/upload', methods=['POST'])
def upload():
    upload_file = request.files['audio_input']
    info = {}
    ext = upload_testing(secure_filename(upload_file.filename))
    if ext == 0:
        info['message'] = '文件上传失败！'
        return jsonify(info)
    # 重命名文件
    filename = f'{generate_string(8)}.{ext}'
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    upload_file.save(file_path)
    session['uploaded_filepath'] = file_path
    info['message'] = f'文件上传成功！'
    return jsonify(info)

# 下载音频处理
@app.route('/download/<filename>/<idx>')
def download(filename:str, idx:str):
    idx = int(idx)
    file_path = os.path.join(app.config['FILE_FOLDERS'][idx], filename) # idx表示下载哪个路径下的文件
    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True)
    else:
        return 'File Not Found', 404

# 音频转换处理
@app.route('/convert')
def convert():
    # 获取上传的文件，文件路径及其文件名
    uploaded_filepath = session.get('uploaded_filepath')
    uploaded_filename = os.path.basename(uploaded_filepath)
    info = {}
    if uploaded_filename:
        # voice convert操作...

        # 构造新的文件名：原文件名_conv
        split_name = uploaded_filename.rsplit('.', 1)
        converted_filename = split_name[0] + '_conv' + '.' + split_name[1].lower()

        # 设置转换音频的存储路径并保存
        converted_filepath = os.path.join(app.config['DOWNLOAD_FOLDER'], converted_filename)
        shutil.copy(uploaded_filepath, converted_filepath) #这里简化为直接复制
        session['converted_filepath'] = converted_filepath
        info['message'] = '转换成功！'
        info['file_url'] = url_for('download', filename=converted_filename, idx=1)
    else:
        info['message'] = '出了点问题，请重新上传！'
    return jsonify(info)

# 模拟压缩处理
@app.route('/compress')
def compress():
    converted_filepath = session.get('converted_filepath')
    converted_filename = os.path.basename(converted_filepath)
    info = {}
    if converted_filename:
        # 音频压缩操作...

        # 构造新的文件名：原文件名_comp
        split_name = converted_filename.rsplit('.', 1)
        compressed_filename = split_name[0] + '_comp' + '.' + split_name[1].lower()

        # 设置压缩音频的存储路径并保存
        compressed_filepath = os.path.join(app.config['COMPRESS_FOLDER'], compressed_filename)
        shutil.copy(converted_filepath, compressed_filepath)
        session['compressed_filepath'] = compressed_filepath
        info['message'] = '压缩成功！'
        info['file_url'] = url_for('download', filename=compressed_filename, idx=2)
    else:
        info['message'] = '压缩出了点问题，请重试！'
    return jsonify(info)

# 说话人身份验证处理
@app.route('/identify')
def identify():
    compressed_filepath = session.get('compressed_filepath')
    info = {}
    info['message'] = '验证成功！'
    info['speaker_id'] = '12345678'
    return jsonify(info)

# 加载登录页面
@app.route('/login.html')
def login_html():
    return render_template('login.html')

# 加载注册页面
@app.route('/register.html')
def register_html():
    return render_template('register.html')

# 登录信息验证
@app.route('/login', methods=['POST'])
def login():
    # 获取用户名和密码
    uid = request.form['uid']
    pwd = hashlib.sha256(request.form['pwd'].encode('utf-8')).hexdigest() #sha256

    # 查询数据库
    user = User.query.filter_by(uid=uid).first()
    info = {}
    if user and user.pwd == pwd:
        session['uid'] = uid
        return redirect(url_for('index'))
    else:
        info['message'] = '用户名或密码有误！'
        return jsonify(info)

# 注册信息验证
@app.route('/register', methods=['POST'])
def register():
    # 获取注册表单信息
    email = request.form['email']
    pwd = hashlib.sha256(request.form['pwd'].encode('utf-8')).hexdigest()
    vrfcode = request.form['vrfcode']

    my_vrfcode = session.get('vrfcode')
    info = {}
    # 检查是否是已经存在的用户
    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        info['message'] = '该邮箱已经被注册过了！'
        return jsonify(info)

    # 检查验证码（邮箱是否真实存在）
    if vrfcode != my_vrfcode:
        info['message'] = '验证码错误！'
        return jsonify(info)
    else:
        uid = generate_string(6) # 生成uid
        # 向数据库添加一条user记录
        new_user = User(uid=uid, pwd=pwd, email=email)
        db.session.add(new_user)
        db.session.commit()
        
        info['message'] = f'注册成功，你的uid为{uid}，请牢记！'
        return jsonify(info)

# 邮箱验证码发送
@app.route('/sendcode', methods=['POST'])
def sendcode():
    info = {}
    receiver_email = request.get_json()['email']
    vrfcode = send_email(receiver_email)
    if vrfcode:
        session['vrfcode'] = vrfcode
        info['message'] = '验证码发送成功，请查看收件箱或检查垃圾邮箱！'
    else:
        info['message'] = '出了点问题，请重试！'
    return jsonify(info)

if __name__ == '__main__':
    app.run(debug=True)
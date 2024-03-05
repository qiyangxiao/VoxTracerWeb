from flask import Flask, render_template, request, jsonify, session, send_file, url_for
from werkzeug.utils import secure_filename
from settings import Config
from flask_migrate import Migrate
from models import db
import os
import shutil
import uuid

# 创建Flask应用
app = Flask(__name__)
# 加载配置信息
app.config.from_object(Config)
# 初始化数据库
db.init_app(app)
migrate = Migrate(app, db)


'''
为方便编程而封装的函数
'''
# 检测音频文件是否符合规范
def upload_testing(filename:str):
    if filename == '' or '.' not in filename:
        return 0
    ext = filename.rsplit('.', 1)[1].lower() # 获取文件扩展名
    if ext not in app.config["ALLOWED_EXTENSIONS"]:
        return 0
    return ext

'''
网站路由逻辑函数
'''
# 根目录访问
@app.route('/')
def index():
    return render_template("index.html")

# 上传音频处理
@app.route('/upload', methods=['POST'])
def upload():
    upload_file = request.files['audio_input']
    info = {}
    ext = upload_testing(secure_filename(upload_file.filename))
    if ext == 0:
        info["message"] = "文件上传失败！"
        return jsonify(info)
    # 重命名文件
    filename = f"{uuid.uuid1().hex}.{ext}"
    file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    upload_file.save(file_path)
    session['uploaded_filepath'] = file_path
    info["message"] = f"文件上传成功！"
    return jsonify(info)

# 下载音频处理
@app.route('/download/<filename>/<idx>')
def download(filename:str, idx:str):
    idx = int(idx)
    file_path = os.path.join(app.config["FILE_FOLDERS"][idx], filename) # idx表示下载哪个路径下的文件
    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True)
    else:
        return "File Not Found", 404

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
        converted_filename = split_name[0] + "_conv" + "." + split_name[1].lower()

        # 设置转换音频的存储路径并保存
        converted_filepath = os.path.join(app.config["DOWNLOAD_FOLDER"], converted_filename)
        shutil.copy(uploaded_filepath, converted_filepath) #这里简化为直接复制
        session["converted_filepath"] = converted_filepath
        info["message"] = "转换成功！"
        info["file_url"] = url_for('download', filename=converted_filename, idx=1)
    else:
        info["message"] = "出了点问题，请重新上传！"
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
        compressed_filename = split_name[0] + "_comp" + "." + split_name[1].lower()

        # 设置压缩音频的存储路径并保存
        compressed_filepath = os.path.join(app.config["COMPRESS_FOLDER"], compressed_filename)
        shutil.copy(converted_filepath, compressed_filepath)
        session["compressed_filepath"] = compressed_filepath
        info["message"] = "压缩成功！"
        info["file_url"] = url_for('download', filename=compressed_filename, idx=2)
    else:
        info["message"] = "压缩出了点问题，请重试！"
    return jsonify(info)

# 说话人身份验证处理
@app.route('/identify')
def identify():
    compressed_filepath = session.get('compressed_filepath')
    info = {}
    info["message"] = "验证成功！"
    session["speaker_id"] = 1234
    return jsonify(info)


if __name__ == "__main__":
    app.run(debug=True)
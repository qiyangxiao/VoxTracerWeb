class Config:
    SECRET_KEY = 'your session key' # session秘钥
    ALLOWED_EXTENSIONS = {'mp3', 'wav', 'aac', 'flac', 'm4a'}
    ALLOWED_STATICFILES = {'favicon.ico', 'manifest.json', 'logo192.png', 'logo512.png'}
    UPLOAD_FOLDER = 'audio/upload/'
    DOWNLOAD_FOLDER = 'audio/converted/'
    COMPRESS_FOLDER = 'audio/compressed/'
    FILE_FOLDERS = [UPLOAD_FOLDER, DOWNLOAD_FOLDER, COMPRESS_FOLDER]
    SQLALCHEMY_DATABASE_URI = 'sqlite:///voxtracer.db' # sqlite中instance目录为默认根目录
    SQLALCHEMY_TRACK_MODIFICATIONS = False # 禁用数据库模型修改监控
    SERVER_EMAIL_ADDRESS = 'your server email address' # 服务器邮箱
    SERVER_EMAIL_PASSWORD = 'your authentication code' # 服务器STMP授权码
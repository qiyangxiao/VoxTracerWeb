class Config:
    SECRET_KEY = 'icckcfd20zzq523v4hawtdce76p2i7ar'
    ALLOWED_EXTENSIONS = {'mp3', 'wav', 'aac', 'flac', 'm4a'}
    UPLOAD_FOLDER = 'audio/upload/'
    DOWNLOAD_FOLDER = 'audio/converted'
    COMPRESS_FOLDER = 'audio/compressed'
    FILE_FOLDERS = [UPLOAD_FOLDER, DOWNLOAD_FOLDER, COMPRESS_FOLDER]
    SQLALCHEMY_DATABASE_URI = 'sqlite:///instance/voxtracer.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False # 禁用数据库模型修改监控
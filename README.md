# VoxTracerWeb

本项目是基于VoxTracer(ACM MM 2023)实现的应用网页系统。主要包括音频变声转换，音频传输压缩和说话人溯源3大功能。VoxTracer项目官方代码可访问[https://github.com/hongchengzhu/VoxTracer](https://github.com/hongchengzhu/VoxTracer)查看。

## 使用教程

本项目网站采用的是Python编写的轻量级web开发框架**Flask(version 3.0.2)**。

你可以在终端输入如下命令以运行本项目：

```
cd VoxTracerWeb
python app.py
```

本项目使用的是Python自带的轻量级数据库sqlite3，数据库的初始化会在`python app.py`执行。具体的数据库配置可在settings.py和models.py修改。然后，你可以在终端使用如下命令操作数据库：

```
sqlite3 instance/voxtracer.db
```
**More contents remain to be added...**

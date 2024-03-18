# VoxTracerWeb

本项目是基于 VoxTracer(ACM MM 2023) 实现的应用网页系统。主要包括音频变声转换，音频传输压缩和说话人溯源 3 大功能。 VoxTracer 项目官方代码可访问[https://github.com/hongchengzhu/VoxTracer](https://github.com/hongchengzhu/VoxTracer)查看。

## 使用教程

本项目网站采用 Flask（后端） + React（前端） 编写，以实现前后端分离。

你可以下载本项目的 zip 包或者在终端使用命令来在本地运行项目

```
git clone https://github.com/qiyangxiao/VoxTracerWeb.git
```

然后，你可以在终端输入如下命令以运行本项目：

```
cd VoxTracerWeb
python app.py
```

### Flask 部分说明

+ 后端使用的是 Python 自带的轻量级数据库 sqlite3 ，数据库的初始化会在`python app.py`执行。具体的数据库配置可在 config.py 和 models.py 修改。然后，你可以在终端使用如下命令操作数据库：

```
sqlite3 instance/voxtracer.db
```

+  app.py 主要是路由选择函数的设计，具体可以结合 frontend/src 的内容分析；

+  config.py 文件包含了后端 app 的配置信息，包括 session 密钥，STMP 授权码等信息；

+  templates/captcha.html 为发送验证码邮件的渲染文件，你可以修改这个文件来设计你的邮件样式；

### React 部分说明

本项目使用的框架理念使得前后端的设计可以基本分离，前端设计在 /frontend 目录下。为了解代码逻辑和目录结构，你可能需要了解[React 官方文档](https://react.docschina.org/)。

+ 当你修改了前端文件后，请在终端输入以下命令，将前端内容更新到 templates/ , static/ （build 操作可以在 frontend/package.json 进行修改，目前仅适配了 Windows 平台的 build 方法；）

```
cd frontend
npm run build
```

+ src/pages：页面设置；src/components：封装的组件； router.js：前端路由；style.js：自定义的组件样式；utils.js：封装的工具函数

**More contents remain to be added...**

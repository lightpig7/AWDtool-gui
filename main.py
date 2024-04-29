import os
import webview
from flask import Flask, render_template

from API.Api import Api

app = Flask(__name__, template_folder='static', static_folder='static/assets')  # 创建一个应用


@app.route('/')
def index():  # 定义根目录处理器
    print(os.path.dirname(os.path.abspath(__file__)))
    return render_template('index.html')  # 模板文件路径是相对于 'templates' 文件夹的


if __name__ == '__main__':
    window = webview.create_window('AWDtool-gui', app, height=700, width=1000, resizable=False, min_size=(1000, 700),
                                   js_api=Api())
    webview.start(debug=True,args='--disable-web-security')

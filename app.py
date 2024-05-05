import os

from flask import Flask, render_template, request

from API.down_file import down_file
from API.getFlag import check_web_service

app = Flask(__name__, template_folder='static', static_folder='static/assets')  # 创建一个应用


@app.route('/')
def index():  # 定义根目录处理器
    print(os.path.dirname(os.path.abspath(__file__)))
    return render_template('index.html')  # 模板文件路径是相对于 'templates' 文件夹的


@app.route('/api_flag')
def api_flag():
    url = request.args.get('url')
    param = request.args.get('param')
    method = request.args.get('method')
    header = request.args.get('header')
    return check_web_service(url, param, method, header)

@app.route('/down_file')
def api_down_file():
    content = request.args.post('strr')
    file_name = request.args.post('file_name')
    return down_file(content , file_name)
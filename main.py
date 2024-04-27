import os
import re

import webview
from flask import Flask, render_template, jsonify, request

from change_passsword import ssh_changepasswd, ssh_changemorepasswd

app = Flask(__name__, template_folder='static', static_folder='static/assets')  # 创建一个应用


@app.route('/')
def index():  # 定义根目录处理器
    print(os.path.dirname(os.path.abspath(__file__)))
    return render_template('index.html')  # 模板文件路径是相对于 'templates' 文件夹的

class Api():
    def chage_passwd(self, host, port, username, password, new_password):
        if host == '':
            host = '192.168.52.143'
        if port == '':
            port = 22
        if username == '':
            username = 'ubuntu'
        if password == '':
            password = '123456'
        if new_password == '':
            new_password = 'peiqi7@987'
        s = ssh_changepasswd(host, port, username, password, new_password)
        print(s)
        return s
    def change_morepasswd(self, host, port, username, password, new_password,thread):
        if host == '':
            host = '192.168.52.143'
        if port == '':
            port = 22
        if username == '':
            username = 'ubuntu'
        if password == '':
            password = '123456'
        if new_password == '':
            new_password = 'peiqi7@987'
        s = ssh_changemorepasswd(host, port, username, password, new_password,thread)
        print(s)
        return s


if __name__ == '__main__':
    window = webview.create_window('AWDtool-gui', app, height=530, width=800, resizable=False, min_size=(800, 500),
                                   js_api=Api())
    # result = window.evaluate_js('import emitter from "@/eventBus.js";emitter.emit("dataout", "123");')
    webview.start(debug=True)

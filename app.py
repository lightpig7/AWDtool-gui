from flask import Flask, render_template, jsonify, request

app = Flask(__name__, template_folder='static', static_folder='static/assets')  # 创建一个应用

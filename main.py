import webview

from API.Api import Api
from app import app

if __name__ == '__main__':
    window = webview.create_window('AWDtool-gui', app, height=700, width=1000, resizable=False, min_size=(1000, 700),
                                   js_api=Api())
    webview.start(debug=True)

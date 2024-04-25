import webview
from app import  app


class Api():
    def chage_passwd(self, value):
        print(value)



if __name__ == '__main__':
    window = webview.create_window('演示系统', app, height=530, width=800, resizable=False, min_size=(800, 500),
                                   js_api=Api())

    webview.start()

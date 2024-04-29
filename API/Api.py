from API.change_passsword import *


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

    def change_morepasswd(self, host, port, username, password, new_password, thread, mode):
        if mode == '1':
            kill_pool()
            return ''
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
        if thread == '':
            thread = '20'
        s = ssh_changemorepasswd(host, port, username, password, new_password, thread)
        print(s)
        return s


import re
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from socket import socket

import paramiko


def ssh_command(host, port, username, password, command):
    pass


def ssh_changepasswd(host, port, username, password, new_password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # print(host+'-'+str(port)+'-'+ username+'-'+ password+'-'+new_password +'-'+'\n')
    try:
        ssh.connect(hostname=host, port=port, username=username, password=password, timeout=5)

        command = f"echo -e '{password}\n{new_password}\n{new_password}' | passwd {username}"
        stdin, stdout, stderr = ssh.exec_command(command)
        out, err = stdout.read(), stderr.read()

        if 'successfully' in str(err):
            final_string = host + " Password changed successfully!!!\n"
        else:
            final_string = host + " false:\n"
            for line in stdout:
                final_string += line.decode()
            final_string += str(err.decode())
        return final_string
    except paramiko.AuthenticationException:
        return host + " Authentication failed, please check your credentials.\n"
    except paramiko.SSHException as e:
        return host + " SSH connection failed:", str(e) + '\n'
    except Exception as e:
        return host + f" false:{e}\n"
    finally:
        ssh.close()


mode = 0
flag = 1
def ssh_changemorepasswd(host, port, username, password, new_password, thread):
    global mode,flag
    if flag == 0:
        kill_pool()
    else:
        flag = 0

    final_string = ''
    pool = ThreadPoolExecutor(max_workers=int(thread))

    if '/24' in host:
        regex = re.compile(r'\.[0-9]{1,3}/\d{1,2}')
        host_val = regex.sub('', host)
        futures = []
        for i in range(1, 256):

            future = pool.submit(ssh_changepasswd, host_val + '.' + str(i), port, username, password, new_password)
            futures.append(future)

        for future in as_completed(futures):
            if mode == 0:
                try:
                    result = future.result()  # 获取任务结果
                    final_string += result
                    print(result)
                except Exception as e:
                    final_string += f"An error occurred: {e}"
                    print(f"An error occurred: {e}")
            else:
                mode = 0
                flag=1
                final_string+='关闭成功'
                return final_string

    if '/16' in host:
        regex = re.compile(r'\.[0-9]{1,3}\.[0-9]{1,3}/\d{1,2}')
        host_val = regex.sub('', host)
        futures = []
        for i in range(1, 256):
            for j in range(1, 256):
                future = pool.submit(ssh_changepasswd, host_val + '.' + str(i) + '.' + str(j), port, username,
                                     password,
                                     new_password)
                futures.append(future)


        for future in as_completed(futures):
            if mode == 0:
                try:
                    result = future.result()  # 获取任务结果
                    final_string += result
                    print(result)
                except Exception as e:
                    final_string += f"An error occurred: {e}"
                    print(f"An error occurred: {e}")
            else:
                mode = 0
                flag = 1
                final_string += '关闭成功'
                return final_string
    flag=1
    return final_string


def kill_pool():
    global mode
    mode = 1

# ssh_changemorepasswd('192.168.52.0/24', 22, 'ubuntu', 'peiqi7@987', 'peiqi7@987', '10')
# # # pool_array.pop().shutdown(wait=False)
# # print(pool_array)
# kill_pool()
# time.sleep(2)
# kill_pool()
# print(ssh_changepasswd('192.168.52.143',22,'ubuntu','peiqi7@987','peiqi7@987'))

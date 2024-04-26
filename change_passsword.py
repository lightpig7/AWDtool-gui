from socket import socket

import paramiko


def ssh_command(host, port, username, password, command):
    pass

def ssh_changepasswd(host, port, username, password,new_password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    final_string=''
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
            final_string += line
        final_string+=str(err)
        return final_string
    except paramiko.AuthenticationException:
        return "Authentication failed, please check your credentials."
    except paramiko.SSHException as e:
        return "SSH connection failed:", str(e)
    except Exception as e:
        return f"false:{e}"
    finally:
        ssh.close()

# ssh_changemorepasswd('192.168.52',22,'ubuntu','peiqi7@987','peiqi7@987','24',5)
# print(ssh_changepasswd('192.168.52.143',22,'ubuntu','peiqi7@987','peiqi7@987'))
import re
from concurrent.futures import ThreadPoolExecutor, as_completed

import requests

headers = {
    "Accept": "image/gif, image/jpeg, image/pjpeg, application/x-ms-application, application/xaml+xml, application/x-ms-xbap, */*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-Hans-CN,zh-Hans;q=0.8,en-US;q=0.5,en;q=0.3",
    "Host": "httpbin.org",
    "User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; Tablet PC 2.0; wbx 1.0.0; wbxapp 1.0.0; Zoom 3.6.0)",
    "X-Amzn-Trace-Id": "Root=1-628b672d-4d6de7f34d15a77960784504"
}


def check_web_service(url,param,method,header):
    try:
        if method == 'GET':
            if param != '':
                url_val = url + '?' + param
            else:
                url_val = url
            response = requests.get(url_val ,headers=headers)
        elif method == 'POST':
            if '=' in param:
                param_val = {}
                for item in param.split('&'):
                    print(item)
                    param_val[item.split('=')[0]] = item.split('=')[1]
                print(param_val)
                response = requests.post(url,data=param_val,headers=headers)
            else:
                response = requests.post(url, data=param, headers=headers)
        else:
            if param != '':
                url_val = url + '?' + param
            else:
                url_val = url
            response = requests.get(url_val, headers=headers)
        if response.status_code == 200:
            return url+' '+regex_flag(response.text)
        else:
            return f"{url} false: No web service found"
    except requests.RequestException as e:
        return f"{url} false: {str(e)}"

def regex_flag(strr):
    s = ''
    regex = re.compile(r'flag\{.*?\}')
    match = re.findall(regex, strr)  # 使用 re.search 查找整个字符串中的匹配项
    if match:
        for i in match:
            s += i + ';'
        return s.strip(';')
    else:
        print('false')
        return 'no found flag'


def kill_get():
    global mode
    mode = 1


if __name__ == "__main__":
    strr = 'http://127.0.0.1:12345/'
    print(check_web_service(strr,'212312dasdads','POST','1'))

# def check_web_moreservice(host, thread):
#     global mode, flag
#     if flag == 0:
#         kill_get()
#     else:
#         flag = 0
#
#     final_string = ''
#     pool = ThreadPoolExecutor(max_workers=int(thread))
#
#     if '/24' in host:
#         regex = re.compile(r'\.[0-9]{1,3}/\d{1,2}')
#         host_val = regex.sub('', host)
#         futures = []
#         for i in range(1, 256):
#             future = pool.submit(check_web_service, host_val + '.' + str(i))
#             futures.append(future)
#
#         for future in as_completed(futures):
#             if mode == 0:
#                 try:
#                     result = future.result()  # 获取任务结果
#                     final_string += result
#                     print(result)
#                 except Exception as e:
#                     final_string += f"An error occurred: {e}"
#                     print(f"An error occurred: {e}")
#             else:
#                 mode = 0
#                 flag = 1
#                 final_string += '关闭成功'
#                 return final_string
#
#     if '/16' in host:
#         regex = re.compile(r'\.[0-9]{1,3}\.[0-9]{1,3}/\d{1,2}')
#         host_val = regex.sub('', host)
#         futures = []
#         for i in range(1, 256):
#             for j in range(1, 256):
#                 future = pool.submit(check_web_service, host_val + '.' + str(i))
#                 futures.append(future)
#
#         for future in as_completed(futures):
#             if mode == 0:
#                 try:
#                     result = future.result()  # 获取任务结果
#                     final_string += result
#                     print(result)
#                 except Exception as e:
#                     final_string += f"An error occurred: {e}"
#                     print(f"An error occurred: {e}")
#             else:
#                 mode = 0
#                 flag = 1
#                 final_string += '关闭成功'
#                 return final_string
#     flag = 1
#     return final_string

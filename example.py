# coding:utf-8
import requests
import time
import json
import sys

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4495.0 Safari/537.36"
}


def get_proxy():
    p = requests.get("http://127.0.0.1:1117")
    return p.text


def pwn():
    proxy = get_proxy()
    proxy = json.loads(proxy)['proxy']
    print(proxy)
    ip_proxy = {
        'http': 'socks5://' + proxy,
        'https': "socks5://" + proxy
    }
    try:
        r = requests.get(
            url="http://myip.ipip.net/",
            headers=headers,
            proxies=ip_proxy,
            timeout=10,
            verify=False
        )
        print(r.text)
    except:
        pass


if __name__ == '__main__':
    if sys.version_info < (3, 0):
        sys.stdout.write("wrote by Python 3.x\n")
        sys.exit(1)
    requests.packages.urllib3.disable_warnings()
    for i in range(5):
        pwn()
        time.sleep(1)

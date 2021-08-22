#  coding:utf-8
#  使用多线程检测ip的存活，并且将存活ip覆盖原来的ip.txt
#  Author: seventeen
import time
import threading
import queue
import requests
import sys
import getopt


def get_ip():
    with open('ip.txt', 'r', encoding="utf-8") as ips:
        ip_list = ips.readlines()
    init()
    return ip_list


def init():
    # 提取结束清空ip.txt
    with open('ip.txt', 'w') as ip:
        ip.write('')


class test_ip(threading.Thread):
    def __init__(self, data):
        threading.Thread.__init__(self)
        self._data = data

    def run(self):
        global proxies
        global headers
        while not self._data.empty():
            time.sleep(0.8)
            proxy = self._data.get()
            test_url = 'http://myip.ipip.net/'
            print('[*] ' + proxy + ' is testing...')
            ip_proxy = {
                'http': 'socks5://' + proxy,
                'https': "socks5://" + proxy
            }
            try:
                r = requests.get(
                    url=test_url,
                    headers=headers,
                    proxies=ip_proxy,
                    timeout=8,
                    verify=False
                )
                if (r.status_code != 200):
                    print('[-] ' + proxy + ' is died')
                else:
                    time.sleep(0.8)
                    proxies.append(proxy)
                    print('[+] ' + proxy + ' is living')
                    # check_again(proxy)
            except Exception:
                print('[-] ' + proxy + ' is died')
                pass


def check_live():
    ip_list = get_ip()

    data = queue.Queue()
    threads = []
    global threads_count
    threads_count = int(threads_count)

    for ip in ip_list:
        ip = ip.strip('\n')
        data.put(ip)
    for i in range(threads_count):
        threads.append(test_ip(data))

    for i in threads:
        i.start()
    for i in threads:
        i.join()


# 如果使用这个函数再次检测，可能存活的很少
def check_again(proxy):
    test_url_again = 'http://www.baidu.com'
    global headers
    ip_proxy = {
        'http': 'socks5://' + proxy,
        'https': "socks5://" + proxy
    }
    try:
        r = requests.get(
            url=test_url_again,
            headers=headers,
            proxies=ip_proxy,
            timeout=8,
            verify=False
        )
        if (r.status_code != 200):
            print('[-] ' + proxy + ' is died')
        else:
            proxies.append(proxy)
            print('[+] ' + proxy + ' is living')
    except Exception:
        print('[-] ' + proxy + ' is died')
        pass


def save_ip(ip_save):
    print('[*] 检测结束，准备保存结果')
    for ip in ip_save:
        with open('ip.txt', 'a') as goal:
            goal.write(ip + '\n')
    print('[*] 存活数量为: ', len(proxies))
    print(proxies)


def getArg():
    global threads_count
    if len(sys.argv) < 2:
        sys.stdout.write("plz input: -t {threads_count}" + "\n")
        sys.exit(1)
    try:
        opts, args = getopt.getopt(sys.argv[1:], "t:", ["threads_count="])
    except getopt.GetoptError:
        sys.stdout.write("plz input: -t {threads_count}" + "\n")
        sys.exit(1)
    for opt, arg in opts:
        if opt in ("-t", "--threads_count"):
            threads_count = arg
            sys.stdout.write("[*] threads_count: " + threads_count + "\n")
    return [threads_count]


if __name__ == '__main__':
    if sys.version_info < (3, 0):
        sys.stdout.write("wrote by Python 3.x\n")
        sys.exit(1)
    threads_count = ''
    proxies = []
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4495.0 Safari/537.36"
    }
    requests.packages.urllib3.disable_warnings()
    arg_list = []
    arg_list = getArg()
    threads_count = arg_list[0]
    main = check_live()
    save_ip(proxies)

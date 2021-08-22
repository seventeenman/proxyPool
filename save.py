#  coding:utf-8
#  自动化爬虫爬取网站上的代理ip并保存于ip.txt
#  Author: seventeen
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import sys
import getopt


def init():
    # 每次启动清空ip.txt
    with open('ip.txt', 'w') as ip:
        ip.write('')


def openbrower(page):
    ip_url = 'http://free-proxy.cz/zh/proxylist/country/all/socks5/ping/all/' + str(page)
    driver = webdriver.Firefox()
    driver.get(url=ip_url)
    return driver


def web_click(driver):
    driver.set_window_size(809, 692)
    driver.execute_script("window.scrollTo(0,0)")
    driver.find_element(By.ID, "clickexport").click()
    time.sleep(0.8)
    # print(driver.find_element_by_id('zkzk').text)
    ip_list = driver.find_element_by_id('zkzk').text.split('\n')
    driver.quit()
    return ip_list


def save_ip(ip_save, page):
    print("[*] 爬取{0}次结束，准备保存结果".format(str(page)))
    for ip in ip_save:
        with open('ip.txt', 'a') as goal:
            goal.write(ip + '\n')


def controller(page):
    res = web_click(openbrower(page))
    save_ip(res, page)


def getArg():
    global pages_count
    if len(sys.argv) < 2:
        sys.stdout.write("plz input: -p {pages_count}" + "\n")
        sys.exit(1)
    try:
        opts, args = getopt.getopt(sys.argv[1:], "p:", ["pages_count="])
    except getopt.GetoptError:
        sys.stdout.write("plz input: -p {pages_count}" + "\n")
        sys.exit(1)
    for opt, arg in opts:
        if opt in ("-p", "--pages_count"):
            pages_count = arg
            sys.stdout.write("[*] pages_count: " + pages_count + "\n")
    return [pages_count]


if __name__ == '__main__':
    if sys.version_info < (3, 0):
        sys.stdout.write("wrote by Python 3.x\n")
        sys.exit(1)
    init()
    arg_list = []
    arg_list = getArg()
    # 爬取的页数
    pages_count = ''
    pages_count = arg_list[0]
    for page in range(1, int(pages_count) + 1):
        controller(page)

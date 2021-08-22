# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


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


if __name__ == '__main__':
    init()
    # 爬取的页数
    for page in range(1, 3):
        controller(page)

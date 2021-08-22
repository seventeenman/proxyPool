# coding:utf-8
import socket
import random

HOST = "0.0.0.0"
PORT = 1117


def server():
    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listen_socket.bind((HOST, PORT))
    listen_socket.listen(5)
    print('Serving HTTP on port %s ...' % PORT)
    while True:
        client_connection, client_address = listen_socket.accept()
        request = client_connection.recv(1024)
        print(request.decode("utf-8"))
        proxy_ip = get_ip()
        http_response = '''HTTP/1.1 200 OK
Content-Type: application/json
Connection: close
Server: seventeen

{
  "proxy": "%s"
}
'''%(proxy_ip)
        client_connection.sendall(http_response.encode("utf-8"))
        client_connection.close()


def get_ip():
    with open('ip.txt', 'r', encoding="utf-8") as ips:
        ip_list = ips.readlines()
    return ip_list[random.randint(0, len(ip_list)-1)].strip('\n')


if __name__ == '__main__':
    server()

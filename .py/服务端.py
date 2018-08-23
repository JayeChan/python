import socket

phone = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
phone.bind(('127.0.0.1',8000))
phone.listen(5)

conn,addr = phone.accept()
msg = conn.recv(1024)    #收消息
print('客户端发来的消息是：',msg)
conn.send(msg.upper())  #发消息

conn.close()
phone.close()
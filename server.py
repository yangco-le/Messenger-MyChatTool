# -*-coding:utf-8-*-

from socket import *
import threading

address = '127.0.0.1'
port = 15556
buffsize = 1024
s = socket(AF_INET, SOCK_STREAM)
s.bind((address, port))
s.listen(10)  # 最大连接数

client_list = []

user_list = [[518030910001, 1], [518030910002, 2], [518030910003, 3], [518030910004, 4], [518030910005, 5],
             [518030910006, 6]]
user_l = len(user_list)
user_client = []
group_list = [['GROUP_1'], ['GROUP_2'], ['GROUP_3'], ['GROUP_4']]


def login(logindata, clientsock):
    for x in range(0, user_l):
        print("Login request:" + str(logindata[1]))
        if len(user_client) >= 1:
            ul = len(user_client)

            if str(user_list[x][0]) == str(logindata[1]) and str(user_list[x][1]) != str(logindata[2]):
                login_bkinfo = 'false-pw'
                clientsock.send(login_bkinfo.encode())
                break
            elif str(user_list[x][0]) == str(logindata[1]) and str(user_list[x][1]) == str(logindata[2]):
                for user_cl in range(0, ul):
                    if str(user_client[user_cl][0]) == str(logindata[1]):
                        login_bkinfo = 'false-login'
                        clientsock.send(login_bkinfo.encode())
                        break
                    elif user_cl == ul - 1:
                        usercl = []
                        usercl.append(logindata[1])
                        usercl.append(clientsock)
                        login_bkinfo = 'true'
                        user_client.append(usercl)
                        print(user_client)
                        clientsock.send(login_bkinfo.encode())
                break
            elif x == user_l - 1:
                login_bkinfo = 'false-user'
                clientsock.send(login_bkinfo.encode())

        else:

            if str(user_list[x][0]) == str(logindata[1]) and str(user_list[x][1]) != str(logindata[2]):
                login_bkinfo = 'false-pw'
                clientsock.send(login_bkinfo.encode())
                break
            elif str(user_list[x][0]) == str(logindata[1]) and str(user_list[x][1]) == str(logindata[2]):
                usercl = []
                usercl.append(logindata[1])
                usercl.append(clientsock)
                login_bkinfo = 'true'
                user_client.append(usercl)
                print(user_client)
                clientsock.send(login_bkinfo.encode())
                break
            elif x == user_l - 1:
                login_bkinfo = 'false-user'
                clientsock.send(login_bkinfo.encode())


def tcplink(clientsock, clientaddress):
    group_l = len(group_list)
    while True:
        try:
            recvdata = clientsock.recv(buffsize)
            print(recvdata)
            recvdata = recvdata.decode('utf-8')
            logindata = recvdata.split(' ')
            print(logindata)
        except:
            pass

        if str(logindata[0]) == 'login':
            login(logindata, clientsock)

        elif str(logindata[0]) == 'wechat_req':
            for y in range(0, group_l):
                if str(group_list[y][0]) == str(logindata[1]):
                    requser = str(logindata[2]) + ' ' + 'Join'
                    group_list[y].append(clientsock)
                    print(group_list)
                    groupl = len(group_list[y])
                    if groupl > 2:
                        for h in range(1, groupl):
                            group_list[y][h].send(requser.encode())
                    else:
                        clientsock.send(requser.encode())
                    break

        elif str(logindata[0]) == 'wechat':
            for wl in range(0, group_l):
                if str(group_list[wl][0]) == str(logindata[1]):
                    senddata = str(logindata[2]) + ":" + str(logindata[3])
                    l = len(group_list[wl])
                    try:
                        if l >= 2:
                            for x in range(1, l):
                                group_list[wl][x].send(senddata.encode())
                        else:
                            clientsock.send(senddata.encode())
                            break
                        print("Group chat information" +
                              str(senddata) + str(clientaddress))
                    except ValueError:
                        break

        elif str(logindata[0]) == 'personal':
            # print(logindata)
            user_cl = len(user_client)
            # print(user_client)
            send_info = str(logindata[1]) + ":" + str(logindata[3])
            z = 1
            for pl in range(0, user_cl):
                if user_client[pl][0] == logindata[2]:
                    user_client[pl][1].send(send_info.encode())
                    # clientsock.send(send_info.encode())
                    break
                elif z == user_cl:
                    back = str(logindata[2]) + 'is not online'
                    clientsock.send(back.encode())
                z += 1

        elif str(logindata[0]) == 'personal_file':
            # message: 'personal_file', sender, receiver, file_name, length
            # data

            user_cl = len(user_client)
            file_name = logindata[3]
            length = int(logindata[4])
            file_info = ['file', file_name, str(length)]
            print(file_info)

            z = 1
            for pl in range(0, user_cl):
                if user_client[pl][0] == logindata[2]:

                    textsend = ' '.join(file_info)
                    user_client[pl][1].send(textsend.encode())

                    received_size = 0
                    while received_size < length:
                        size = 0
                        if length - received_size > 1024:  # 每次只接收 1024
                            size = 1024
                        else:  # 最后一次接收
                            size = length - received_size

                        data = clientsock.recv(size)
                        user_client[pl][1].sendall(data)
                        data_len = len(data)
                        received_size += data_len

                    break
                elif z == user_cl:
                    back = str(logindata[2]) + 'is not online'
                    clientsock.send(back.encode())
                z += 1

        elif str(logindata[0]) == '':
            print('Unrecognized:')
            print(logindata[0])
            break

    clientsock.close()
    del client_list[-1]


print("The Server is On ..")
while True:
    clientsock, clientaddress = s.accept()
    client_list.append(clientsock)
    print('connect from:', clientaddress)

    t = threading.Thread(target=tcplink, args=(
        clientsock, clientaddress))  # 新创建的线程
    t.start()

import socket
import threading
from saveDataManager import *

clients = []

Accounts = {}

account_counter = 0

def encoding(data):
    encoded_data = b""
    if isinstance(data, str):
        encoded_data = data.encode()
    elif isinstance(data, int):
        encoded_data += (struct.pack("i", data))
    elif isinstance(data, list):
        for item in data:
            if isinstance(item, str):
                encoded_data += (item.encode())
            elif isinstance(item, int):
                encoded_data += struct.pack("i", item)
    return encoded_data

def recive_Data(client):
    data = client[0].recv(1024).decode()
    return data


def send_saves(account_id, client):
    datas = load_data("saves/" + str(account_id) + ".ss")
    client[0].send(encoding(datas))


def connect(server_socket):
    global clients
    while True:
        server_socket.listen(1)
        client_socket, client_address = server_socket.accept()
        client_data = (client_socket, client_address)

        clients.append(client_data)
        print(clients)


def close():
    for client in clients:
        client[0].close()
    server_socket.close()


def main():
    global clients, Accounts
    host = 'localhost'
    port = 1234


    # Socket erstellen
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    server_socket.bind((host, port))

    print(f"Server lauscht auf {host}:{port}")

    connect_thraed = threading.Thread(target=connect, args=[server_socket])
    connect_thraed.start()

    while True:
        for client in clients:
            username = recive_Data(client)
            username = username.lower()

            try:
                account_password = Accounts[username]

            except:
                new_data = {str(username): str(len(Accounts))}
                Accounts.update(new_data)
                account_password = Accounts[username]
                save_data(["new"], "saves/admin.ss")
                print(f"account_password: {account_password}")

            unit = recive_Data(client).lower()
            print(unit)
            if unit == "load_data":
                print(str(client[1]))
                send_saves(username, client)

            elif unit == "save_data":
                print("saving...")
                data = recive_Data(client)
                print(f"Data: {data}")
                save_data(data, "saves/" + str(username) + ".ss")
            clients.remove(client)






if __name__ == "__main__":
    s = main()
    s.connect_thread.join()

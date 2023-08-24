import socket
import threading
from saveDataManager import *

clients = []


Accounts = {}

save_data(Accounts, "saves/accounts.ss")

#Accounts = SaveDataManager.load_data("serrver/saves/accounts.ss")

def recive_Data(client):
    data = client[0].recv(1024).decode()
    return data


def send_saves(client_number, id):
    for client in clients:
        if client == clients[client_number]:
            data = save_manager.load_data("saves/" + str(id) + ".ss")
            client[0].send()


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
    save_manager = SaveDataManager()

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
                account_id = Accounts[username]

            except:
                new_data = {username: len(Accounts)}
                Accounts.update(new_data)
                account_id = Accounts[username]
                save_manager.save_data([], "saves/" + str(account_id) + ".ss")

            unit = recive_Data(client)
            if unit == "load_data":
                send_saves(client[1], account_id)

            elif unit == "save_data":
                print("send...")
                data = recive_Data(client)
                save_manager.save_data(data, "saves/" + str(account_id) + ".ss")
            else:
                print("Error")
                print(unit)



if __name__ == "__main__":
    s = main()
    s.connect_thread.join()

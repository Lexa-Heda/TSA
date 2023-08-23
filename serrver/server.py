import socket
import threading
from saveDataManager import SaveDataManager

clients = []
Accounts = []

def main():
    global clients, Accounts
    host = 'localhost'
    port = 12345
    save_manager = SaveDataManager()

    # Socket erstellen
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    server_socket.bind((host, port))


    server_socket.listen(1)

    print(f"Server lauscht auf {host}:{port}")


    def recive_Data():
        for client in clients:
            data = client[0].recv(1024).decode().upper()

    def send_saves(client_number):
        for client in clients:
            if client == clients[client]:
                data = save_manager.load_data("saves/" + str(client_number) + ".ss")
                client[0].send()

    def create_account():
        pass

    def connect():
        global clients
        client_socket, client_address = server_socket.accept()
        client_data = (client_socket, client_address)

        clients.append(client_data)

    def close():
        for client in clients:
            client[0].close()
        server_socket.close()

if __name__ == "__main__":
    main()

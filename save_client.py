import socket
import struct


def client(iv, data=None):

    host = 'localhost'
    port = 1234

    data_to_save = data

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client_socket.connect((host, port))
    print(f"Verbunden mit {host}:{port}")




    username = input("Username: ")
    send_data(username, client_socket)
    ivint = iv
    send_data(ivint, client_socket)

    if ivint == "save_data":
        for element in data_to_save:
            print("send...")

            send_data(element, client_socket)
    elif ivint == "load_data":
        data = client_socket.recv(1024).decode()
        print(data)
        return data




def send_data(data, client_socket):
    encoded_data = b""
    if isinstance(data, str):
        client_socket.send(data.encode())
    elif isinstance(data, int):
        encoded_data += (struct.pack("i", data))
        client_socket.send(encoded_data)
    elif isinstance(data, list):
        for item in data:
            if isinstance(item, str):
                encoded_data += (item.encode())
            elif isinstance(item, int):
                encoded_data += struct.pack("i", item)
        client_socket.send(encoded_data)


if __name__ == "__main__":
    client(["None"])

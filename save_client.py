import socket
import struct


def main(save_data):

    host = 'localhost'
    port = 1234



    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client_socket.connect((host, port))
    print(f"Verbunden mit {host}:{port}")




    username = input("Username: ")
    ivint = input("string: ")

    send_data(username, client_socket)
    send_data(ivint, client_socket)

    if ivint == "save_data":
        send_data(save_data, client_socket)




def send_data(data, client_socket):
    encoded_data = b""
    if isinstance(data, str):
        client_socket.send(data.encode())
        print(data.encode())
    elif isinstance(data, int):
        encoded_data.join(struct.pack("i", data))
        client_socket.send(encoded_data)
    elif isinstance(data, list):
        for item in data:
            if isinstance(item, str):
                encoded_data += (item.encode())
            else:
                print(encoded_data)
                encoded_data += struct.pack("i", item)
        client_socket.send(encoded_data)


if __name__ == "__main__":
    main([1])

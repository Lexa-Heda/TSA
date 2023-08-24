import socket

def main(save_data):

    host = 'localhost'
    port = 1234


    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client_socket.connect((host, port))
    print(f"Verbunden mit {host}:{port}")

    try:


        username = input("Username: ")
        ivint = input("string: ")

        send_data(username, client_socket)
        send_data(ivint, client_socket)

        if ivint.lower() == "save_data":
            send_data(save_data, client_socket)


    except Exception as e:
        print(f"Fehler aufgetreten: {e}")

def send_data(data, client_socket):
    client_socket.send(data.encode())

if __name__ == "__main__":
    main([])

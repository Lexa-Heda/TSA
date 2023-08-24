import socket

def main():

    host = 'localhost'
    port = 12345


    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:

        client_socket.connect((host, port))
        print(f"Verbunden mit {host}:{port}")

        username = input("Username")

        client_socket.send(username.encode())


        data = client_socket.recv(1024).decode()
        print(f"Antwort vom Server: {data}")

    except Exception as e:
        print(f"Fehler aufgetreten: {e}")

    finally:

        client_socket.close()

if __name__ == "__main__":
    main()

import socket

def main():

    host = '127.0.0.1'
    port = 12345

    # Socket erstellen
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    server_socket.bind((host, port))


    server_socket.listen(1)

    print(f"Server lauscht auf {host}:{port}")


    client_socket, client_address = server_socket.accept()
    print(f"Verbindung hergestellt von {client_address}")

    try:

        data = client_socket.recv(1024).decode().upper()
        print(f"Empfangene Daten: {data}")


        client_socket.send(data.encode())

    except Exception as e:
        print(f"Fehler aufgetreten: {e}")

    finally:
        client_socket.close()
        server_socket.close()

if __name__ == "__main__":
    main()

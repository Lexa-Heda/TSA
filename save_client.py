import socket

def main():

    host = '127.0.0.1'  # IP-Adresse des Servers
    port = 12345        # Port-Nummer des Servers


    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:

        client_socket.connect((host, port))
        print(f"Verbunden mit {host}:{port}")

        message = input("Geben Sie eine Nachricht ein: ")
        client_socket.send(message.encode())


        data = client_socket.recv(1024).decode()
        print(f"Antwort vom Server: {data}")

    except Exception as e:
        print(f"Fehler aufgetreten: {e}")

    finally:

        client_socket.close()

if __name__ == "__main__":
    main()

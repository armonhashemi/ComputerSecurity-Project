def server(shared_key):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)
    client_socket, addr = server_socket.accept()
    print("Connection from:", addr)

    while True:
        data = client_socket.recv(1024)
        if not data: break
        decrypted_message = decrypt_message(data, shared_key)
        print("Received:", decrypted_message)

    client_socket.close()

def client(shared_key):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    while True:
        message = input("Enter message: ")
        encrypted_message = encrypt_message(message, shared_key)
        client_socket.send(encrypted_message)

    client_socket.close()

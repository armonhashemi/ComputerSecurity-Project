import socket
import threading
import time

from encryption import encrypt_message, decrypt_message
from key_exchange import generate_key_pair, derive_shared_key


def server(ip_address, port_num):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((ip_address, port_num))
    server_socket.listen(1)
    client_socket, addr = server_socket.accept()
    print("Connection from:", addr)

    # Key exchange
    server_key_pair = generate_key_pair()
    server_pubkey = server_key_pair.gen_public_key()
    client_socket.send(server_pubkey.to_bytes(4096, 'big'))
    client_pubkey_bytes = client_socket.recv(4096)
    client_pubkey = int.from_bytes(client_pubkey_bytes, 'big')

    shared_key = derive_shared_key(server_key_pair, client_pubkey)

    def receive_messages():
        while True:
            data = client_socket.recv(4096)
            if not data: break
            decrypted_message = decrypt_message(data, shared_key)
            print('\n' + "Received:", decrypted_message)

    def send_messages():
        while True:
            prefix = "Server: Enter message: "
            message = input(prefix)
            encrypted_message = encrypt_message(message, shared_key)
            client_socket.send(encrypted_message)

    receive_thread = threading.Thread(target=receive_messages)
    send_thread = threading.Thread(target=send_messages)

    receive_thread.start()
    send_thread.start()

    # Key update timer
    while True:
        # TODO modify this to be every 10 minutes
        time.sleep(30)  # 10 minutes
        server_key_pair = generate_key_pair()
        server_pubkey = server_key_pair.gen_public_key()
        client_socket.send(server_pubkey.to_bytes(4096, 'big'))
        client_pubkey_bytes = client_socket.recv(4096)
        client_pubkey = int.from_bytes(client_pubkey_bytes, 'big')

        shared_key = derive_shared_key(server_key_pair, client_pubkey)
        print("new shared_key: ", shared_key)

    receive_thread.join()
    send_thread.join()

    client_socket.close()


def client(ip_address, port_num):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((ip_address, port_num))

    # Key exchange
    client_key_pair = generate_key_pair()
    client_pubkey = client_key_pair.gen_public_key()
    server_pubkey_bytes = client_socket.recv(4096)
    server_pubkey = int.from_bytes(server_pubkey_bytes, 'big')
    client_socket.send(client_pubkey.to_bytes(4096, 'big'))

    shared_key = derive_shared_key(client_key_pair, server_pubkey)

    def receive_messages():
        while True:
            data = client_socket.recv(4096)
            if not data: break
            decrypted_message = decrypt_message(data, shared_key)
            print('\n' + "Received:", decrypted_message)

    def send_messages():
        while True:
            prefix = "Client: Enter message: "
            message = input(prefix)
            encrypted_message = encrypt_message(message, shared_key)
            client_socket.send(encrypted_message)

    receive_thread = threading.Thread(target=receive_messages)
    send_thread = threading.Thread(target=send_messages)

    receive_thread.start()
    send_thread.start()

    # Key update timer
    while True:
        # TODO modify this to be every 10 minutes
        time.sleep(30)  # 10 minutes
        client_key_pair = generate_key_pair()
        client_pubkey = client_key_pair.gen_public_key()
        client_socket.send(client_pubkey.to_bytes(4096, 'big'))
        server_pubkey_bytes = client_socket.recv(4096)
        server_pubkey = int.from_bytes(server_pubkey_bytes, 'big')

        shared_key = derive_shared_key(client_key_pair, server_pubkey)
        print("new shared_key: ", shared_key)

    receive_thread.join()
    send_thread.join()

    client_socket.close()

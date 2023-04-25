import socket
import threading
from Crypto.Cipher import Blowfish
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from encryption import encrypt_message, decrypt_message



def server(shared_key):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)
    client_socket, addr = server_socket.accept()
    print("Connection from:", addr)

    def receive_messages():
        while True:
            data = client_socket.recv(1024)
            if not data: break
            decrypted_message = decrypt_message(data, shared_key)
            print("Received:", decrypted_message)

    def send_messages():
        while True:
            message = input("Server: Enter message: ")
            encrypted_message = encrypt_message(message, shared_key)
            client_socket.send(encrypted_message)

    receive_thread = threading.Thread(target=receive_messages)
    send_thread = threading.Thread(target=send_messages)

    receive_thread.start()
    send_thread.start()

    receive_thread.join()
    send_thread.join()

    client_socket.close()

def client(shared_key):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    def receive_messages():
        while True:
            data = client_socket.recv(1024)
            if not data: break
            decrypted_message = decrypt_message(data, shared_key)
            print("Received:", decrypted_message)

    def send_messages():
        while True:
            message = input("Client: Enter message: ")
            encrypted_message = encrypt_message(message, shared_key)
            client_socket.send(encrypted_message)

    receive_thread = threading.Thread(target=receive_messages)
    send_thread = threading.Thread(target=send


from key_exchange import generate_shared_key
from connection import server, client

if __name__ == "__main__":
    shared_key = generate_shared_key()
    print("Shared key:", shared_key)

    choice = input("Choose (s)erver or (c)lient: ")

    if choice.lower() == "s":
        server(shared_key)
    elif choice.lower() == "c":
        client(shared_key)

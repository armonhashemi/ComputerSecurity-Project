from key_exchange import generate_key_pair, derive_shared_key
from connection import server, client

if __name__ == "__main__":
    choice = input("Choose (s)erver or (c)lient: ")

    if choice.lower() == "s":
        server()
    elif choice.lower() == "c":
        client()

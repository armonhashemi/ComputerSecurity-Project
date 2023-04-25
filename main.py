if __name__ == "__main__":
    shared_key = generate_shared_key()
    print("Shared key:", shared_key)

    choice = input("Choose (s)erver or (c)lient: ")

    if choice.lower() == "s":
        server_thread = threading.Thread(target=server, args=(shared_key,))
        server_thread.start()
    elif choice.lower() == "c":
        client_thread = threading.Thread(target=client, args=(shared_key,))
        client_thread.start()

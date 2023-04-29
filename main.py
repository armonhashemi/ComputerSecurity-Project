from connection import server, client

if __name__ == "__main__":
    choice = input("Choose (s)erver or (c)lient: ")

    ip_address = '10.190.240.93'
    port = 12350
    if choice.lower() == "s":
        server(ip_address, port)
    elif choice.lower() == "c":
        client(ip_address, port)

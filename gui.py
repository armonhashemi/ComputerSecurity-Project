from tkinter import *
from threading import Thread
from connection import send_messages, receive_messages

class GUI:
    def __init__(self, name, send_func):
        self.root = Tk()
        self.root.title(name)
        self.send_func = send_func
        
        self.frame = Frame(self.root)
        self.frame.pack()

        self.scrollbar = Scrollbar(self.frame)
        self.scrollbar.pack(side=RIGHT, fill=Y)

        self.text_box = Text(self.frame, wrap=WORD, yscrollcommand=self.scrollbar.set)
        self.text_box.pack(side=LEFT, fill=BOTH)

        self.message_box = Entry(self.root, width=80)
        self.message_box.pack(side=BOTTOM)

        self.send_button = Button(self.root, text="Send", command=self.send_message)
        self.send_button.pack(side=BOTTOM)

    def send_message(self):
        message = self.message_box.get()
        self.send_func(message)
        self.message_box.delete(0, END)

    def start(self):
        receive_thread = Thread(target=receive_messages, args=(self,))
        send_thread = Thread(target=send_messages, args=(self,))
        receive_thread.start()
        send_thread.start()
        self.root.mainloop()

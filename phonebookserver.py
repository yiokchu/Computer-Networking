from phonebook import Phonebook
from socket import *
from phonebookclienthandler import PhonebookClientHandler

HOST = "localhost"
PORT = 5000
ADDRESS = (HOST, PORT)

phonebook = Phonebook()
server = socket(AF_INET, SOCK_STREAM)
server.bind(ADDRESS)
server.listen(5)

# The server now just waits for connections from clients
# and hands sockets off to client handlers
while True:
    print("Waiting for connection . . .")
    client, address = server.accept()
    print("... connected from: ", address)
    # The handlers share the phonebook
    handler = PhonebookClientHandler(client, phonebook)
    handler.start()

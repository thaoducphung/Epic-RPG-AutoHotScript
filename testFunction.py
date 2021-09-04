stringDetect = "<@!405714559857590283>, you are in the **jail**! type `rpg jail`"

# #!/usr/bin/env python3

import socket
import time

# HOST = '127.0.0.1'  # The server's hostname or IP address
HOST = '192.168.0.105'  # The server's hostname or IP address
PORT = 8999        # The port used by the server

# serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# serversocket.bind((host, port))

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.connect((HOST, PORT))
#     time.sleep(2)
#     s.send(b'quit\n')
#     data = s.recv(1024).decode
#     print('Data received from server:',data) # THIS NEVER HAPPENS!

try:
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	    s.connect((HOST, PORT))
	    time.sleep(2)
	    s.send(b'quit\n')
	    data = s.recv(1024).decode
	    print('Data received from server:',data) # THIS NEVER HAPPENS!
except ConnectionRefusedError as err:
	print(err)
	print('Server is not available at the momment!')
except ConnectionResetError as err:
	print(err)
	print('Server is disconnected and close!')



# ### This is SERVER PYTHON alwasy listening to the data from client
# import socket
# serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# serv.bind(('0.0.0.0', 8999))
# serv.listen(5)
# while True:
#     conn, addr = serv.accept()
#     from_client = ''
#     while True:
#         data = conn.recv(4096).decode("utf-8") 
#         if not data: break
#         from_client += data
#         print (from_client)
#         conn.send(b"I am SERVER\n")
#     conn.close()
#     print ('client disconnected')
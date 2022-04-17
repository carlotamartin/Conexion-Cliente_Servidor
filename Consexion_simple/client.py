# echo-client.py

import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # Elpuerto utilizado por elservidor

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))
    message = input(" Escribe la temperatura mínima: ")  # introducir los datos por pantalla
    client_socket.send(message.encode())  # mandar el mensaje
    data_temp_min = client_socket.recv(1024).decode()  # recibidos losdatos

    message = input(" Escribe la temperatura máxima: ")
    client_socket.send(message.encode())
    data_temp_max = client_socket.recv(1024).decode()

    message = input(" Escribe la presión: ")
    client_socket.send(message.encode())
    data_presión = client_socket.recv(1024).decode()

    message = input(" Escribe la pluviometría: ")
    client_socket.send(message.encode())
    data_pluviometría = client_socket.recv(1024).decode()

print('Recibido del servidor:')
print(f"Temperatura mínima: {data_temp_min!r}")
print(f"Temperatura máxima: {data_temp_max!r}")
print(f"Presión: {data_presión!r}")
print(f"Pluviometría: {data_presión!r}")

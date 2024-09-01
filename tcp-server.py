import socket
from faker import Faker

def start_server():
  # Create a TCP/IP socket
  server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  
  # Define the server address and port
  server_address = ('localhost', 12345)

  # Bind the socket to the address
  server_socket.bind(server_address)

  # Start listening for incoming connections
  # Backlog is set to 1
  server_socket.listen(1)
  print(f"Server is listening on {server_address}")

  fake = Faker()

  while True:
    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address} has benn established!")

    # Receive data from the client
    data = client_socket.recv(1024).decode('utf-8')
    print(f"Received from client: {data}")

    # Generate a fake response using faker
    fake_response = fake.sentence()
    print(f"Sending fake response: {fake_response}")

    # Send the fake response back to the client
    client_socket.send(fake_response.encode('utf-8'))
    
    # Clise the client connection
    client_socket.close()


if __name__ == "__main__":
  start_server()
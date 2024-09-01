import socket

def start_client():
  client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server_address = ('localhost', 12345)

  # Connect to the server 
  client_socket.connect(server_address)

  # Get user input
  user_input = input("Enter a message to sent to the server\n")

  # Send the user input to the server
  client_socket.send(user_input.encode('utf-8'))

  # Receive the response from the server
  response = client_socket.recv(1024).decode('utf-8')
  print(f"Response from server: {response}")

  # Close the client connection
  client_socket.close()


if __name__ == "__main__":
  start_client()
from struct import pack, unpack
import socket, threading

def handle_client(conn, addr):
    while True:
        try:
            operation_type = unpack('!B', conn.recv(1))[0]
            num1 = num2 = num3 = num4 = None

            if operation_type == 1:  # Addition
                num1, num2, num3, num4 = unpack('!HHHH', conn.recv(8))
            elif operation_type == 4:  # Multiplication
                num1, num2, num3 = unpack('!HHH', conn.recv(6))
            else:
                num1, num2 = unpack('!HH', conn.recv(4))

            result = 0
            error_message = None
            if operation_type == 1:  # Addition
                result = num1 + num2 + num3 + num4
            elif operation_type == 2:  # Subtraction
                result = num1 - num2
            elif operation_type == 3:  # Division
                if num2 !=0:
                    result = num1 // num2
                else:
                    error_message = 1
            elif operation_type == 4:  # Multiplication
                result = num1 * num2 * num3
            elif operation_type == 5:  # Modulo
                if num2 !=0:
                    result = num1 % num2
                else:
                    error_message = 2

            if error_message != None:
                response = pack('!B', error_message)  
            else:
                fmt = None
                if operation_type == 1:  # Addition
                    fmt = 'I'
                elif operation_type == 2:  # Subtraction
                    fmt = 'h'
                elif operation_type == 3:  # Division
                    fmt = 'd'
                elif operation_type == 4:  # Multiplication
                    fmt = 'Q'
                else:                      # Modulo
                    fmt = 'H'
                response = pack('!B' + fmt, 0, result)
            break
        except Exception as e:
            print(e)
            response = pack('!B', 3)
            break

    conn.sendall(bytes(response))
    conn.close()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serverSocket:
    serverSocket.bind(('localhost', 12345))
    serverSocket.listen()
    while True:
        conn, addr = serverSocket.accept()
        threading.Thread(target=handle_client, args=(conn, addr)).start()
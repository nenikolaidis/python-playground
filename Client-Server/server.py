from struct import pack, unpack
import socket, threading

from protocol import (HOST, PORT, OPERATIONS, SUCCESS, UNKNOWN_ERROR,
                      calculate, recv_exact, operand_size)


def handle_client(conn, addr):
    try:
        operation_type = unpack('!B', recv_exact(conn, 1))[0]
        if operation_type not in OPERATIONS:
            response = pack('!B', UNKNOWN_ERROR)
        else:
            operand_fmt, result_fmt = OPERATIONS[operation_type][1:3]
            numbers = unpack('!' + operand_fmt, recv_exact(conn, operand_size(operation_type)))
            status, result = calculate(operation_type, numbers)
            if status == SUCCESS:
                response = pack('!B' + result_fmt, SUCCESS, result)
            else:
                response = pack('!B', status)
    except Exception as e:
        print(e)
        response = pack('!B', UNKNOWN_ERROR)

    conn.sendall(response)
    conn.close()


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        while True:
            conn, addr = server_socket.accept()
            threading.Thread(target=handle_client, args=(conn, addr)).start()


if __name__ == "__main__":
    main()

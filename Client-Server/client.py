from struct import pack, unpack
import socket

from protocol import (HOST, PORT, OPERATIONS, ERRORS, SUCCESS, UNKNOWN_ERROR,
                      recv_exact, result_size)


def send_request(operation_type, numbers):
    operand_fmt, result_fmt = OPERATIONS[operation_type][1:3]

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))
        client_socket.sendall(pack('!B' + operand_fmt, operation_type, *numbers))

        status = unpack('!B', recv_exact(client_socket, 1))[0]
        if status != SUCCESS:
            return status, None
        result = unpack('!' + result_fmt, recv_exact(client_socket, result_size(operation_type)))[0]
        return status, result


def ask_operation():
    menu = ", ".join(f"{code}: {name}" for code, (name, *_) in OPERATIONS.items())
    while True:
        try:
            operation = int(input(f"Select an operation ({menu}): "))
            if operation in OPERATIONS:
                return operation
        except ValueError:
            pass
        print("Invalid operation. Please try again.")


def ask_numbers(operation_type):
    _, operand_fmt, _, max_value = OPERATIONS[operation_type]
    ordinals = ("first", "second", "third", "fourth")
    while True:
        try:
            numbers = [int(input(f"Enter the {ordinals[i]} number: ")) for i in range(len(operand_fmt))]
        except ValueError:
            print("Please enter whole numbers.")
            continue
        if all(0 <= n <= max_value for n in numbers):
            return numbers
        print(f"Numbers must be between 0 and {max_value}. Please try again.")


def main():
    operation = ask_operation()
    numbers = ask_numbers(operation)
    status, result = send_request(operation, numbers)
    if status == SUCCESS:
        print("Result:", result)
    else:
        print(ERRORS.get(status, ERRORS[UNKNOWN_ERROR]))


if __name__ == "__main__":
    main()

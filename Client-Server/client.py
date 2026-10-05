from socket import *
from struct import pack, unpack

errors = (
    "Division by 0 error",
    "Modulo by 0 error",
    "Unknown error"
)

def send_request(operation_type, num1, num2, num3, num4):
    global errors

    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect(('localhost', 12345))

    if operation_type == 1:  # Addition
        request = pack('!BHHHH', operation_type, num1, num2, num3, num4)
    elif operation_type == 4:  # Multiplication
        request = pack('!BHHH', operation_type, num1, num2, num3)
    else:
        request = pack('!BHH', operation_type, num1, num2)

    clientSocket.sendall(bytes(request))

    success = unpack('!B', clientSocket.recv(1))[0]

    if success == 0:
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
        result = unpack('!'+fmt, clientSocket.recv(8))[0]
        print("Result:", result)
    else:
        print(errors[success - 1])

    clientSocket.close()

while True:
    try:
        operation = int(input("Select an operation (1: Addition, 2: Subtraction, 3: Division, 4: Multiplication, 5: Modulo): "))
        if 1 <= operation <= 5:
            break
        else:
            print("Invalid operation. Please try again.")
    except ValueError:
        print("Invalid operation. Please try again.")

if operation == 1:  # Addition
    while True: 
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        num3 = int(input("Enter the third number: "))
        num4 = int(input("Enter the fourth number: "))
        if 0 <= num1 <= 60000 and 0 <= num2 <= 60000 and 0 <= num3 <= 60000 and 0 <= num4 <= 60000:
            send_request(operation, num1, num2, num3, num4)
            break
elif operation == 4:  # Multiplication
    while True:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        num3 = int(input("Enter the third number: "))
        if 0 <= num1 <= 60000 and 0 <= num2 <= 60000 and 0 <= num3 <= 60000:
            send_request(operation, num1, num2, num3, None)
            break
else:
    while True:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        if operation != 2:
            if 0 <= num1 <= 60000 and 0 <= num2 <= 60000:
                send_request(operation, num1, num2, None, None)
                break
        else:
            if 0 <= num1 <= 30000 and 0 <= num2 <= 30000:
                send_request(operation, num1, num2, None, None)
                break
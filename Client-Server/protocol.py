from struct import calcsize

HOST = 'localhost'
PORT = 12345

# code: (name, numbers format, result format, max number)
OPERATIONS = {
    1: ("Addition",       'HHHH', 'I', 60000),
    2: ("Subtraction",    'HH',   'h', 30000),
    3: ("Division",       'HH',   'd', 60000),
    4: ("Multiplication", 'HHH',  'Q', 60000),
    5: ("Modulo",         'HH',   'H', 60000),
}

SUCCESS = 0
DIVISION_BY_ZERO = 1
MODULO_BY_ZERO = 2
UNKNOWN_ERROR = 3

ERRORS = {
    DIVISION_BY_ZERO: "Division by 0 error",
    MODULO_BY_ZERO: "Modulo by 0 error",
    UNKNOWN_ERROR: "Unknown error",
}


def calculate(operation_type, numbers):
    if operation_type == 1:    # Addition
        return SUCCESS, sum(numbers)
    elif operation_type == 2:  # Subtraction
        return SUCCESS, numbers[0] - numbers[1]
    elif operation_type == 3:  # Division
        if numbers[1] == 0:
            return DIVISION_BY_ZERO, None
        return SUCCESS, numbers[0] // numbers[1]
    elif operation_type == 4:  # Multiplication
        return SUCCESS, numbers[0] * numbers[1] * numbers[2]
    elif operation_type == 5:  # Modulo
        if numbers[1] == 0:
            return MODULO_BY_ZERO, None
        return SUCCESS, numbers[0] % numbers[1]
    return UNKNOWN_ERROR, None


#Reading until we get all the bytes
def recv_exact(sock, size):
    data = b''
    while len(data) < size:
        chunk = sock.recv(size - len(data))
        if not chunk:
            raise ConnectionError("connection closed before all data arrived")
        data += chunk
    return data


def operand_size(operation_type):
    return calcsize('!' + OPERATIONS[operation_type][1])


def result_size(operation_type):
    return calcsize('!' + OPERATIONS[operation_type][2])

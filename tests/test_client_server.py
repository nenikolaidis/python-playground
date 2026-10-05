import socket
import threading
from struct import pack, unpack

import pytest

import client
import protocol
from protocol import SUCCESS, DIVISION_BY_ZERO, MODULO_BY_ZERO, UNKNOWN_ERROR, calculate
from server import handle_client


@pytest.mark.parametrize("operation, numbers, expected", [
    (1, (1, 2, 3, 4), 10),
    (2, (3, 10), -7),
    (3, (7, 2), 3),
    (4, (2, 3, 4), 24),
    (5, (7, 3), 1),
])
def test_calculate(operation, numbers, expected):
    assert calculate(operation, numbers) == (SUCCESS, expected)


def test_calculate_errors():
    assert calculate(3, (5, 0)) == (DIVISION_BY_ZERO, None)
    assert calculate(5, (5, 0)) == (MODULO_BY_ZERO, None)
    assert calculate(9, (1, 2)) == (UNKNOWN_ERROR, None)


def test_largest_results_fit_their_formats():
    for code, (_, operand_fmt, result_fmt, max_value) in protocol.OPERATIONS.items():
        numbers = [max_value] * len(operand_fmt)
        if code == 2:
            numbers = [0, max_value]
        _, result = calculate(code, numbers)
        pack('!' + result_fmt, result)


def ask_server(request):
    server_side, client_side = socket.socketpair()
    thread = threading.Thread(target=handle_client, args=(server_side, None))
    thread.start()
    client_side.sendall(request)
    response = b''
    while chunk := client_side.recv(64):
        response += chunk
    thread.join()
    client_side.close()
    return response


def test_server_returns_result():
    assert unpack('!BQ', ask_server(pack('!BHHH', 4, 10, 20, 30))) == (SUCCESS, 6000)


def test_server_returns_error_on_division_by_zero():
    assert ask_server(pack('!BHH', 3, 5, 0)) == pack('!B', DIVISION_BY_ZERO)


def test_server_rejects_unknown_operation():
    assert ask_server(pack('!B', 42)) == pack('!B', UNKNOWN_ERROR)


def test_client_and_server_end_to_end(monkeypatch):
    listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listener.bind(('localhost', 0))
    listener.listen()
    monkeypatch.setattr(client, "PORT", listener.getsockname()[1])

    def serve_once():
        conn, addr = listener.accept()
        handle_client(conn, addr)

    thread = threading.Thread(target=serve_once)
    thread.start()
    assert client.send_request(1, [1, 2, 3, 4]) == (SUCCESS, 10)
    thread.join()
    listener.close()

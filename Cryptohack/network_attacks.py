#!/usr/bin/env python3

from pwn import remote  # pip install pwntools
import json

HOST = "socket.cryptohack.org"
PORT = 11112


def json_recv(r):
    line = r.readline()
    return json.loads(line.decode())


def json_send(r, hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)


def main():
    r = remote(HOST, PORT)

    for _ in range(4):
        print(r.readline())

    json_send(r, {"buy": "clothes"})
    print(json_recv(r))


if __name__ == "__main__":
    main()

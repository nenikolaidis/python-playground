# python-playground

Small Python programs I wrote while learning: networking, cryptography challenges, competitive programming and algorithm exercises.

## Setup

Requires Python 3.10+.

```bash
python3 -m venv .venv
source .venv/bin/activate        # Windows: .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt  # only needed for the Cryptohack scripts
```

## Contents

### `Client-Server/` — binary-protocol calculator over TCP

| File | What it does |
| --- | --- |
| `server.py` | Multi-threaded TCP server on `localhost:12345`. Receives an operation and its numbers packed with `struct`, returns the result or an error code. |
| `client.py` | Interactive client: pick an operation (addition, subtraction, division, multiplication, modulo), enter the numbers, get the result. |

```bash
cd Client-Server
python3 server.py     # terminal 1
python3 client.py     # terminal 2
```

### `Cryptohack/` — [CryptoHack](https://cryptohack.org) introductory challenges

| File | Challenge |
| --- | --- |
| `XOR_starter.py` | XOR every character of a string with 13 |
| `favourite_byte.py` | Brute-force a single-byte XOR key |
| `XOR_properties.py` | Recover a flag using XOR's associative/self-inverse properties |
| `bytes_and_big_integers.py` | Convert a big integer back to bytes |
| `network_attacks.py` | Talk to a CryptoHack server with JSON over a socket |

```bash
cd Cryptohack
python3 favourite_byte.py
```

### `IEEExtreme/` — [IEEEXtreme](https://ieeextreme.org) competition problems

Both solutions read from standard input and print to standard output.

| File | Problem |
| --- | --- |
| `war_games.py` | Simulate the card game War for each test case; print the winner or `draw` if the game loops. |
| `restaurant_cipher.py` | For each message, print (in uppercase) the most frequent letter among `a`–`g`. |

```bash
cd IEEExtreme
printf '1\n2 3 A\nK 4 5\n' | python3 war_games.py
```

### `Exercises/` — algorithm practice

| File | What it does |
| --- | --- |
| `ex1_sudoku.py` | Backtracking sudoku solver that picks the cell with the fewest options first; prints the solved board and the number of backtracking steps. |
| `ex2_stockstrategy.py` | Simulates a random stock market over several days and tests a simple buy/sell strategy. |

```bash
cd Exercises
python3 ex1_sudoku.py
```

## License

[MIT](LICENSE.md)

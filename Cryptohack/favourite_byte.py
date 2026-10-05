from pwn import xor

flag_bytes = bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")

for key in range(256):
    flag = xor(flag_bytes, key).decode("utf-8", errors="ignore")
    if "crypto" in flag:
        print(flag)
        break

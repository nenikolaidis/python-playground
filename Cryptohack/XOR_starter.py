def xor(input_string):
    result = ""
    for char in input_string:
        result += chr(ord(char) ^ 13)
    return result


if __name__ == "__main__":
    flag = "crypto{" + xor("label") + "}"
    print(flag)

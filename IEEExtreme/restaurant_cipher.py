def most_frequent_lowercase_to_uppercase(text):
    lowercase = 'abcdefg'
    uppercase = 'ABCDEFG'
    f = {}

    for c in text:
        if c in lowercase:
            if c in f:
                f[c] += 1
            else:
                f[c] = 1

    if not f:  # No letters a-g found
        return None

    most_frequent_lower = max(f, key=f.get)
    most_frequent_upper = uppercase[lowercase.index(most_frequent_lower)]

    return most_frequent_upper


def main():
    n = int(input())
    for _ in range(n):
        print(most_frequent_lowercase_to_uppercase(input()))


if __name__ == "__main__":
    main()

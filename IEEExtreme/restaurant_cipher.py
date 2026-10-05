n = int(input())
messages = [input() for _ in range(n)]


def most_frequent_lowercase_to_uppercase(text):
    lowercase = 'abcdefg'
    uppercase = 'ABCDEFG'
    f = {}

    for c in text:
        if c.islower() and c in lowercase:
            if c in f:
                f[c] += 1
            else:
                f[c] = 1

    if not f:  # No lowercase letters found
        return None

    most_frequent_lower = max(f, key=f.get)
    most_frequent_upper = uppercase[lowercase.index(most_frequent_lower)]

    return most_frequent_upper


for i in range(n):
    result = most_frequent_lowercase_to_uppercase(messages[i])
    print(result)
user_input = list(input("Enter a list of numbers separated by spaces: ").split(" "))


def classify_numbers(lst: list):
    even = []
    odd = []
    for i in lst:
        if int(i) % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return even, odd


if __name__ == 'main':
    enums, onums = classify_numbers(user_input)
    print(enums, onums)
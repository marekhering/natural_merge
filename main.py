import random


def clear_file(filename):
    with open(filename, 'w') as _:
        pass


def save_to_file(filename, data):
    with open(filename, 'a') as file:
        file.write(str(data) + '\n')


def load_from_file(left_bounds, right_bounds):
    with open(filename, 'r') as file:
        result = []
        for index, line in enumerate(file.readlines()):
            if left_bounds <= index <= right_bounds:
                result.append(int(line))
    return result


if __name__ == '__main__':
    filename = "temp.txt"

    clear_file(filename)

    random_number = random.randint(0, 10 ** 20)
    print(random_number)
    save_to_file(filename, random_number)

    random_number = random.randint(0, 10 ** 20)
    print(random_number)
    save_to_file(filename, random_number)

    print(load_from_file(0, 1))

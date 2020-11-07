

def clear_file(file_dir):
    with open(file_dir, 'w') as _:
        pass


def save_to_file(file_dir, data):
    with open(file_dir, 'a') as file:
        file.write(str(data) + '\n')


def load_from_file(file_dir, left_bounds, right_bounds):
    with open(file_dir, 'r') as file:
        result = []
        for index, line in enumerate(file.readlines()):
            if left_bounds <= index <= right_bounds:
                result.append(line)
    return result


def print_file(file_dir):
    with open(file_dir, 'r') as file:
        for line in file.readlines():
            print(line, end='')

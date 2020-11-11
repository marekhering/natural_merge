

def clear_file(file_dir):
    with open(file_dir, 'w') as _:
        pass


def save_to_file(file_dir, data):
    with open(file_dir, 'a') as file:
        file.write(str(data) + '\n')


def print_file(file_dir):
    with open(file_dir, 'r') as file:
        print('[', end='')
        for line in file.readlines():
            print(line[:2], end=' ')
        print(']')

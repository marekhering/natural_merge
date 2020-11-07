from natural_merge.generator import generate_data
from natural_merge.file_operations import print_file

if __name__ == '__main__':

    file_dir = "data/numbers.txt"
    numbers_amount = 20
    random_number = random.randint(0, 10 ** 20)
    print_file(file_dir)


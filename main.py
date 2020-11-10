from natural_merge.generator import generate_data
from natural_merge.sorting import sort_file

if __name__ == '__main__':

    file_dir = "data/numbers.txt"
    numbers_amount = 20
    # generate_data(file_dir, numbers_amount)
    # print_file(file_dir)

    sort_file(file_dir)


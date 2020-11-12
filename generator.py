from natural_merge.file_operations.file_operations import *
from natural_merge.setup import *
import random


def generate_data(file_dir, numbers_amount):

    for _ in range(numbers_amount):
        number_type = random.randint(0, 1)
        if number_type == 0:
            random_number = random.randint(0, NUMBER_LIMIT)
        else:
            random_number = random.random() * NUMBER_LIMIT
            random_number = round(random_number, DECIMAL_PLACES)

        save_to_file(file_dir, random_number)

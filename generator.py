from natural_merge.file_operations.file_operations import *
from natural_merge.setup import *
import random


def generate_data(file_dir, numbers_amount):

    for _ in range(numbers_amount):
        random_number = random.randint(0, NUMBER_LIMIT)
        save_to_file(file_dir, random_number)

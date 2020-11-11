from pathlib import Path
import time

from natural_merge.file_operations.file_operations import print_file, save_to_file, clear_file
from natural_merge.setup import *
from natural_merge.sorting import sort_file
from natural_merge.generator import generate_data


class Interface:
    def __init__(self):
        self.input_directory = DEFAULT_INPUT_DIR
        self.config = {
            'print_after_phases': True,
            'print_file_before_sorting': True,
            'print_file_after_sorting': True
        }

    def run_menu(self):

        while True:

            print("Natural merge")
            print("Options:")
            print("1. Generate numbers")
            print("2. Sort file")
            print("3. Add records from keyboard")
            print("4. Print input file")
            print("5. Clear input file")
            print("6. Set new input file (" + self.input_directory + ")")
            print("7. Change the parameters")
            print("0. Exit")
            print("Select an option number: ", end='')

            choice = input()

            print()

            if choice == '1':
                self.generate()
            elif choice == '2':
                self.sort()
            elif choice == '3':
                self.add_records()
            elif choice == '4':
                print("Input: ", end='')
                print_file(self.input_directory)
                print()
            elif choice == '5':
                clear_file(self.input_directory)
                print("Input file cleared")
            elif choice == '6':
                self.set_new_directory()
            elif choice == '0':
                break
            else:
                print("Wrong option")

    def sort(self):
        sort_file(self.input_directory)

    def generate(self):
        print("Enter numbers of records: ", end='')
        numbers_of_records = input()
        try:
            numbers_of_records = int(numbers_of_records)
        except(ValueError, TypeError):
            print("Wrong input")
            print()
            return

        generate_data(self.input_directory, numbers_of_records)
        print("Data generated")
        print()

    def set_new_directory(self):
        print("Enter new directory: ", end='')
        directory = input()

        new_file = Path(directory)
        if new_file.exists():
            self.input_directory = directory
            print("Directory set")
        else:
            print("Wrong directory")

        time.sleep(0.4)
        print()

    def add_records(self):
        print("Enter new records")
        print("After every record press 'Enter'")
        print("Press 'q' and 'Enter' to quit")

        counter = 0
        while True:
            print(str(counter) + ". Record: ", end='')
            record = input()

            if record == 'q':
                print()
                return

            try:
                record = int(record)
            except(ValueError, TypeError):
                print("Wrong record (must be integer or float)")
                continue
            counter += 1
            save_to_file(self.input_directory, record)


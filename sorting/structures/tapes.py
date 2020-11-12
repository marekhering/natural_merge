from natural_merge.file_operations.file_operations import print_file, clear_file
from natural_merge.file_operations import Buffer
from natural_merge.setup import BUFFER_SIZE
from natural_merge.sorting.structures import Record

TAPES_NUMBER = 4


class Tape:
    def __init__(self, name, directory):
        self.name = name
        self.directory = directory
        self.buffer = Buffer(directory, BUFFER_SIZE)
        self.run_counter = 0

    def write_run(self, run):
        self.run_counter += 1
        for record in run:
            self.buffer.write_record(record.value)

    def read_record(self):
        number = self.buffer.read_number()
        if number is None:
            return None
        else:
            return Record(number)

    def get_number_of_runs(self):
        return self.run_counter

    def finish_read(self):
        self.buffer.read_offset = 0

    def finish_write(self):
        self.buffer.save_to_file()


    def print(self):
        print(self.name, end=' ')
        print_file(self.directory)

    def clear(self):
        self.run_counter = 0

        clear_file(self.directory)

    @staticmethod
    def create_tapes():
        tapes = list()
        tapes_directory = "data/tapes"
        for type_number in range(TAPES_NUMBER):
            tape_name = "tape" + str(type_number)
            tape_directory = tapes_directory + "/" + tape_name + ".txt"
            new_tape = Tape(tape_name, tape_directory)
            new_tape.clear()
            tapes.append(new_tape)
        return tapes

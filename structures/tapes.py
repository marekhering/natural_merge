from natural_merge.file_operations.file_operations import print_file, clear_file
from natural_merge.file_operations import Buffer
from natural_merge.setup import BUFFER_SIZE

TAPES_NUMBER = 4


class Tape:
    def __init__(self, name, directory):
        self.name = name
        self.directory = directory
        self.buffer = Buffer(directory, BUFFER_SIZE)

    def write_run(self, run):
        for record in run:
            self.buffer.write_record(record)

    def read_record(self):
        return self.buffer.read_record()

    def print(self):
        print(self.name)
        print_file(self.directory)

    def clear(self):
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

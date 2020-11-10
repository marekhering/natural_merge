from natural_merge.file_operations.file_operations import clear_file, save_to_file

TAPES_NUMBER = 4


class Tape:
    def __init__(self, directory):
        clear_file(directory)
        self.directory = directory

    def write_run(self, run):
        for record in run:
            save_to_file(self.directory, record.value)

    @staticmethod
    def create_tapes():
        tapes = list()
        tapes_directory = "data/tapes"
        for type_number in range(TAPES_NUMBER):
            tape_directory = tapes_directory + "/tape" + str(type_number) + ".txt"
            new_tape = Tape(tape_directory)
            tapes.append(new_tape)
        return tapes
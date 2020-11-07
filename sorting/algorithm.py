from natural_merge.file_operations import read_from_file
from natural_merge.structures import Record


def sort_file(file_dir):

    stop_clause = False
    record_index = 0

    create_tapes()

    while stop_clause is False:

        record = read_record(file_dir, record_index)


def read_record(file_dir, index):
    # Temporary function
    # TODO Block read
    value = read_from_file(file_dir, index, index)
    value = int(value[0])
    return Record(value)


def create_tapes():
    pass

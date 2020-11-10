from natural_merge.file_operations.file_operations import print_file
from natural_merge.structures import Record, Tape


def sort_file(file_dir):

    input_dir = file_dir
    tapes = Tape.create_tapes()

    print("Numbers")
    print_file(input_dir)

    distribution([input_dir], [tapes[0], tapes[1]])
    print("TAPE 0")
    print_file(tapes[0].directory)
    print("TAPE 1")
    print_file(tapes[1].directory)
    merge([tapes[0], tapes[1]], tapes[2])


def distribution(inputs, outputs):
    prev_record = None

    in_index = 0
    out_index = 0
    run = list()

    in_len = len(inputs)
    out_len = len(outputs)

    record_indexes = [0] * in_len

    while True:

        record = read_record(inputs[in_index], record_indexes[in_index])
        record_indexes[in_index] += 1
        in_index = (in_index + 1) % in_len

        if record is None:
            outputs[out_index].write_run(run)
            break

        if prev_record is None:
            prev_record = record
            run.append(record)
            continue

        if record < prev_record:
            outputs[out_index].write_run(run)
            out_index = (out_index + 1) % out_len
            run = [record]
        else:
            run.append(record)

        prev_record = record

def merge(inputs, outputs):
    pass


def read_record(file_dir, index):
    # Temporary function
    # TODO Block read
    value = read_from_file(file_dir, index, index)
    if value:
        value = int(value[0])
        return Record(value)
    else:
        return None


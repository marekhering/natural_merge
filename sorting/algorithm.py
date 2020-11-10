from natural_merge.file_operations.file_operations import print_file
from natural_merge.structures import Record, Tape


def sort_file(file_dir):

    input_tape = Tape("Input", file_dir)
    distribution_tapes = Tape.create_tapes()

    input_tape.print()

    first_distribution(input_tape, [distribution_tapes[0], distribution_tapes[1]])

    distribution_tapes[0].print()
    distribution_tapes[1].print()


def first_distribution(input_tape, outputs_tapes):
    prev_record = None

    run = list()
    out_index = 0
    out_len = len(outputs_tapes)

    while True:

        record = input_tape.read_record()

        if record is None:
            outputs_tapes[out_index].write_run(run)
            for tape in outputs_tapes:
                tape.buffer.save_to_file()
            break

        if prev_record is None:
            prev_record = record
            run.append(record)
            continue

        if record < prev_record:
            outputs_tapes[out_index].write_run(run)
            out_index = (out_index + 1) % out_len
            run = [record]
        else:
            run.append(record)

        prev_record = record

from natural_merge.sorting.structures import Tape, RecordList


def sort_file(file_dir):
    phase_counter = 0

    input_tape = Tape("Input", file_dir)
    distribution_tapes = Tape.create_tapes()

    print("Phase:", phase_counter)
    input_tape.print()
    distribution([input_tape], [distribution_tapes[0], distribution_tapes[1]])

    input_tapes = [distribution_tapes[0], distribution_tapes[1]]
    output_tapes = [distribution_tapes[2], distribution_tapes[3]]

    for tape in input_tapes:
        tape.print()


    while True:
        phase_counter += 1
        print("Phase:", phase_counter)

        distribution(input_tapes, output_tapes)

        for tape in output_tapes:
            tape.print()

        number_of_runs = [tape.get_number_of_runs() for tape in output_tapes]
        if sum(number_of_runs) == 1:
            break

        input_tapes, output_tapes = swap(input_tapes, output_tapes)


def distribution(input_tapes, output_tapes):
    record_list = RecordList(len(input_tapes))
    prev_record = None

    run = list()
    out_index = 0
    out_len = len(output_tapes)

    for tape in output_tapes:
        tape.clear()

    while True:

        for index, tape in enumerate(input_tapes):
            if record_list[index] is None:
                record_list[index] = tape.read_record()

        if record_list.none_full():
            output_tapes[out_index].write_run(run)
            break

        record = record_list.get_next_record(prev_record)

        if prev_record is not None and record < prev_record:
            output_tapes[out_index].write_run(run)
            out_index = (out_index + 1) % out_len
            run = [record]
        else:
            run.append(record)

        prev_record = record

    for tape in input_tapes:
        tape.finish_read()

    for tape in output_tapes:
        tape.finish_write()


def swap(a, b):
    return b, a

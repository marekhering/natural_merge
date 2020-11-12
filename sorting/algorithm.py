from natural_merge.sorting.structures import Tape, RecordList


def sort_file(file_dir):
    phase_counter = 1
    result_tape = None

    input_tape = Tape("Input", file_dir)
    distribution_tapes = Tape.create_tapes()

    input_tape.print()
    number_of_readings, number_of_writings = distribution([input_tape], [distribution_tapes[0], distribution_tapes[1]])

    input_tapes = [distribution_tapes[0], distribution_tapes[1]]
    output_tapes = [distribution_tapes[2], distribution_tapes[3]]

    print("Phase:", phase_counter)
    for tape in input_tapes:
        tape.print()

    while True:
        number_of_runs = [tape.get_number_of_runs() for tape in input_tapes]
        if sum(number_of_runs) == 1:
            result_tape = input_tapes[0]
            break

        if output_tapes[0] == distribution_tapes[0]:
            phase_counter += 1
            print("Phase:", phase_counter)

        n_read, n_write = distribution(input_tapes, output_tapes)
        number_of_readings += n_read
        number_of_writings += n_write

        for tape in output_tapes:
            tape.print()

        input_tapes, output_tapes = swap(input_tapes, output_tapes)

    copy_content(result_tape, input_tape)

    print()
    print("Sorting finished")
    print("Copy content of tape to input file")
    print("Sorted file: ", end='')
    input_tape.print()
    print()
    print("Stats:")
    print("Number of phases: ", phase_counter)
    print("Number of readings: ", number_of_readings)
    print("Number of writings: ", number_of_writings)
    print()



def distribution(input_tapes, output_tapes):
    number_of_readings = 0
    number_of_writings = 0
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
        number_of_readings += tape.finish_read()

    for tape in output_tapes:
        number_of_writings += tape.finish_write()

    return number_of_readings, number_of_writings


def copy_content(input_tape, output_tape):
    output_tape.clear()
    result_run = []

    while True:

        record = input_tape.read_record()
        if record is None:
            break

        result_run.append(record)

    output_tape.write_run(result_run)
    output_tape.finish_write()


def swap(a, b):
    return b, a

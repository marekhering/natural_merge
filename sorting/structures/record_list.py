

class RecordList(list):
    def __init__(self, size):
        super(RecordList).__init__()
        self.extend([None] * size)

    def get_next_record(self, prev_record):
        if prev_record is None:
            next_record, next_record_index = self.minimum_value_and_index()
            if next_record_index is not None:
                self[next_record_index] = None
            return next_record

        next_record, next_record_index = self.minimum_value_and_index(higher_than=prev_record)

        if next_record is None:
            next_record, next_record_index = self.minimum_value_and_index()

        if next_record_index is not None:
            self[next_record_index] = None

        return next_record

    def none_full(self):
        for record in self:
            if record is not None:
                return False
        return True

    def minimum_value_and_index(self, higher_than=None):
        min_val = None
        min_ind = None

        for index, record in enumerate(self):
            if record is not None and (min_val is None or record < min_val):
                if higher_than is None or record >= higher_than:
                    min_val = record
                    min_ind = index

        return min_val, min_ind

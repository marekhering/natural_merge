class Buffer(list):
    def __init__(self, directory, size):
        super(Buffer).__init__()

        self.size = size
        self.directory = directory
        self.read_offset = 0
        self.string_cast = ""
        self.readings = 0
        self.writings = 0

        self.empty_file = False

    def read_number(self):
        if self.empty() and not self.empty_file:
            self.load_from_file()
        number = self.pop(0) if not self.empty() else None
        self.string_cast = self.string_cast[(len(str(number)) + 1):]
        return number

    def write_record(self, record):
        if len(self.to_string(additional_records=[record])) > self.size:
            self.save_to_file()
        self.append(record)
        self.string_cast += str(record) + '\n'

    def load_from_file(self):
        with open(self.directory, 'r') as file:
            file.seek(self.read_offset, 0)
            page = file.read(self.size)
            self.readings += 1
            file.close()

        if not page:
            self.empty_file = True
            return

        number_constructor = ""
        temp_offset = self.read_offset
        for char in page:
            temp_offset += 1
            if char == '\n':
                temp_offset += 1
                if '.' in number_constructor:
                    number = float(number_constructor)
                else:
                    number = int(number_constructor)

                self.append(number)
                self.string_cast += number_constructor + '\n'
                self.read_offset = temp_offset
                number_constructor = ""
            else:
                number_constructor += char

    def save_to_file(self):
        with open(self.directory, 'a') as file:
            file.write(self.to_string())
            self.writings += 1
            file.close()
        self.clear()
        self.string_cast = ""

    def to_string(self, additional_records=[]):
        result = self.string_cast
        for record in additional_records:
            result += str(record) + '\n'
        return result

    def setup(self):
        self.clear_counters()
        self.empty_file = False
        self.read_offset = 0

    def clear_counters(self):
        self.readings = 0
        self.writings = 0

    def empty(self):
        if self:
            return False
        else:
            return True

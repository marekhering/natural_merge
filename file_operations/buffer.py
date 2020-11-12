class Buffer(list):
    def __init__(self, directory, size):
        super(Buffer).__init__()

        self.size = size
        self.directory = directory
        self.read_offset = 0

    def read_number(self):
        if self.empty():
            self.load_from_file()
        number = self.pop(0) if not self.empty() else None
        return number

    def write_record(self, record):
        if len(self.to_string(additional_records=[record])) > self.size:
            self.save_to_file()
        self.append(record)

    def load_from_file(self):
        with open(self.directory, 'r') as file:
            file.seek(self.read_offset, 0)
            page = file.read(self.size)
            file.close()

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
                number_constructor = ""
                self.append(number)
                self.read_offset = temp_offset
            else:
                number_constructor += char

    def save_to_file(self):
        with open(self.directory, 'a') as file:
            file.write(self.to_string())
            file.close()
        self.clear()

    def to_string(self, additional_records=[]):
        result = ""
        for record in self + additional_records:
            result += str(record) + '\n'
        return result

    def empty(self):
        if self:
            return False
        else:
            return True

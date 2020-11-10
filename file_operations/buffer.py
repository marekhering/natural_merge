

class Buffer:
    def __init__(self, size):
        self.size = size
        self.read_buffer = []
        self.save_buffer = []
        self.save_directory = None
        self.read_directory = None

    def read_record(self):
        if self.read_buffer:
            record = self.read_buffer.pop(0)
        else:
            print("trzea sciagnac")

    def save_record(self):
        pass

    def set_save_directory(self, directory):
        self.save_directory = directory

    def set_read_directory(self, directory):
        self.read_directory = directory
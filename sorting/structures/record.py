

class Record:
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        if isinstance(self.value, int) == isinstance(other.value, int):
            return self.value == other.value
        else:
            return False

    def __lt__(self, other):
        if isinstance(self.value, int) == isinstance(other.value, int):
            return self.value < other.value
        elif isinstance(self.value, int):
            return False
        else:
            return True

    def __gt__(self, other):
        if isinstance(self.value, int) == isinstance(other.value, int):
            return self.value > other.value
        elif isinstance(self.value, int):
            return True
        else:
            return False

    def __ne__(self, other):
        return not self == other

    def __le__(self, other):
        return self < other or self == other

    def __ge__(self, other):
        return self > other or self == other

    def is_none(self):
        return self.value is None

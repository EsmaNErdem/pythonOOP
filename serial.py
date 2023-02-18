"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        self.start = start
        self.generator = start 
    
    def __repr__(self):
        return f"<SerialGenerator start={self.start} current={self.generator-1} next={self.generator}>"

    def generate(self):
        self.generator += 1
        return self.generator - 1

    def reset(self):
        self.generator = self.start 
        return
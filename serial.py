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
    counter = 0
    def __init__(self,start=100):
        self.start

    def generate(self):
        """Generates next sequential serial number"""
        srl_num = self.start + self.counter
        self.counter += 1
        return srl_num
    
    
    


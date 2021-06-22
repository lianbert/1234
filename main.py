class Conversion:
    def __init__(self, name: str, ratio: float):
            self.name = name
            self.ratio = ratio
       





    def convert(self, input_unit: float) -> float:
        self.input_unit = input_unit

class Converter:
    def __init__(self):
        self = self
    def add(self, conversion: Conversion):
        self.conversion = conversion

    def convert(self, conversion_name: str, input_unit: float) -> float:
        self.conversion_name = conversion_name
        self.input_unit = input_unit

        

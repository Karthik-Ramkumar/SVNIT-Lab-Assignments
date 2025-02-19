class Converter:
    conversion_factors = {
        "inches": 1,
        "feet": 1 / 12,
        "yards": 1 / 36,
        "miles": 1 / 63360,
        "kilometers": 1 / 39370.1,
        "meters": 1 / 39.3701,
        "centimeters": 1 / 0.393701,
        "millimeters": 1 / 0.0393701
    }

    def __init__(self, length, unit):
        self.length_in_inches = length / self.conversion_factors[unit]

    def inches(self):
        return self.length_in_inches * self.conversion_factors["inches"]

    def feet(self):
        return self.length_in_inches * self.conversion_factors["feet"]

    def yards(self):
        return self.length_in_inches * self.conversion_factors["yards"]

    def miles(self):
        return self.length_in_inches * self.conversion_factors["miles"]

    def kilometers(self):
        return self.length_in_inches * self.conversion_factors["kilometers"]

    def meters(self):
        return self.length_in_inches * self.conversion_factors["meters"]

    def centimeters(self):
        return self.length_in_inches * self.conversion_factors["centimeters"]

    def millimeters(self):
        return self.length_in_inches * self.conversion_factors["millimeters"]

if __name__ == "__main__":
    c = Converter(9, 'inches')
    print(c.feet()) 
    print(c.yards())  
    print(c.miles())  
    print(c.kilometers())  
    print(c.meters())  
    print(c.centimeters())  
    print(c.millimeters())  

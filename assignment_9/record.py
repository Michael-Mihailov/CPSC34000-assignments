class Record:
    def __init__(self, vinNum, city, state, postalCode, modelYear, make, model):
        self.vinNum = vinNum
        self.city = city
        self.state = state
        self.postalCode = postalCode
        self.modelYear = modelYear
        self.make = make
        self.model = model

    def __str__(self):
        return str((self.vinNum, self.city, self.state, self.postalCode, self.modelYear, self.make, self.model))

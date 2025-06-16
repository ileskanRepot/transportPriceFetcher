from datetime import datetime

class Listifier:
    def __init__(self):
        self.allPropertiesList = []
    def __iter__(self):
        for elem in self.allPropertiesList:
            yield elem
    def __getitem__(self, idx):
        return self.allPropertiesList[idx]

class Stations(Listifier):
    joensuu = JNS = "JNS"
    helsinki = HKI = "HKI"
    tampere = TPE = "TPE"

    def __init__(self):
        super().__init__()
        self.allPropertiesList = [self.HKI, self.JNS]
        self.allPropertiesList.sort()

class Passengers(Listifier):
    lapsi = child = "CHILD"
    aikuinen = adult = "ADULT"
    opiskelija = student = "STUDENT"
    asevelvollinen = conscript = "CONSCRIPT"
    eläkeläinen = pensioner = "PENSIONER"

    def __init__(self):
        super().__init__()
        self.allPropertiesList = [self.child, self.adult, self.student, self.conscript, self.pensioner]
        self.allPropertiesList.sort()

class Trip:
    def strToDate(self, stri: str):
        return datetime.fromisoformat(stri)
    def __init__(self, inputJson:dict = None):
        # print(inputJson["arrivalStation"])
        self.departureTime = self.strToDate(inputJson["departureTime"]) if inputJson is not None else None
        self.departureStation = inputJson["departureStation"]           if inputJson is not None else None
        self.arrivalTime = self.strToDate(inputJson["arrivalTime"])     if inputJson is not None else None
        self.arrivalStation = inputJson["arrivalStation"]               if inputJson is not None else None

        self.totalPrice	= int(inputJson["totalPrice"]) if inputJson is not None else None # price in cents

    def __str__(self):
        return f"{self.departureStation}:{self.departureTime} -> {self.arrivalStation}:{self.arrivalTime}, {self.totalPrice /100}€"
    def toDatabase(self):
        pass

stations = Stations()
passengers = Passengers()

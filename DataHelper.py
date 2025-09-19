import os
import pickle

class DataHelper:

    def __init__(self):
        self.default = {
            "firstTAlert": True,
            "meta": 0,
            "progress": 0,
            "mDate": 0,
            "rDate": 0,
            "operator": 0,
            "currentDate": 0,
        }
        self.data = {}

    def dataLoader(self):
        print("Looking for data...")
        if not os.path.exists("Data.data"):
            print("Data not found, creating new data...")
            with open("Data.data", "wb") as dataFile:
                pickle.dump(self.default, dataFile)
            print("Data created")
        if os.path.exists("Data.data"):
            print("Data found, loading...")
            with open("Data.data", "rb") as dataFile:
                self.data = pickle.load(dataFile)
            print("Data loaded")

    def dataSaver(self):
        print("Saving data...")
        with open("Data.data", "wb") as dataFile:
            pickle.dump(self.data, dataFile)
        print("Data saved")

    def getData(self):
        return self.data
    def setData(self, data):
        self.data = data
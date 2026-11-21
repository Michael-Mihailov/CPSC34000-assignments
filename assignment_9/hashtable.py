class HashTable:
    def __init__(self, size):
        self.table = [[] for i in range(size)]
        self.size = size

    def hashFunction(self, key):
        value = 0
        for character in key:
            value = value * 7 + ord(character)
        return value % self.size

    def addRecord(self, record):
            index = self.hashFunction(record.vinNum)
            for oldRecord in self.table[index]:
                if oldRecord.vinNum == record.vinNum:
                    return False
            self.table[index].append(record)
            return True

    def findRecord(self, key):
        index = self.hashFunction(key)
        for record in self.table[index]:
            if record.vinNum == key:
                return record
        return None

    def deleteRecord(self, key):
        index = self.hashFunction(key)
        for record in self.table[index]:
            if record.vinNum == key:
                self.table[index].remove(record)
                return

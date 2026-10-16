import os
from isort import file
import numpy

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


class DSAHashEntry:
    # state: 0 = never used, 1 = used, -1 = formerly-used  
    def __init__(self, inKey=None, inValue=None):
        if inKey is None:
            self.key = ""
            self.value = None
            self.state = 0
        else:
            self.key = inKey
            self.value = inValue
            self.state = 1

#1
class DSAHashTable:
    UPPER_LOAD = 0.7     # "keep load factor below 0.6 or 0.7" 
    LOWER_LOAD = 0.2     # "LF < 0.4 means 60% wasted space" 
    MIN_SIZE = 11
    MAX_STEP = 1         # small prime, "certainly << table size"

    def __init__(self, tableSize):
        actualSize = self._nextPrime(tableSize)
        self.hashArray = numpy.empty(actualSize, dtype=object)
        ii = 0
        while ii < actualSize:
            self.hashArray[ii] = DSAHashEntry()
            ii = ii + 1
        self.count = 0

    #  hashing 
    def _hash(self, inKey):
        hashIndex = 0
        for ch in inKey:                       
            hashIndex = hashIndex + ord(ch)    # FOR ii<-0 TO len(key)-1 loop
        hashIndex = hashIndex % self.hashArray.size
        return hashIndex

    def _stepHash(self, inKey):
        # secondary hash for double hashing
        # hashStep <- MAX_STEP - (key % MAX_STEP)
        total = 0
        for ch in inKey:
            total = total + ord(ch)
        hashStep = self.MAX_STEP - (total % self.MAX_STEP)
        return hashStep

    #  next prime  A2
    def _nextPrime(self, startVal):
        if startVal % 2 == 0:
            primeVal = startVal - 1
        else:
            primeVal = startVal
        isPrime = False
        while not isPrime:
            primeVal = primeVal + 2
            ii = 3
            isPrime = True
            keepChecking = True
            while keepChecking:
                if primeVal % ii == 0:
                    isPrime = False
                else:
                    ii = ii + 2
                # ii <= rootVal from the slide, written as ii*ii <= primeVal
                # so we don't need a sqrt() call
                keepChecking = (ii * ii <= primeVal) and isPrime
        return primeVal

    def _findKey(self, inKey):
        hashIdx = self._hash(inKey)
        origIdx = hashIdx
        step = self._stepHash(inKey)
        found = False
        giveUp = False
        while (not found) and (not giveUp):
            if self.hashArray[hashIdx].state == 0:
                giveUp = True                          # never-used slot: key can't be here
            elif self.hashArray[hashIdx].state == 1 and self.hashArray[hashIdx].key == inKey:
                found = True
            else:
                hashIdx = (hashIdx + step) % self.hashArray.size
                if hashIdx == origIdx:
                    giveUp = True                       # wrapped all the way around
        if found:
            return hashIdx
        return -1

    def _resize(self, requestedSize):
        newSize = self._nextPrime(requestedSize)
        oldArray = self.hashArray
        oldSize = oldArray.size

        self.hashArray = numpy.empty(newSize, dtype=object)
        ii = 0
        while ii < newSize:
            self.hashArray[ii] = DSAHashEntry()
            ii = ii + 1
        self.count = 0

        ii = 0
        while ii < oldSize:
            if oldArray[ii].state == 1:
                self.put(oldArray[ii].key, oldArray[ii].value)   # re-hash into new array
            ii = ii + 1

    def put(self, inKey, inValue):
        hashIdx = self._hash(inKey)
        origIdx = hashIdx
        step = self._stepHash(inKey)
        firstFree = -1        # earliest free-or-formerly-used slot seen along the probe
        found = False
        giveUp = False
        while (not found) and (not giveUp):
            entry = self.hashArray[hashIdx]
            if entry.state == 0:
                if firstFree == -1:
                    firstFree = hashIdx
                giveUp = True
            elif entry.state == 1 and entry.key == inKey:    #dupli`cate key
                found = True
            else:
                if entry.state == -1 and firstFree == -1:
                    firstFree = hashIdx
                hashIdx = (hashIdx + step) % self.hashArray.size
                if hashIdx == origIdx:
                    giveUp = True

        if found:
            self.hashArray[hashIdx].value = inValue          # key exists - overwrite
        else:
            self.hashArray[firstFree].key = inKey
            self.hashArray[firstFree].value = inValue
            self.hashArray[firstFree].state = 1
            self.count = self.count + 1
            if self.getLoadFactor() > self.UPPER_LOAD:
                self._resize(self.hashArray.size * 2)

    def get(self, inKey):
        idx = self._findKey(inKey)
        if idx != -1:
            return self.hashArray[idx].value
        return None

    def hasKey(self, inKey):
        return self._findKey(inKey) != -1

    def remove(self, inKey):
        idx = self._findKey(inKey)
        if idx != -1:
            self.hashArray[idx].state = -1        # formerly-used, NOT free (Lecture 7, "Removal Solution")
            self.hashArray[idx].key = None
            self.hashArray[idx].value = None
            self.count = self.count - 1
            if self.getLoadFactor() < self.LOWER_LOAD and self.hashArray.size > self.MIN_SIZE:
                self._resize(self.hashArray.size // 2)
            return True
        return False

    def getLoadFactor(self):
        return self.count / self.hashArray.size

    # file I/O  A3
    def load(self, filename):
        # expects rows of: id,name  -> key = name, value = id
        file = open(filename, "r")
        rowsLoaded = 0
        for line in file:
            line = line.strip()
            if line != "":
                parts = line.split(",")
                idValue = parts[0]
                nameValue = parts[1]
                self.put(nameValue, idValue)
                rowsLoaded = rowsLoaded + 1
        file.close()
        return rowsLoaded

    def export(self, filename):
        file = open(filename, "w")
        ii = 0
        rowsWritten = 0
        while ii < self.hashArray.size:
            if self.hashArray[ii].state == 1:
                file.write(self.hashArray[ii].value)
                file.write(",")
                file.write(self.hashArray[ii].key)
                file.write("\n")
                rowsWritten = rowsWritten + 1
            ii = ii + 1
        file.close()
        return rowsWritten


#if __name__ == "__main__":
    # table = DSAHashTable(11)

    # rows = table.load(os.path.join(SCRIPT_DIR, "test.csv"))
    # print("rows read from file:", rows)
    # print("entries in table (count):", table.count)
    # print("final table size:", table.hashArray.size)
    # print("Removing 'Katy Vacek' ->", table.remove("Katy Vacek"))
    # #print("final load factor:", table.getLoadFactor())
    # print("entries in table (count):", table.count)


    # #print("hasKey('Nobody Here') ->", table.hasKey("Nobody Here")) 

    # written = table.export(os.path.join(SCRIPT_DIR, "hashtable_output.csv"))
    # print("\nrows written back out:", written)
if __name__ == "__main__":
    table = DSAHashTable(7)
    print("initial table size:", table.hashArray.size)

    rows = table.load(os.path.join(SCRIPT_DIR, "test.csv"))
    print("rows read from file:", rows)
    print("entries in table (count):", table.count)
    print("initial table size:", table.hashArray.size)

    # #Insert
    table.put("Mathew Mercedes", "8")
    print("\nAfter insert:")
    print("entries in table (count):", table.count)
    print("table size:", table.hashArray.size)

    # # Delete
    # print("\nRemoving 'Mathew Mercedes' ->", table.remove("Mathew Mercedes"))
    # print("entries in table (count):", table.count)
    # print("table size:", table.hashArray.size)

    # written = table.export(os.path.join(SCRIPT_DIR, "hashtable_output.csv"))
    # print("\nrows written back out:", written)

 


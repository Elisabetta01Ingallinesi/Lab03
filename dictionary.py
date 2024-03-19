class Dictionary:
    def __init__(self):
        self._dict = []

    def loadDictionary(self,path):
        infile = open(path, "r", encoding="utf-8")
        riga = infile.readline()
        while riga != "":
            parola = riga.rstrip().lower()
            self._dict.append(parola)
            riga = infile.readline()
        infile.close()


    def printAll(self):
        for parola in self._dict:
            print(parola)


    @property
    def dict(self):
        return self._dict
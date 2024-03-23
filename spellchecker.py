import time

import multiDictionary as md

class SpellChecker:

    def __init__(self):
        self.multiDictionary =md.MultiDictionary()

    def handleSentence(self, txtIn, language):
        start_time = time.time()
        sbagliate = []
        testo = replaceChars(txtIn)
        parole = testo.lower().split(" ")

        print("---------------------------------------------------")
        parole_1= self.multiDictionary.searchWord(parole, language)
        for parola in parole_1:
            if parola.corretta == False:
                sbagliate.append(parola)
        end_time = time.time()
        print(f"Numero di parole sbagliate: {len(sbagliate)}")
        for parola in sbagliate:
            print(parola)
        print(f"Time elapsed: {end_time - start_time}")
        print("---------------------------------------------------")

        parole_1=[]
        sbagliate = []
        parole_1 = self.multiDictionary.searchWordLinear(parole, language)
        for parola in parole_1:
            if parola.corretta == False:
                sbagliate.append(parola)
        end_time = time.time()
        print(f"Numero di parole sbagliate: {len(sbagliate)}")
        for parola in sbagliate:
            print(parola)
        print(f"Time elapsed: {end_time-start_time}")
        print("---------------------------------------------------")

        parole_1 = []
        sbagliate = []
        parole_1 = self.multiDictionary.searchWordDichotomic(parole, language)
        for parola in parole_1:
            if parola.corretta == False:
                sbagliate.append(parola)
        end_time = time.time()
        print(f"Numero di parole sbagliate: {len(sbagliate)}")
        for parola in sbagliate:
            print(parola)
        print(f"Time elapsed: {end_time - start_time}")
        print("---------------------------------------------------")


    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")

def replaceChars(text):
    chars = "\\`*_{}[]()>#+-.!$%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text
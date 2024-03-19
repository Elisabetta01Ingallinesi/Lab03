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

        parole= self.multiDictionary.searchWord(parole, language)
        for parola in parole:
            if parola.corretta == False:
                sbagliate.append(parola)
        end_time = time.time()
        for parola in sbagliate:
            print(parola)
            print(f"Numero di parole sbagliate: {len(sbagliate)}")
            print(f"Time elapsed: {end_time-start_time}")



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
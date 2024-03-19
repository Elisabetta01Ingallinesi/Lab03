import dictionary as d
import richWord as rw


class MultiDictionary:

    def __init__(self):
       self.dizionario = d.Dictionary()

    def printDic(self, language):
        self.inizializzazioneDizionario(language)
        self.dizionario.printAll()


    def searchWord(self, words, language):
        parole = []
        self.inizializzazioneDizionario(language)
        for word in words:
            controllo = rw.RichWord(word)
            if word in self.dizionario.dict:
                controllo.corretta= True
            else:
                controllo.corretta=False

            parole.append(controllo)
        return parole


    def inizializzazioneDizionario(self,language):
        if language == "italian":
            self.dizionario.loadDictionary("resources/Italian.txt")
        elif language == "english":
            self.dizionario.loadDictionary("resources/English.txt")
        elif language == "spanish":
            self.dizionario.loadDictionary("resources/Spanish.txt")

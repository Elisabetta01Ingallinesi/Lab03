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

    def searchWordLinear(self, words, language):
        parole = []
        self.inizializzazioneDizionario(language)
        for word in words:
            find = False
            controllo = rw.RichWord(word)
            for element in self.dizionario.dict:
                if element == word:
                    controllo.corretta = True
                    parole.append(controllo)
                    find = True
                    break
            if find==False:
                controllo.corretta = False
                parole.append(controllo)

        return parole

    def searchWordDichotomic(self, words, language):
        parole = []
        self.inizializzazioneDizionario(language)


        meta_lunghezza = len(self.dizionario.dict) // 2
        elem_centrale = self.dizionario.dict[meta_lunghezza]
        for word in words:
            find = False
            controllo = rw.RichWord(word)
            if word == elem_centrale:
                controllo.corretta = True
                parole.append(controllo)
                find = True
            elif elem_centrale < word:
                for i in range(meta_lunghezza,0, -1):
                    if word == self.dizionario.dict[i]:
                        controllo.corretta = True
                        parole.append(controllo)
                        find = True
            elif elem_centrale > word:
                for i in range(meta_lunghezza, len(self.dizionario.dict)):
                    if word == self.dizionario.dict[i]:
                        controllo.corretta = True
                        parole.append(controllo)
                        find = True
            if find == False:
                controllo.corretta = False
                parole.append(controllo)
        return parole


    def inizializzazioneDizionario(self,language):
        if language == "italian":
            self.dizionario.loadDictionary("resources/Italian.txt")
        elif language == "english":
            self.dizionario.loadDictionary("resources/English.txt")
        elif language == "spanish":
            self.dizionario.loadDictionary("resources/Spanish.txt")

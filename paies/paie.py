class Paie:
    def __init__(self, Nomprenom, Numerocarte, dateexp, CVV):
        self.__Nomprenom = Nomprenom 
        self.__Numerocarte = Numerocarte
        self.__dateexp = dateexp
        self.__CVV = CVV

    @property
    def Nomprenom(self):
        return self.__Nomprenom

    @Nomprenom.setter
    def Nomprenom(self, value):
        self.__Nomprenom = value

    @property
    def Numerocarte(self):
        return self.__Numerocarte

    @Numerocarte.setter
    def Numerocarte(self, value):
        self.__Numerocarte = value

    @property
    def dateexp(self):
        return self.__dateexp

    @dateexp.setter
    def dateexp(self, value):
        self.__dateexp = value

    @property
    def CVV(self):
        return self.__CVV

    @CVV.setter
    def CVV(self, value):
        self.__CVV = value
 

        

import database
class Reservation:
    def __init__(self, nom_event, nom_util, nombrePlaces) :
        self.__nomevent = nom_event
        self.__nomutil = nom_util
        self.__nombresPlaces = nombrePlaces

    @property
    def nomevent(self):
        return self.__nomevent

    @nomevent.setter
    def nomevent(self, value):
        self.__nomevent = value

    @property
    def nomutil(self):
        return self.__nomutil

    @nomutil.setter
    def nomutil(self, value):
        self.__nomutil = value

    @property
    def nombresPlaces(self):
        return self.__nombresPlaces

    @nombresPlaces.setter
    def nombresPlaces(self, value):
        self.__nombresPlaces = value


        

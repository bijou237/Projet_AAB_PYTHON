class Evenement:
    def __init__(self, id_event, nom_event, date_event, heure_event, prix_event, nombre_places_event, lieu_event):
        self._id_event = id_event
        self._nom_event = nom_event
        self._date_event = date_event
        self._heure_event = heure_event
        self._prix_event = prix_event
        self._nombre_places_event = nombre_places_event
        self._lieu_event = lieu_event

    @property
    def id_event(self):
        return self._id_event

    @id_event.setter
    def id_event(self, value):
        self._id_event = value

    @property
    def nom_event(self):
        return self._nom_event

    @nom_event.setter
    def nom_event(self, value):
        self._nom_event = value

    @property
    def date_event(self):
        return self._date_event

    @date_event.setter
    def date_event(self, value):
        self._date_event = value

    @property
    def heure_event(self):
        return self._heure_event

    @heure_event.setter
    def heure_event(self, value):
        self._heure_event = value

    @property
    def prix_event(self):
        return self._prix_event

    @prix_event.setter
    def prix_event(self, value):
        self._prix_event = value

    @property
    def nombre_places_event(self):
        return self._nombre_places_event

    @nombre_places_event.setter
    def nombre_places_event(self, value):
        self._nombre_places_event = value

    @property
    def lieu_event(self):
        return self._lieu_event

    @lieu_event.setter
    def lieu_event(self, value):
        self._lieu_event = value

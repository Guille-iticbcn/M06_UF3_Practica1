class Agenda:
    def __init__(self, nom, usuaris, events):
        self._nom = nom
        self._usuaris = usuaris
        self._events = events

    #GETTERS    
    def get_nom(self):
        return self._nom
    
    def get_usuarios(self):
        return self._usuaris
    
    def get_events(self):
        return self._events
    

    #SETTERS
    def set_nom(self, nom):
        self._nom = nom

    def set_usuaris(self, usuaris):
        self._usuaris = usuaris

    def set_events(self, events):
        self._events = events
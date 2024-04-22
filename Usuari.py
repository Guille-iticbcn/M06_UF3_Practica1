class Usuari:
    def __init__(self, id, nom, cognom, nacionalitat):
        self._id = id
        self._nom = nom
        self._cognom = cognom
        self._nacionalitat = nacionalitat

    #GETTERS
    def get_id(self):
        return self._id
    
    def get_nom(self):
        return self._nom
    
    def get_cognom(self):
        return self._cognom
    
    def get_nacionalitat(self):
        return self._nacionalitat
    

    #SETTERS
    def set_id(self, id):
        self._id = id

    def set_nom(self, nom):
        self._nom = nom

    def set_cognom(self, cognom):
        self._cognom = cognom

    def set_nacionalitat(self, nacionalitat):
        self._nacionalitat = nacionalitat
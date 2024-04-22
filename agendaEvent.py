class agendaEvent:
    def __init__(self, fecha, duracion, titulo, descripcion=None, tags=None, ubicacion=None):
        self._fecha = fecha
        self._duracion = duracion
        self._titulo = titulo
        self._descripcion = descripcion
        self._tags = tags #if tags else []
        self._ubicacion = ubicacion

    def __str__(self):
        return f"Evento: {self._titulo}, Fecha: {self._fecha}, Duración: {self._duracion}, Ubicación: {self._ubicacion}"

    def get_fecha(self):
        return self._fecha

    def get_duracion(self):
        return self._duracion

    def get_titulo(self):
        return self._titulo

    def get_descripcion(self):
        return self._descripcion

    def get_tags(self):
        return self._tags

    def get_ubicacion(self):
        return self._ubicacion

    def set_fecha(self, fecha):
        self._fecha = fecha

    def set_duracion(self, duracion):
        self._duracion = duracion

    def set_titulo(self, titulo):
        self._titulo = titulo

    def set_descripcion(self, descripcion):
        self._descripcion = descripcion

    def set_tags(self, tags):
        self._tags = tags

    def set_ubicacion(self, ubicacion):
        self._ubicacion = ubicacion


evento = agendaEvent("2024-04-16", 2, "Reunión de equipo", "descripcion", ["reunión", "equipo"], "Oficina")
print(evento)

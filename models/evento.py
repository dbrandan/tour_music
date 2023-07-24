import json
class Evento:
    def __init__(self,id:int,nombre:str,artista:str,genero:str,id_ubicacion:int,hora_inicio:str,hora_fin:str,descripcion:str,imagen:str):
        self.id=id
        self.nombre=nombre
        self.artista=artista
        self.genero=genero
        self.id_ubicacion=id_ubicacion
        self.hora_inicio=hora_inicio
        self.hora_fin=hora_fin
        self.descripcion=descripcion
        self.imagen=imagen
        self.eventos=[]
    def  agregar_evento(self,evento):
        self.eventos.append(evento)
    

    def buscar_evento_por_nombre(self, nombre):
        nombre_buscado = nombre.lower()
        eventos_encontrados = []   
        for evento in self.eventos:
            if evento.nombre.lower() == nombre_buscado:
                eventos_encontrados.append(evento)
        return eventos_encontrados
    
    #def buscar_evento_por_nombre(self, nombre):
   #     return [evento for evento in self.eventos if evento.nombre.lower() == nombre.lower()]

    def buscar_evento_por_artista(self, artista):
        return [evento for evento in self.eventos if evento.artista.lower() == artista.lower()]

    def buscar_evento_por_genero(self, genero):
        return [evento for evento in self.eventos if evento.genero.lower() == genero.lower()]

    def buscar_evento_por_ubicacion(self, id_ubicacion):
        return [evento for evento in self.eventos if evento.id_ubicacion == id_ubicacion]

    def filtrar_eventos_por_horario(self, hora_inicio):
        return [evento for evento in self.eventos if hora_inicio <= evento.hora_inicio ]
    def filtrar_eventos_por_horario(self, hora_fin):
        return [evento for evento in self.eventos if hora_fin <= evento.hora_inicio ]
    
    @classmethod
    def cargar_de_json(cls, archivo):
        with open(archivo, "r") as f:
            data = json.load(f)
        return [cls(**evento) for evento in data]


import json
class Review:
    def __init__(self, id:int, id_evento:int, id_usuario:int, calificacion:int, comentario:str):
        self.id = id
        self.id_evento = id_evento
        self.id_usuario = id_usuario
        self.calificacion = calificacion
        self.comentario = comentario
        self.reseñas=[]
    def agregar_reseña(self, reseña):
        self.reseñas.append(reseña)
    @classmethod
    def cargar_de_json(cls, archivo):
        with open(archivo, "r") as f:
            data = json.load(f)
        return [cls(**review) for review in data]
     
   
   
   
   
   
   

   
   
   
   
   
   ## def to_json(self):
  ##      return {"id":self.id, "id_evento":{self.id_evento}, "id_usuario":{self.id_usuario}, "calificacion":{self.calificacion},"comentarios":{self.comentarios}, "animo":{self.animo}}
   ## @classmethod
  #  def from_json(cls,json_data):
  #      data= json.loads(json_data)
   #     id = data["id"]
   #     id_evento =data["id_evento"]
   #     id_usuario =data["id_usuario"]
   #     calificacion = data["calificacion"]
   #     comentarios= data["comentarios"]
   #     animo=data["animo"]
   #     return cls(id, id_evento, id_usuario, calificacion, comentarios,animo) 

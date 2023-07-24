import json
import evento
class Usuario:
    def __init__(self, id:int, nombre:str, apellido:str, historial_eventos:list[int]):
        self.id=id
        self.nombre=nombre
        self.apellido=apellido
        self.historial_eventos=historial_eventos
    def mostrar_eventos(self):
        for id in self.historial_eventos:
            

    
    def to_json(self):
        return {"id":self.id, "nombre":{self.nombre}, "historial_eventos":{self.historial_eventos}}
    @classmethod
    def from_json(cls,json_data):
        data= json.loads(json_data)
        id = data["id"]
        nombre =data["nombre"]
        apellido =data["apellido"]
        historial_eventos = data["historial_eventos"]
        return cls(id, nombre, apellido, historial_eventos) 
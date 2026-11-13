from abc import ABC, abstractmethod
class Servicio(ABC):
    def __init__(self,nombre: str, tarifa_base: float):
        @abstractmethod
        def calcular_costo(self, *args, **kwargs):
            pass
# Servicio especializado 1: Reserva de salas
class ReservaSalas(Servicio):
    def __init__( self, nombre: str, tarifa_base: float, capacidad_personas: int):
        super().__init__(nombre, tarifa_base)
        self.capacidad_personas=capacidad_personas
# Método con parámetros opcionales para calcular el costo con impuesto
    def calcular_costo(self, horas:int = 1, impuesto: float=0.19)-> float:
       f horas <= 0:
            raise ValueError("Error las horas de reservas deben ser mayor a cero.")
        subtotal= self.tarifa_base * horas
       return subtotal + (subtotal * impuesto)
# 3. Servicio especializado 2: Alquiler de equipos
class AlquilerEquipos(Servicio):
    def __init__(self, nombre, str, tarifa_base: float, codigo_equipo: str):
        super(). __init__(nombre, tarifa_base)
        self.codigo_equipo = codigo_equipo
# Método con parámetros opcionales para calcular el costo con descuento
def calcular_costo(serlf, dias: int= 1,descuento: float= 0.0)-> float:
    if dias <= 0:
        raise ValueError("Error: Los días de alquiler deben ser mayores a cero.")
    subtotal= self.tarifa_base
    return subtotal - (subtotal * descuento)
# 4. Servicio especializado 3: Asesorías especializadas
class AsesoriaEspecializada(Servicio):
    def __init__(self, nombre:str,tarifa_base: float, especialidad: str):
        super(). __init__(nombre, tarifa_base)
        self.especialidad = especialidad
# Método con parámetros opcionales para sesiones y recargo nocturno
def calcular_costo(self, sesiones: int = 1, recargo_nocturno: bool= False) -> float:
    if sesiones<= 0:
        raise ValueError("Error: El número de sesiones debe ser mayor a cero.")
        subtotal = self.tarifa_base * sesiones
        if recargo_nocturno:
            subtotal *= 1.25
            return subtota

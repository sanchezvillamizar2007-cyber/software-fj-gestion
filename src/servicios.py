from abc import ABC, abstractmethod
from src.excepciones import DatosServicioInvalidosError, ServicioNoDisponibleError

class Servicio(ABC):
    def __init__(self, nombre: str, tarifa_base: float, disponible: bool = True):
        self.nombre = nombre
        self.tarifa_base = tarifa_base
        self.disponible = disponible

    @abstractmethod
    def calcular_costo(self, *args, **kwargs):
        pass

# Servicio especializado 1: Reserva de salas
class ReservaSalas(Servicio):
    def __init__(self, nombre: str, tarifa_base: float, capacidad_personas: int, disponible: bool = True):
        super().__init__(nombre, tarifa_base, disponible)
        self.capacidad_personas = capacidad_personas

    # Método con parámetros opcionales para calcular el costo con impuesto
    def calcular_costo(self, horas: int = 1, impuesto: float = 0.19) -> float:
        if not self.disponible:
            raise ServicioNoDisponibleError(f"Error: La sala '{self.nombre}' no está disponible.")
        if horas <= 0:
            raise DatosServicioInvalidosError("Error: Las horas de reserva deben ser mayores a cero.")
        subtotal = self.tarifa_base * horas
        return subtotal + (subtotal * impuesto)

# Servicio especializado 2: Alquiler de equipos
class AlquilerEquipos(Servicio):
    def __init__(self, nombre: str, tarifa_base: float, codigo_equipo: str, disponible: bool = True):
        super().__init__(nombre, tarifa_base, disponible)
        self.codigo_equipo = codigo_equipo

    # Método con parámetros opcionales para calcular el costo con descuento
    def calcular_costo(self, dias: int = 1, descuento: float = 0.0) -> float:
        if not self.disponible:
            raise ServicioNoDisponibleError(f"Error: El equipo '{self.nombre}' no está disponible.")
        if dias <= 0:
            raise DatosServicioInvalidosError("Error: Los días de alquiler deben ser mayores a cero.")
        subtotal = self.tarifa_base * dias
        return subtotal - (subtotal * descuento)

# Servicio especializado 3: Asesorías especializadas
class AsesoriaEspecializada(Servicio):
    def __init__(self, nombre: str, tarifa_base: float, especialidad: str, disponible: bool = True):
        super().__init__(nombre, tarifa_base, disponible)
        self.especialidad = especialidad

    # Método con parámetros opcionales para sesiones y recargo nocturno
    def calcular_costo(self, sesiones: int = 1, recargo_nocturno: bool = False) -> float:
        if not self.disponible:
            raise ServicioNoDisponibleError(f"Error: La asesoría '{self.nombre}' no está disponible.")
        if sesiones <= 0:
            raise DatosServicioInvalidosError("Error: El número de sesiones debe ser mayor a cero.")
        subtotal = self.tarifa_base * sesiones
        if recargo_nocturno:
            subtotal *= 1.25  # Aplica un 25% extra por recargo nocturno
        return subtotal

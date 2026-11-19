from datetime import datetime
from src.entidades import Entidad, Cliente
from src.servicios import Servicio
from src.excepciones import DatosReservaInvalidosError, ReservaCanceladaError, ServicioNoDisponibleError

class Reserva(Entidad):
    """Representa una reserva de servicio realizada por un cliente en el sistema."""
    
    _contador_reservas = 0

    def __init__(self, cliente: Cliente, servicio: Servicio, cantidad: int = 1):
        super().__init__()
        self.cliente = cliente
        self.servicio = servicio
        self.cantidad = cantidad
        self.fecha_reserva = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.activa = True
        self.costo_total = self._calcular_total_reserva()

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, valor):
        if not isinstance(valor, Cliente):
            raise DatosReservaInvalidosError("La reserva debe estar asociada a un objeto Cliente válido.")
        self.__cliente = valor

    @property
    def servicio(self):
        return self.__servicio

    @servicio.setter
    def servicio(self, valor):
        if not isinstance(valor, Servicio):
            raise DatosReservaInvalidosError("La reserva debe estar asociada a un objeto Servicio válido.")
        if not valor.disponible:
            raise ServicioNoDisponibleError(f"El servicio '{valor.nombre}' no se puede reservar porque no está disponible.")
        self.__servicio = valor

    @property
    def cantidad(self):
        return self.__cantidad

    @cantidad.setter
    def cantidad(self, valor):
        if not isinstance(valor, int) or valor <= 0:
            raise DatosReservaInvalidosError("La cantidad de unidades (horas/días/sesiones) debe ser un número entero mayor a cero.")
        self.__cantidad = valor

    def _calcular_total_reserva(self) -> float:
        """Calcula el costo total usando el método polimórfico del servicio."""
        try:
            return float(self.servicio.calcular_costo(self.cantidad))
        except Exception as e:
            raise DatosReservaInvalidosError(f"No se pudo calcular el costo de la reserva: {e}") from e

    def cancelar_reserva(self):
        """Cancela la reserva si se encuentra activa."""
        if not self.activa:
            raise ReservaCanceladaError("La reserva ya se encuentra cancelada previamente.")
        self.activa = False
        self.servicio.disponible = True  # Libera el servicio nuevamente

    def describir(self) -> str:
        estado = "Activa" if self.activa else "Cancelada"
        return (
            f"Reserva #{self.id_entidad} [{estado}] - "
            f"Cliente: {self.cliente.nombre} | Servicio: {self.servicio.nombre} | "
            f"Cantidad: {self.cantidad} | Total: ${self.costo_total:.2f} (Fecha: {self.fecha_reserva})"
        )
# Clase base personalizada para todo el sistema de gestión
class SistemaGestionError(Exception):
    """Excepción base para errores del sistema de gestión."""
    pass


# --- Excepciones del módulo de Servicios ---
class DatosServicioInvalidosError(SistemaGestionError):
    """Se lanza cuando los parámetros de cálculo de un servicio no son válidos."""
    pass


class ServicioNoDisponibleError(SistemaGestionError):
    """Se lanza cuando se intenta usar o reservar un servicio inactivo o sin cupo."""
    pass


# --- Excepciones del módulo de Clientes ---
class DatosClienteInvalidosError(SistemaGestionError):
    """Se lanza cuando los datos de un cliente no son válidos."""
    pass


class ClienteDuplicadoError(SistemaGestionError):
    """Se lanza cuando ya existe un cliente con el mismo documento."""
    pass


class ClienteNoEncontradoError(SistemaGestionError):
    """Se lanza cuando no se encuentra el cliente buscado."""
    pass


# --- Excepciones del módulo de Reservas ---
class DatosReservaInvalidosError(SistemaGestionError):
    """Se lanza cuando los datos de una reserva no son válidos."""
    pass


class ReservaCanceladaError(SistemaGestionError):
    """Se lanza cuando se intenta operar sobre una reserva ya cancelada."""
    pass
# Clase base personalizada para todo el sistema de gestión
class SistemaGestionError(Exception):
    """Excepción base para errores del sistema de gestión."""
    pass

# Error específico para datos inválidos en los servicios (horas, días, sesiones)
class DatosServicioInvalidosError(SistemaGestionError):
    """Se lanza cuando los parámetros de cálculo de un servicio no son válidos."""
    pass

# Error específico cuando un servicio no está disponible
class ServicioNoDisponibleError(SistemaGestionError):
    """Se lanza cuando se intenta usar o reservar un servicio inactivo o sin cupo."""
    pass

# Error específico para datos inválidos de un cliente
class DatosClienteInvalidosError(SistemaGestionError):
    """Se lanza cuando los datos de un cliente no son válidos."""
    pass

# Error específico cuando se intenta registrar un cliente repetido
class ClienteDuplicadoError(SistemaGestionError):
    """Se lanza cuando ya existe un cliente con el mismo documento."""
    pass

# Error específico cuando no se encuentra un cliente
class ClienteNoEncontradoError(SistemaGestionError):
    """Se lanza cuando no se encuentra el cliente buscado."""
    pass

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

"""
Módulo 1 - Entidades y Clientes (Software FJ)

Contiene:
  - Entidad: clase abstracta base de las entidades del sistema.
  - Cliente: entidad con datos personales encapsulados y validados.
  - GestorClientes: administra una lista interna de clientes.

Nota: este módulo solo LANZA excepciones. El registro en el archivo de logs
se hace en el bloque except que maneja el error de forma definitiva
(por ejemplo en main.py), para no registrar el mismo error dos veces.
"""

# re permite validar textos con expresiones regulares (ej. el correo)
import re
# ABC y abstractmethod permiten crear clases abstractas
from abc import ABC, abstractmethod

# Excepciones personalizadas del sistema (archivo compartido por el equipo).
# Se importa con el prefijo "src." igual que en servicios.py, porque el
# proyecto se ejecuta desde la carpeta raíz (donde está main.py).
from src.excepciones import (
    DatosClienteInvalidosError,
    ClienteDuplicadoError,
    ClienteNoEncontradoError,
)


class Entidad(ABC):
    """Clase abstracta que representa cualquier entidad general del sistema."""

    # Atributo de clase: contador compartido para dar un id único a cada entidad
    _contador = 0

    def __init__(self):
        # Aumenta el contador compartido en uno
        Entidad._contador += 1
        # Guarda el id de esta entidad (atributo protegido, con un guion bajo)
        self._id_entidad = Entidad._contador

    @property
    def id_entidad(self):
        """Devuelve el id de la entidad (solo lectura: no tiene setter)."""
        return self._id_entidad

    @abstractmethod
    def describir(self):
        """Cada entidad concreta debe explicar cómo se describe (polimorfismo)."""

    def __str__(self):
        # Al imprimir la entidad se muestra su descripción
        return self.describir()

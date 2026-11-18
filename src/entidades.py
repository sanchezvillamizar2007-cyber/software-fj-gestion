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

class Cliente(Entidad):
    """Cliente de Software FJ con datos personales encapsulados."""

    def __init__(self, nombre, documento, correo, telefono=None):
        # Primero se valida todo; si algo falla se lanza la excepción y el
        # cliente no se crea (así no se gasta un id con datos inválidos).
        self.nombre = nombre          # usa el setter de nombre
        self.documento = documento    # usa el setter de documento
        self.correo = correo          # usa el setter de correo
        self.telefono = telefono      # usa el setter de teléfono (opcional)
        # Solo si todo fue válido se asigna el id llamando a la clase padre
        super().__init__()

    # ---------- Nombre ----------
    @property
    def nombre(self):
        """Devuelve el nombre del cliente."""
        return self.__nombre  # atributo privado (name mangling)

    @nombre.setter
    def nombre(self, valor):
        """Valida y guarda el nombre."""
        self.__nombre = self._validar_nombre(valor)

    @staticmethod
    def _validar_nombre(valor):
        # Debe ser texto y no estar vacío ni ser solo espacios
        if not isinstance(valor, str) or not valor.strip():
            raise DatosClienteInvalidosError("El nombre es obligatorio y debe ser texto.")
        # Quita espacios sobrantes entre palabras
        nombre = " ".join(valor.split())
        # Debe tener al menos 3 caracteres
        if len(nombre) < 3:
            raise DatosClienteInvalidosError("El nombre debe tener al menos 3 caracteres.")
        # Solo letras (con tildes y ñ) y espacios
        if not re.fullmatch(r"[A-Za-zÁÉÍÓÚÜÑáéíóúüñ ]+", nombre):
            raise DatosClienteInvalidosError("El nombre solo puede contener letras y espacios.")
        # Devuelve el nombre con la primera letra de cada palabra en mayúscula
        return nombre.title()

    # ---------- Documento ----------
    @property
    def documento(self):
        """Devuelve el número de documento (texto)."""
        return self.__documento

    @documento.setter
    def documento(self, valor):
        """Valida y guarda el documento."""
        self.__documento = self._validar_documento(valor)

    @staticmethod
    def _validar_documento(valor):
        # Convierte a texto y quita espacios
        texto = str(valor).strip()
        try:
            # Intenta convertir a número; si falla, se encadena la excepción
            int(texto)
        except ValueError as error:
            # "from error" conserva el error original (encadenamiento)
            raise DatosClienteInvalidosError(
                "El documento debe contener solo números."
            ) from error
        # Debe tener solo dígitos y entre 6 y 12 caracteres
        if not texto.isdigit() or not 6 <= len(texto) <= 12:
            raise DatosClienteInvalidosError(
                "El documento debe tener entre 6 y 12 dígitos."
            )
        return texto

    # ---------- Correo ----------
    @property
    def correo(self):
        """Devuelve el correo electrónico."""
        return self.__correo

    @correo.setter
    def correo(self, valor):
        """Valida y guarda el correo."""
        self.__correo = self._validar_correo(valor)

    @staticmethod
    def _validar_correo(valor):
        # Debe ser texto
        if not isinstance(valor, str):
            raise DatosClienteInvalidosError("El correo debe ser texto.")
        correo = valor.strip().lower()
        # Formato básico: algo@dominio.ext
        if not re.fullmatch(r"[\w.+-]+@[\w-]+(\.[\w-]+)*\.[a-z]{2,}", correo):
            raise DatosClienteInvalidosError("El correo no tiene un formato válido.")
        return correo

    # ---------- Teléfono (opcional) ----------
    @property
    def telefono(self):
        """Devuelve el teléfono o None si no se registró."""
        return self.__telefono

    @telefono.setter
    def telefono(self, valor):
        """Valida y guarda el teléfono (puede ser None)."""
        self.__telefono = self._validar_telefono(valor)

    @staticmethod
    def _validar_telefono(valor):
        # El teléfono es opcional
        if valor is None:
            return None
        texto = str(valor).strip()
        # Debe tener exactamente 10 dígitos
        if not texto.isdigit() or len(texto) != 10:
            raise DatosClienteInvalidosError("El teléfono debe tener 10 dígitos.")
        return texto

    # ---------- Polimorfismo ----------
    def describir(self):
        """Implementa el método abstracto de Entidad."""
        telefono = self.__telefono if self.__telefono else "No registrado"
        return (
            f"Cliente #{self.id_entidad}: {self.__nombre} | "
            f"Documento: {self.__documento} | Correo: {self.__correo} | "
            f"Teléfono: {telefono}"
        )

import os
import logging
from src.excepciones import DatosServicioInvalidosError, ServicioNoDisponibleError
from src.servicios import ReservaSalas, AlquilerEquipos, AsesoriaEspecializada

# 1. Creamos la carpeta 'logs' si no existe y configuramos el registro de errores
os.makedirs("logs", exist_ok=True)
logging.basicConfig(
    filename="logs/errores_servicios.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

print("=== INICIANDO PRUEBAS DEL MÓDULO DE SERVICIOS ===\n")

# --- PRUEBA 1: try / except (Error por datos inválidos) ---
sala = ReservaSalas("Sala Juntas VIP", 50000, 10)
try:
    print("1. Probando reserva con horas negativas...")
    sala.calcular_costo(horas=-3)
except DatosServicioInvalidosError as e:
    print(f"   [Capturado]: {e}")
    logging.error(f"Prueba 1 - {e}")

# --- PRUEBA 2: try / except / else (Operación exitosa) ---
try:
    print("\n2. Probando reserva válida de 2 horas...")
    costo_sala = sala.calcular_costo(horas=2)
except DatosServicioInvalidosError as e:
    print(f"   [Error]: {e}")
    logging.error(f"Prueba 2 - {e}")
else:
    print(f"   [Éxito en else]: El costo total de la sala es ${costo_sala}")

# --- PRUEBA 3: try / except / finally (Servicio no disponible) ---
equipo = AlquilerEquipos("Proyector Epson", 30000, "EQ-01", disponible=False)
try:
    print("\n3. Probando alquiler de equipo no disponible...")
    equipo.calcular_costo(dias=2)
except ServicioNoDisponibleError as e:
    print(f"   [Capturado]: {e}")
    logging.error(f"Prueba 3 - {e}")
finally:
    print("   [Finally]: Verificación de disponibilidad finalizada.")

# --- PRUEBA 4: Encadenamiento de excepciones (raise ... from ...) ---
asesoria = AsesoriaEspecializada("Asesoría en Redes", 80000, "Infraestructura")
try:
    print("\n4. Probando encadenamiento de excepciones...")
    try:
        sesiones_usuario = int("tres")  # Provocamos un ValueError técnico al convertir texto
        asesoria.calcular_costo(sesiones=sesiones_usuario)
    except ValueError as error_tecnico:
        raise DatosServicioInvalidosError("La cantidad de sesiones debe ser un número entero.") from error_tecnico
except DatosServicioInvalidosError as e:
    print(f"   [Excepción encadenada]: {e} | Causa original: {type(e.__cause__).__name__}")
    logging.error(f"Prueba 4 - {e} (Causa: {e.__cause__})")

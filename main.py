import os
import logging
from src.excepciones import (
    DatosServicioInvalidosError,
    ServicioNoDisponibleError,
    DatosClienteInvalidosError,
    ClienteDuplicadoError,
    ClienteNoEncontradoError,
    DatosReservaInvalidosError,
    ReservaCanceladaError
)
from src.entidades import Cliente, GestorClientes
from src.servicios import ReservaSalas, AlquilerEquipos, AsesoriaEspecializada
from src.reservas import Reserva

# Configuración del archivo de log unificado para todo el sistema (Observación 3 del profesor)
os.makedirs("logs", exist_ok=True)
logging.basicConfig(
    filename="logs/sistema.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def ejecutar_simulaciones():
    print("==================================================")
    print("   INICIANDO SIMULACIÓN INTEGRAL - SOFTWARE FJ    ")
    print("==================================================\n")

    gestor = GestorClientes()

    # ----------------------------------------------------
    # SIMULACIÓN 1: Registro exitoso de un cliente válido
    # ----------------------------------------------------
    print("--- SIMULACIÓN 1: Registro de Cliente Válido ---")
    try:
        c1 = Cliente("Carlos Pérez", "12345678", "carlos@mail.com", "3001234567")
        gestor.registrar_cliente(c1)
        print(f" [Éxito]: {c1}")
    except Exception as e:
        print(f" [Error inesperado]: {e}")

    # ----------------------------------------------------
    # SIMULACIÓN 2: Excepción por datos de cliente inválidos
    # ----------------------------------------------------
    print("\n--- SIMULACIÓN 2: Error por Cliente Inválido (Nombre corto) ---")
    try:
        Cliente("Jo", "87654321", "jo@mail.com")
    except DatosClienteInvalidosError as e:
        print(f" [Capturado con éxito]: {e}")
        logging.error(f"Simulación 2 - {e}")

    # ----------------------------------------------------
    # SIMULACIÓN 3: Excepción por documento duplicado
    # ----------------------------------------------------
    print("\n--- SIMULACIÓN 3: Error por Cliente Duplicado ---")
    try:
        c2 = Cliente("Ana Gómez", "12345678", "ana@mail.com") # Mismo documento que Carlos
        gestor.registrar_cliente(c2)
    except ClienteDuplicadoError as e:
        print(f" [Capturado con éxito]: {e}")
        logging.error(f"Simulación 3 - {e}")

    # ----------------------------------------------------
    # SIMULACIÓN 4: Búsqueda exitosa de cliente
    # ----------------------------------------------------
    print("\n--- SIMULACIÓN 4: Búsqueda Exitosa de Cliente ---")
    try:
        encontrado = gestor.buscar_cliente(documento="12345678")
        print(f" [Encontrado]: {encontrado.nombre} - Correo: {encontrado.correo}")
    except Exception as e:
        print(f" [Error]: {e}")

    # ----------------------------------------------------
    # SIMULACIÓN 5: Excepción por cliente no encontrado
    # ----------------------------------------------------
    print("\n--- SIMULACIÓN 5: Error por Cliente No Encontrado ---")
    try:
        gestor.buscar_cliente(documento="99999999")
    except ClienteNoEncontradoError as e:
        print(f" [Capturado con éxito]: {e}")
        logging.error(f"Simulación 5 - {e}")

    # ----------------------------------------------------
    # SIMULACIÓN 6: Creación y cálculo de Reserva de Sala (con IVA)
    # ----------------------------------------------------
    print("\n--- SIMULACIÓN 6: Reserva de Sala Exitosa (try/else) ---")
    sala = ReservaSalas("Auditorio Principal", 100000, 50)
    try:
        cliente_ref = gestor.buscar_cliente(documento="12345678")
        reserva_sala = Reserva(cliente_ref, sala, cantidad=3) # 3 horas
    except Exception as e:
        print(f" [Error]: {e}")
    else:
        print(f" [Éxito en else]: {reserva_sala}")
        print(f" Costo calculado con IVA (19%): ${reserva_sala.costo_total}")

    # ----------------------------------------------------
    # SIMULACIÓN 7: Excepción por horas de sala inválidas (Negativas)
    # ----------------------------------------------------
    print("\n--- SIMULACIÓN 7: Error por Horas Negativas en Sala ---")
    try:
        sala.calcular_costo(horas=-5)
    except DatosServicioInvalidosError as e:
        print(f" [Capturado con éxito]: {e}")
        logging.error(f"Simulación 7 - {e}")

    # ----------------------------------------------------
    # SIMULACIÓN 8: Excepción por Alquiler de Equipo No Disponible (try/finally)
    # ----------------------------------------------------
    print("\n--- SIMULACIÓN 8: Alquiler de Equipo No Disponible ---")
    equipo = AlquilerEquipos("Servidor Rack", 200000, "SRV-01", disponible=False)
    try:
        cliente_ref = gestor.buscar_cliente(documento="12345678")
        Reserva(cliente_ref, equipo, cantidad=2)
    except ServicioNoDisponibleError as e:
        print(f" [Capturado con éxito]: {e}")
        logging.error(f"Simulación 8 - {e}")
    finally:
        print(" [Finally]: Verificación de disponibilidad de equipos finalizada.")

    # ----------------------------------------------------
    # SIMULACIÓN 9: Asesoría Especializada con Recargo Nocturno
    # ----------------------------------------------------
    print("\n--- SIMULACIÓN 9: Asesoría Especializada con Recargo Nocturno ---")
    asesoria = AsesoriaEspecializada("Arquitectura de Software", 150000, "Backend")
    try:
        cliente_ref = gestor.buscar_cliente(documento="12345678")
        # Calculamos directo aplicando recargo nocturno (25% extra)
        costo_asesoria = asesoria.calcular_costo(sesiones=2, recargo_nocturno=True)
        print(f" [Éxito]: Asesoría '{asesoria.nombre}' para 2 sesiones con recargo nocturno. Total: ${costo_asesoria}")
    except Exception as e:
        print(f" [Error]: {e}")

    # ----------------------------------------------------
    # SIMULACIÓN 10: Cancelación de Reserva y validación de excepción
    # ----------------------------------------------------
    print("\n--- SIMULACIÓN 10: Cancelación de Reserva ---")
    try:
        cliente_ref = gestor.buscar_cliente(documento="12345678")
        otra_sala = ReservaSalas("Sala de Juntas B", 60000, 10)
        reserva_temporal = Reserva(cliente_ref, otra_sala, cantidad=1)
        
        print(f" Estado inicial: {reserva_temporal.activa}")
        reserva_temporal.cancelar_reserva()
        print(f" Estado tras cancelar: {reserva_temporal.activa}")
        
        # Intentamos cancelar de nuevo para forzar la excepción de reserva ya cancelada
        reserva_temporal.cancelar_reserva()
    except ReservaCanceladaError as e:
        print(f" [Capturado con éxito]: {e}")
        logging.error(f"Simulación 10 - {e}")

    print("\n==================================================")
    print("   SIMULACIONES FINALIZADAS CON ÉXITO             ")
    print("==================================================")

if __name__ == "__main__":
    ejecutar_simulaciones()

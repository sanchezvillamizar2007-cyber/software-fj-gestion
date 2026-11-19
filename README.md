# software-fj-gestion
Software FJ - Gestión de Clientes, Servicios y Reservas

Proyecto de la Fase 4 del curso Programación (213023), UNAD, grupo 41.

Sistema en Python orientado a objetos, sin base de datos, que gestiona clientes,
servicios y reservas de la empresa Software FJ. Maneja los errores con excepciones
personalizadas y los registra en un archivo de log.

# Integrantes

- Stiven Sánchez Villamizar: entidades y clientes.
- Joilson Martínez Arrieta: servicios, reservas, excepciones y simulaciones.

Archivos principales

- `main.py`: ejecuta las 10 simulaciones del sistema.
- `src/entidades.py`: clases `Entidad`, `Cliente` y `GestorClientes`.
- `src/servicios.py`: clase `Servicio` y los tres servicios (salas, equipos y asesorías).
- `src/reservas.py`: clase `Reserva`.
- `src/excepciones.py`: excepciones personalizadas del sistema.
- `logs/sistema.log`: registro de errores, se genera al ejecutar.

# Cómo ejecutarlo

Requiere Python 3.8 o superior. Desde la carpeta del proyecto:

```
python main.py
```

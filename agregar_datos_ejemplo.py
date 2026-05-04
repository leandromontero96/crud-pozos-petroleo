"""
Script para agregar datos de ejemplo a la base de datos
Ejecutar: python agregar_datos_ejemplo.py
"""

from app import app, db
from models import Pozo
from datetime import datetime, timedelta
import random

def agregar_datos_ejemplo():
    """Agrega pozos de ejemplo a la base de datos"""

    with app.app_context():
        # Verificar si ya hay datos
        count = Pozo.query.count()
        if count > 0:
            print(f"⚠️  La base de datos ya contiene {count} pozo(s).")
            respuesta = input("¿Desea agregar más datos de ejemplo? (s/n): ")
            if respuesta.lower() != 's':
                print("Operación cancelada.")
                return

        # Datos de ejemplo
        pozos_ejemplo = [
            {
                'nombre': 'Pozo Norte-1',
                'ubicacion': 'Cuenca de Burgos, Tamaulipas',
                'latitud': 25.8756,
                'longitud': -98.3421,
                'produccion_diaria': 1250.5,
                'produccion_gas': 850.0,
                'produccion_agua': 120.0,
                'estado': 'Activo',
                'profundidad': 2850.0,
                'fecha_inicio': datetime.now() - timedelta(days=730),
                'operador': 'Pemex Exploración',
                'campo': 'Campo Burgos Norte',
                'notas': 'Pozo con excelente producción. Requiere mantenimiento preventivo cada 6 meses.'
            },
            {
                'nombre': 'Pozo Sur-5',
                'ubicacion': 'Región Sur, Tabasco',
                'latitud': 18.1234,
                'longitud': -93.5678,
                'produccion_diaria': 2100.0,
                'produccion_gas': 1200.0,
                'produccion_agua': 180.0,
                'estado': 'Activo',
                'profundidad': 3200.0,
                'fecha_inicio': datetime.now() - timedelta(days=1095),
                'operador': 'Pemex Exploración',
                'campo': 'Campo Muspac',
                'notas': 'Uno de los pozos más productivos de la región.'
            },
            {
                'nombre': 'Pozo Marina-3',
                'ubicacion': 'Aguas Someras, Golfo de México',
                'latitud': 19.8765,
                'longitud': -92.1234,
                'produccion_diaria': 3500.0,
                'produccion_gas': 2100.0,
                'produccion_agua': 250.0,
                'estado': 'Activo',
                'profundidad': 4100.0,
                'fecha_inicio': datetime.now() - timedelta(days=1825),
                'operador': 'Pemex Exploración',
                'campo': 'Campo Ku-Maloob-Zaap',
                'notas': 'Pozo offshore de alta producción. Plataforma fija.'
            },
            {
                'nombre': 'Pozo Occidente-2',
                'ubicacion': 'Cuenca de Veracruz',
                'latitud': 20.1234,
                'longitud': -97.4567,
                'produccion_diaria': 850.0,
                'produccion_gas': 450.0,
                'produccion_agua': 95.0,
                'estado': 'Mantenimiento',
                'profundidad': 2200.0,
                'fecha_inicio': datetime.now() - timedelta(days=2190),
                'operador': 'Pemex Exploración',
                'campo': 'Campo Poza Rica',
                'notas': 'En mantenimiento programado. Se espera reanudar operaciones en 2 semanas.'
            },
            {
                'nombre': 'Pozo Centro-7',
                'ubicacion': 'Chicontepec, Veracruz',
                'latitud': 21.0987,
                'longitud': -97.8765,
                'produccion_diaria': 450.0,
                'produccion_gas': 200.0,
                'produccion_agua': 60.0,
                'estado': 'Activo',
                'profundidad': 1800.0,
                'fecha_inicio': datetime.now() - timedelta(days=365),
                'operador': 'Pemex Exploración',
                'campo': 'Campo Chicontepec',
                'notas': 'Pozo reciente con producción estable.'
            },
            {
                'nombre': 'Pozo Norte-8',
                'ubicacion': 'Sabinas, Coahuila',
                'latitud': 27.8765,
                'longitud': -101.1234,
                'produccion_diaria': 320.0,
                'produccion_gas': 150.0,
                'produccion_agua': 40.0,
                'estado': 'Inactivo',
                'profundidad': 1500.0,
                'fecha_inicio': datetime.now() - timedelta(days=3650),
                'operador': 'Pemex Exploración',
                'campo': 'Campo Sabinas',
                'notas': 'Pozo en evaluación para reactivación. Producción declinante.'
            },
            {
                'nombre': 'Pozo Litoral-4',
                'ubicacion': 'Reforma, Chiapas',
                'latitud': 18.2345,
                'longitud': -93.2109,
                'produccion_diaria': 1800.0,
                'produccion_gas': 950.0,
                'produccion_agua': 140.0,
                'estado': 'Activo',
                'profundidad': 2950.0,
                'fecha_inicio': datetime.now() - timedelta(days=1460),
                'operador': 'Pemex Exploración',
                'campo': 'Campo Reforma',
                'notas': 'Buen desempeño. Monitoreado continuamente.'
            },
            {
                'nombre': 'Pozo Aguas Profundas-1',
                'ubicacion': 'Golfo de México, Perdido',
                'latitud': 26.1234,
                'longitud': -94.5678,
                'produccion_diaria': 4200.0,
                'produccion_gas': 2800.0,
                'produccion_agua': 320.0,
                'estado': 'Activo',
                'profundidad': 5500.0,
                'fecha_inicio': datetime.now() - timedelta(days=1095),
                'operador': 'Shell México',
                'campo': 'Campo Perdido',
                'notas': 'Proyecto de aguas profundas. Tecnología de punta.'
            }
        ]

        # Agregar pozos a la base de datos
        pozos_agregados = 0
        for pozo_data in pozos_ejemplo:
            try:
                # Verificar si el pozo ya existe
                existe = Pozo.query.filter_by(nombre=pozo_data['nombre']).first()
                if not existe:
                    nuevo_pozo = Pozo(**pozo_data)
                    db.session.add(nuevo_pozo)
                    pozos_agregados += 1
                    print(f"✅ Agregado: {pozo_data['nombre']}")
                else:
                    print(f"⚠️  Ya existe: {pozo_data['nombre']}")
            except Exception as e:
                print(f"❌ Error al agregar {pozo_data['nombre']}: {str(e)}")

        # Commit de los cambios
        try:
            db.session.commit()
            print(f"\n🎉 ¡Proceso completado!")
            print(f"📊 Pozos agregados: {pozos_agregados}")
            print(f"📊 Total de pozos en la base de datos: {Pozo.query.count()}")
        except Exception as e:
            db.session.rollback()
            print(f"\n❌ Error al guardar los datos: {str(e)}")

def generar_datos_aleatorios(cantidad=10):
    """Genera una cantidad específica de pozos con datos aleatorios"""

    with app.app_context():
        estados = ['Activo', 'Inactivo', 'Mantenimiento']
        operadores = ['Pemex Exploración', 'Shell México', 'Chevron México', 'Total México']
        campos = ['Campo Norte', 'Campo Sur', 'Campo Este', 'Campo Oeste', 'Campo Centro']
        ubicaciones = [
            'Tamaulipas', 'Veracruz', 'Tabasco', 'Chiapas',
            'Campeche', 'Coahuila', 'Golfo de México'
        ]

        pozos_generados = 0
        for i in range(cantidad):
            try:
                numero_pozo = random.randint(1, 999)
                nombre = f"Pozo-{numero_pozo}"

                # Verificar si ya existe
                if Pozo.query.filter_by(nombre=nombre).first():
                    nombre = f"Pozo-{numero_pozo}-{random.randint(100, 999)}"

                nuevo_pozo = Pozo(
                    nombre=nombre,
                    ubicacion=random.choice(ubicaciones),
                    latitud=round(random.uniform(18.0, 27.0), 6),
                    longitud=round(random.uniform(-105.0, -92.0), 6),
                    produccion_diaria=round(random.uniform(100.0, 5000.0), 2),
                    produccion_gas=round(random.uniform(50.0, 3000.0), 2),
                    produccion_agua=round(random.uniform(20.0, 400.0), 2),
                    estado=random.choice(estados),
                    profundidad=round(random.uniform(1000.0, 6000.0), 2),
                    fecha_inicio=datetime.now() - timedelta(days=random.randint(30, 3650)),
                    operador=random.choice(operadores),
                    campo=random.choice(campos),
                    notas=f"Pozo generado automáticamente para pruebas."
                )

                db.session.add(nuevo_pozo)
                pozos_generados += 1
                print(f"✅ Generado: {nombre}")

            except Exception as e:
                print(f"❌ Error: {str(e)}")

        try:
            db.session.commit()
            print(f"\n🎉 ¡Generación completada!")
            print(f"📊 Pozos generados: {pozos_generados}")
            print(f"📊 Total en base de datos: {Pozo.query.count()}")
        except Exception as e:
            db.session.rollback()
            print(f"\n❌ Error al guardar: {str(e)}")


if __name__ == '__main__':
    print("=" * 60)
    print("Sistema de Gestión de Pozos Petroleros")
    print("Generador de Datos de Ejemplo")
    print("=" * 60)
    print("\nOpciones:")
    print("1. Agregar 8 pozos de ejemplo con datos realistas")
    print("2. Generar pozos aleatorios (cantidad personalizada)")
    print("3. Salir")
    print()

    opcion = input("Seleccione una opción (1-3): ")

    if opcion == '1':
        print("\n📦 Agregando pozos de ejemplo...\n")
        agregar_datos_ejemplo()
    elif opcion == '2':
        try:
            cantidad = int(input("\n¿Cuántos pozos aleatorios desea generar?: "))
            if cantidad > 0 and cantidad <= 100:
                print(f"\n🎲 Generando {cantidad} pozos aleatorios...\n")
                generar_datos_aleatorios(cantidad)
            else:
                print("❌ Por favor ingrese un número entre 1 y 100")
        except ValueError:
            print("❌ Por favor ingrese un número válido")
    elif opcion == '3':
        print("\n👋 ¡Hasta luego!")
    else:
        print("\n❌ Opción no válida")

    print("\n" + "=" * 60)

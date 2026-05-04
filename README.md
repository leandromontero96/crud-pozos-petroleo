# Sistema CRUD - Gestión de Pozos Petroleros

Sistema web completo para la gestión de pozos petroleros con operaciones CRUD (Crear, Leer, Actualizar, Eliminar). Desarrollado con Flask, SQLAlchemy y SQLite.

## Características

- **Gestión completa de pozos petroleros**: Create, Read, Update, Delete (CRUD)
- **Interfaz web moderna**: Diseño responsive con Bootstrap 5
- **Dashboard con estadísticas**: Resumen de producción y estado de pozos
- **Base de datos SQLite**: Sin necesidad de instalación de servidor de base de datos
- **API REST opcional**: Endpoints JSON para integración con otras aplicaciones
- **Validación de datos**: Formularios con validación del lado del servidor

## Datos Gestionados

Cada pozo incluye la siguiente información:
- Nombre del pozo
- Ubicación y coordenadas (latitud/longitud)
- Campo petrolero y operador
- Producción diaria de petróleo (barriles/día)
- Producción de gas (Mscf/día)
- Producción de agua (barriles/día)
- Estado (Activo/Inactivo/Mantenimiento)
- Profundidad del pozo
- Fecha de inicio de operaciones
- Notas y observaciones

## Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

## Instalación

### 1. Clonar o descargar el proyecto

```bash
cd crud-petroleo
```

### 2. Crear un entorno virtual (recomendado)

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

## Uso

### 1. Iniciar la aplicación

```bash
python app.py
```

La aplicación estará disponible en: `http://localhost:5000`

### 2. Acceder a la interfaz web

Abre tu navegador y visita:
```
http://localhost:5000
```

### 3. Operaciones disponibles

#### Página Principal
- Ver lista completa de pozos
- Estadísticas en tiempo real (total pozos, activos, inactivos, producción total)
- Acciones rápidas: Ver, Editar, Eliminar

#### Crear Nuevo Pozo
- Formulario completo para registrar un nuevo pozo
- Validación de campos obligatorios
- Campos opcionales para información adicional

#### Ver Detalles
- Información completa del pozo
- Datos de producción organizados
- Historial de cambios

#### Editar Pozo
- Modificar cualquier campo del pozo
- Validación de datos
- Actualización de timestamp automática

#### Eliminar Pozo
- Confirmación antes de eliminar
- Eliminación permanente de la base de datos

## API REST (Opcional)

El sistema incluye endpoints REST para integración con otras aplicaciones:

### Listar todos los pozos
```bash
GET http://localhost:5000/api/pozos
```

### Obtener un pozo específico
```bash
GET http://localhost:5000/api/pozo/1
```

Respuesta en formato JSON con toda la información del pozo.

## Estructura del Proyecto

```
crud-petroleo/
│
├── app.py                  # Aplicación Flask principal
├── models.py               # Modelos de base de datos (SQLAlchemy)
├── requirements.txt        # Dependencias del proyecto
├── README.md              # Este archivo
│
├── templates/             # Plantillas HTML
│   ├── base.html         # Plantilla base
│   ├── index.html        # Página principal (lista de pozos)
│   ├── crear.html        # Formulario de creación
│   ├── editar.html       # Formulario de edición
│   ├── ver.html          # Vista de detalles
│   └── 404.html          # Página de error
│
├── static/               # Archivos estáticos
│   └── css/
│       └── style.css     # Estilos personalizados
│
└── pozos_petroleo.db     # Base de datos SQLite (se crea automáticamente)
```

## Tecnologías Utilizadas

- **Backend**: Flask 3.0.0
- **ORM**: SQLAlchemy 2.0.23
- **Base de datos**: SQLite
- **Frontend**: HTML5, CSS3, JavaScript
- **Framework CSS**: Bootstrap 5.3.0
- **Iconos**: Bootstrap Icons 1.10.0

## Configuración Avanzada

### Cambiar el puerto

Edita el archivo `app.py` (última línea):
```python
app.run(debug=True, host='0.0.0.0', port=8080)  # Cambiar 5000 a 8080
```

### Cambiar la clave secreta

Para producción, cambia la clave secreta en `app.py`:
```python
app.config['SECRET_KEY'] = 'tu_clave_secreta_segura_aqui'
```

### Usar otra base de datos

Para usar PostgreSQL o MySQL, actualiza la URI en `app.py`:
```python
# PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://usuario:password@localhost/pozos_db'

# MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://usuario:password@localhost/pozos_db'
```

## Capturas de Pantalla

### Dashboard Principal
Vista general con estadísticas y lista de pozos

### Formulario de Creación
Interfaz intuitiva para agregar nuevos pozos

### Vista de Detalles
Información completa organizada en cards

## Solución de Problemas

### Error: No module named 'flask'
```bash
pip install -r requirements.txt
```

### Error: Unable to open database file
Asegúrate de tener permisos de escritura en el directorio del proyecto.

### Error: Address already in use
Otro proceso está usando el puerto 5000. Cambia el puerto o detén el otro proceso.

## Mejoras Futuras

- [ ] Autenticación de usuarios
- [ ] Exportación de datos (Excel, CSV, PDF)
- [ ] Gráficos de producción histórica
- [ ] Mapa interactivo con ubicación de pozos
- [ ] Sistema de notificaciones
- [ ] Backup automático de base de datos
- [ ] Panel de administración avanzado
- [ ] Integración con APIs externas

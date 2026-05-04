from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Pozo(db.Model):
    """Modelo para representar un pozo petrolero"""
    __tablename__ = 'pozos'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False, unique=True)
    ubicacion = db.Column(db.String(200), nullable=False)
    latitud = db.Column(db.Float)
    longitud = db.Column(db.Float)
    produccion_diaria = db.Column(db.Float, nullable=False)  # Barriles por día
    produccion_gas = db.Column(db.Float, default=0.0)  # Miles de pies cúbicos por día
    produccion_agua = db.Column(db.Float, default=0.0)  # Barriles por día
    estado = db.Column(db.String(50), nullable=False, default='Activo')  # Activo, Inactivo, Mantenimiento
    profundidad = db.Column(db.Float)  # Metros
    fecha_inicio = db.Column(db.Date, nullable=False)
    operador = db.Column(db.String(100))
    campo = db.Column(db.String(100))
    notas = db.Column(db.Text)
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)
    fecha_actualizacion = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f'<Pozo {self.nombre}>'

    def to_dict(self):
        """Convierte el objeto a diccionario para API REST"""
        return {
            'id': self.id,
            'nombre': self.nombre,
            'ubicacion': self.ubicacion,
            'latitud': self.latitud,
            'longitud': self.longitud,
            'produccion_diaria': self.produccion_diaria,
            'produccion_gas': self.produccion_gas,
            'produccion_agua': self.produccion_agua,
            'estado': self.estado,
            'profundidad': self.profundidad,
            'fecha_inicio': self.fecha_inicio.isoformat() if self.fecha_inicio else None,
            'operador': self.operador,
            'campo': self.campo,
            'notas': self.notas,
            'fecha_creacion': self.fecha_creacion.isoformat() if self.fecha_creacion else None,
            'fecha_actualizacion': self.fecha_actualizacion.isoformat() if self.fecha_actualizacion else None
        }

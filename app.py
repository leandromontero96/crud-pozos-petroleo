from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from models import db, Pozo
from datetime import datetime
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'tu_clave_secreta_aqui_cambiar_en_produccion'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pozos_petroleo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Crear tablas si no existen
with app.app_context():
    db.create_all()


@app.route('/')
def index():
    """Página principal - Lista todos los pozos"""
    pozos = Pozo.query.order_by(Pozo.fecha_actualizacion.desc()).all()

    # Calcular estadísticas
    total_pozos = len(pozos)
    pozos_activos = len([p for p in pozos if p.estado == 'Activo'])
    produccion_total = sum([p.produccion_diaria for p in pozos if p.estado == 'Activo'])

    stats = {
        'total_pozos': total_pozos,
        'pozos_activos': pozos_activos,
        'pozos_inactivos': total_pozos - pozos_activos,
        'produccion_total': round(produccion_total, 2)
    }

    return render_template('index.html', pozos=pozos, stats=stats)


@app.route('/pozo/<int:id>')
def ver_pozo(id):
    """Ver detalles de un pozo específico"""
    pozo = Pozo.query.get_or_404(id)
    return render_template('ver.html', pozo=pozo)


@app.route('/crear', methods=['GET', 'POST'])
def crear_pozo():
    """Crear un nuevo pozo"""
    if request.method == 'POST':
        try:
            # Validar fecha
            fecha_inicio_str = request.form.get('fecha_inicio')
            fecha_inicio = datetime.strptime(fecha_inicio_str, '%Y-%m-%d').date()

            nuevo_pozo = Pozo(
                nombre=request.form.get('nombre'),
                ubicacion=request.form.get('ubicacion'),
                latitud=float(request.form.get('latitud')) if request.form.get('latitud') else None,
                longitud=float(request.form.get('longitud')) if request.form.get('longitud') else None,
                produccion_diaria=float(request.form.get('produccion_diaria')),
                produccion_gas=float(request.form.get('produccion_gas', 0)),
                produccion_agua=float(request.form.get('produccion_agua', 0)),
                estado=request.form.get('estado'),
                profundidad=float(request.form.get('profundidad')) if request.form.get('profundidad') else None,
                fecha_inicio=fecha_inicio,
                operador=request.form.get('operador'),
                campo=request.form.get('campo'),
                notas=request.form.get('notas')
            )

            db.session.add(nuevo_pozo)
            db.session.commit()

            flash(f'Pozo "{nuevo_pozo.nombre}" creado exitosamente!', 'success')
            return redirect(url_for('index'))

        except Exception as e:
            db.session.rollback()
            flash(f'Error al crear el pozo: {str(e)}', 'error')
            return redirect(url_for('crear_pozo'))

    return render_template('crear.html')


@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_pozo(id):
    """Editar un pozo existente"""
    pozo = Pozo.query.get_or_404(id)

    if request.method == 'POST':
        try:
            # Validar fecha
            fecha_inicio_str = request.form.get('fecha_inicio')
            fecha_inicio = datetime.strptime(fecha_inicio_str, '%Y-%m-%d').date()

            pozo.nombre = request.form.get('nombre')
            pozo.ubicacion = request.form.get('ubicacion')
            pozo.latitud = float(request.form.get('latitud')) if request.form.get('latitud') else None
            pozo.longitud = float(request.form.get('longitud')) if request.form.get('longitud') else None
            pozo.produccion_diaria = float(request.form.get('produccion_diaria'))
            pozo.produccion_gas = float(request.form.get('produccion_gas', 0))
            pozo.produccion_agua = float(request.form.get('produccion_agua', 0))
            pozo.estado = request.form.get('estado')
            pozo.profundidad = float(request.form.get('profundidad')) if request.form.get('profundidad') else None
            pozo.fecha_inicio = fecha_inicio
            pozo.operador = request.form.get('operador')
            pozo.campo = request.form.get('campo')
            pozo.notas = request.form.get('notas')
            pozo.fecha_actualizacion = datetime.utcnow()

            db.session.commit()

            flash(f'Pozo "{pozo.nombre}" actualizado exitosamente!', 'success')
            return redirect(url_for('ver_pozo', id=pozo.id))

        except Exception as e:
            db.session.rollback()
            flash(f'Error al actualizar el pozo: {str(e)}', 'error')

    return render_template('editar.html', pozo=pozo)


@app.route('/eliminar/<int:id>', methods=['POST'])
def eliminar_pozo(id):
    """Eliminar un pozo"""
    pozo = Pozo.query.get_or_404(id)

    try:
        nombre = pozo.nombre
        db.session.delete(pozo)
        db.session.commit()
        flash(f'Pozo "{nombre}" eliminado exitosamente!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error al eliminar el pozo: {str(e)}', 'error')

    return redirect(url_for('index'))


# API REST endpoints (opcional)
@app.route('/api/pozos', methods=['GET'])
def api_listar_pozos():
    """API: Listar todos los pozos en formato JSON"""
    pozos = Pozo.query.all()
    return jsonify([pozo.to_dict() for pozo in pozos])


@app.route('/api/pozo/<int:id>', methods=['GET'])
def api_obtener_pozo(id):
    """API: Obtener un pozo específico en formato JSON"""
    pozo = Pozo.query.get_or_404(id)
    return jsonify(pozo.to_dict())


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

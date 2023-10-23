from utils import db

class Movilidad(db.Model):
    __tablename__ = 'tbl_movilidad'
    
    movil_id = db.Column(db.Integer, primary_key=True)
    movil_tipo_servicio = db.Column(db.String(100), nullable=False)
    movil_turno = db.Column(db.String(100), nullable=False, unique=True)
    movil_sesion = db.Column(db.String(100), nullable=False)
    movil_docente = db.Column(db.String(150), nullable=False)
    movil_pago = db.Column(db.String(100), nullable=False)

# Agregar una clave foránea para relacionar con la tabla Alumno
    alumno_id = db.Column(db.Integer, db.ForeignKey('tbl_alumno.alumno_id'), nullable=False)
    colegio_id = db.Column(db.Integer, db.ForeignKey('tbl_colegio.colegio_id'), nullable=False)
    vehiculo_id = db.Column(db.Integer, db.ForeignKey('tbl_vehiculo.vehiculo_id'), nullable=False)
# Crear una relación con la tabla Alumno
    alumno = db.relationship('Alumno', backref=db.backref('movilidades', lazy=True))
    colegio = db.relationship('Colegio', backref=db.backref('movilidades', lazy=True))
    vehiculo = db.relationship('Vehiculo', backref=db.backref('movilidades', lazy=True))
    
    @staticmethod
    def get_all():
        return Movilidad.query.all()
    
    @staticmethod
    def get_by_id(id):
        return Movilidad.query.get(id)
    
    @staticmethod
    def get_by_turno(turno):
        return Movilidad.query.filter_by(movil_turno = turno).first()
    
    def save(self):
        if not self.movil_id:
            db.session.add(self)
        db.session.commit()
        
    def delete(self):
        db.session.delete(self)
        db.session.commit()
from utils import db

class Alumno(db.Model):
    __tablename__ = 'tbl_alumno'
    
    alumno_id = db.Column(db.Integer,primary_key=True)
    alumno_nombre = db.Column(db.String(255),nullable=False)
    alumno_apellido = db.Column(db.String(255),nullable=False)
    alumno_fecha_nacimiento = db.Column(db.Date,nullable=False)
    alumno_foto = db.Column(db.String(255))
    
    @staticmethod
    def get_all():
        return Alumno.query.all()
    
    @staticmethod
    def get_by_id(id):
        return Alumno.query.get(id)
    
    @staticmethod
    def get_by_apellido(alumno_apellido):
        return Alumno.query.filter_by(alumno_apellido=alumno_apellido).first()
    
    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()
        
    def delete(self):
        db.session.delete(self)
        db.session.commit()
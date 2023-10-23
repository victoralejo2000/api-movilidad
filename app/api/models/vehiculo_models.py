from utils import db

class Vehiculo(db.Model):
    __tablename__ = 'tbl_vehiculo'
    
    vehiculo_id = db.Column(db.Integer,primary_key=True)
    vehiculo_nombre = db.Column(db.String(100),nullable=False)
    vehiculo_placa = db.Column(db.String(100),nullable=False,unique=True)
    vehiculo_conductor = db.Column(db.String(100),nullable=False)
    
    @staticmethod
    def get_all():
        return Vehiculo.query.all()
    
    @staticmethod
    def get_by_id(id):
        return Vehiculo.query.get(id)
    
    @staticmethod
    def get_by_placa(placa):
        return Vehiculo.query.filter_by(vehiculo_placa = placa).first()
    
    def save(self):
        if not self.vehiculo_id:
            db.session.add(self)
        db.session.commit()
        
    def delete(self):
        db.session.delete(self)
        db.session.commit()
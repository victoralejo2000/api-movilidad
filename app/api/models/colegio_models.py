from utils import db

class Colegio(db.Model):
    __tablename__ = 'tbl_colegio'
    
    colegio_id = db.Column(db.Integer,primary_key=True)
    colegio_nombre = db.Column(db.String(255),nullable=False)
    
    @staticmethod
    def get_all():
        return Colegio.query.all()
    
    @staticmethod
    def get_by_id(colegio_id):
        return Colegio.query.get(colegio_id)
    
    @staticmethod
    def get_by_nombre(colegio_nombre):
        return Colegio.query.filter_by(colegio_nombre = colegio_nombre).first()
    
    def save(self):
        if not self.colegio_id:
            db.session.add(self)
        db.session.commit()
        
    def delete(self):
        db.session.delete(self)
        db.session.commit()
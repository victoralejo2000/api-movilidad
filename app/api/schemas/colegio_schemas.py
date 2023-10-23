from utils import ma

class ColegioSchema(ma.Schema):
    class Meta:
         fields = ('colegio_id','colegio_nombre')
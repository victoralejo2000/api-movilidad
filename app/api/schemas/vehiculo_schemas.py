from utils import ma

class VehiculoSchema(ma.Schema):
    class Meta:
        fields = ('vehiculo_id','vehiculo_nombre','vehiculo_conductor')
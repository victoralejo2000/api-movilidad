from utils import ma

class MovilidadSchema(ma.Schema):
    class Meta:
         fields = ('movil_id','movil_tipo_servicio','movil_turno ',' movil_sesion',' movil_docente',' movil_pago')
from utils import ma

class AlumnoSchema(ma.Schema):
    class Meta:
        fields = ('alumno_id','alumno_nombre','alumno_apellido','alumno_fecha_nacimiento','alumno_foto')
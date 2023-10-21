from flask import request
from flask_restful import Resource,Api
from .. import api
from ..models.alumno_models import Alumno
from ..schemas.alumno_schemas import AlumnoSchema

# from werkzeug.security import (
#     generate_password_hash,
#     check_password_hash
# )

# from flask_jwt_extended import (
#     create_access_token,
#     jwt_required,
#     verify_jwt_in_request,
#     get_jwt_identity
# )

api_alumno = Api(api)

class AlumnoResource(Resource):
    
    def get(self):
        data = Alumno.get_all()
        schema = AlumnoSchema(many=True)
        
        context = {
            'status':True,
            'message':'Lista de Alumnos',
            'content':schema.dump(data)
        }
        return context
    
    def post(self):
        try:
            data = request.get_json()
            # password_hash = generate_password_hash(data['password'])
            
            alumno = Alumno()
            alumno.alumno_nombre = data['alumno_nombre']
            alumno.alumno_apellido = data['alumno_apellido']
            alumno.alumno_fecha_nacimiento = data['alumno_fecha_nacimiento']
            alumno.alumno_foto = data['alumno_foto']
            alumno.save()
            
            schema = AlumnoSchema()
            return {
                'status':True,
                'content':schema.dump(alumno)
            }
            
        except Exception as e:
            return {
                'status':False,
                'message':str(e)
            },500
        
class AlumnoDetailResource(Resource):

    def get(self,id):
        alumno = Alumno.get_by_id(id)
        schema = AlumnoSchema()
        context = {
            'status':True,
            'context':schema.dump(alumno)
        }

        return context
    
    def put(self,id):
        data = request.get_json()
        alumno_nombre = data['alumno_nombre']
        alumno_apellido = data['alumno_apellido']
        alumno_fecha_nacimiento = data['alumno_fecha_nacimiento']
        alumno_foto = data['alumno_foto']

        alumno = Alumno.get_by_id(id)
        alumno.alumno_nombre = alumno_nombre
        alumno.alumno_apellido = alumno_apellido
        alumno.alumno_fecha_nacimiento = alumno_fecha_nacimiento
        alumno.alumno_foto = alumno_foto
        alumno.save()

        schema = AlumnoSchema()

        return {
            'status':True,
            'content':schema.dump(alumno)
        }

    def delete(self,id):
        alumno = Alumno.get_by_id(id)
        alumno.delete()
        
        schema = AlumnoSchema()
        
        context = {
            'status':True,
            'content':schema.dump(alumno)
        }
        
        return context
            
# class AuthenticationResource(Resource):
    
#     def post(self):
#         data = request.get_json()
#         usuario = Usuario.get_by_email(data['email'])
#         if not usuario:
#             return {
#                 'status':False,
#                 'message':'no se encontro usuario'
#             }
        
#         is_password_checked = check_password_hash(usuario.password,data['password'])
#         if is_password_checked:
#             token = create_access_token(identity=usuario.id)
#             return {
#                 'status':True,
#                 'token':token
#             }
#         else:
#             return {
#                 'status':False,
#                 'message':'contraseña invalida'
#             }
        
#     @jwt_required()
#     def get(self):
#         verify_jwt_in_request()
#         usuario_id = get_jwt_identity()
#         usuario = Usuario.get_by_id(usuario_id)
#         schema = UsuarioSchema()
#         return {
#             'status':True,
#             'content':schema.dump(usuario)
#         }
    
api_alumno.add_resource(AlumnoResource,'/alumno')
api_alumno.add_resource(AlumnoDetailResource,'/alumno/<id>')
# api_usuario.add_resource(AuthenticationResource,'/auth')
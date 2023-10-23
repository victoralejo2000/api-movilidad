from flask import request
from flask_restful import Resource,Api
from .. import api
from ..models.movilidad_models import Movilidad
from ..schemas.movilidad_schemas import MovilidadSchema

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

api_movilidad = Api(api)

class MovilidadResource(Resource):
    
    def get(self):
        data = Movilidad.get_all()
        schema = MovilidadSchema(many=True)
        
        context = {
            'status':True,
            'message':'Lista de movils',
            'content':schema.dump(data)
        }
        return context
    
    def post(self):
        try:
            data = request.get_json()
            # password_hash = generate_password_hash(data['password'])
            
            movilidad = Movilidad()
            movilidad.movil_tipo_servicio = data['tipo_servicio']
            movilidad.movil_turno = data['turno']
            movilidad.movil_sesion = data['seccion']
            movilidad.movil_docente = data['docente']
            movilidad.movil_pago = data['pago']
            movilidad.save()
            
            schema = MovilidadSchema()
            return {
                'status':True,
                'content':schema.dump(movilidad)
            }
            
        except Exception as e:
            return {
                'status':False,
                'message':str(e)
            },500
        
class MovilidadDetailResource(Resource):

    def get(self,id):
        movilidad = Movilidad.get_by_id(id)
        schema = MovilidadSchema()
        context = {
            'status':True,
            'context':schema.dump(movilidad)
        }

        return context
    
    def put(self,id):
        data = request.get_json()
        movil_tipo_servicio = data['tipo_servicio']
        movil_turno = data['turno']
        movil_sesion = data['seccion']
        movil_docente = data['docente']
        movil_pago = data['pago']

        movilidad = Movilidad.get_by_id(id)
        movilidad. movil_tipo_servicio = tipo_servicio
        movilidad.movil_turno = turno
        movilidad.movil_sesion = seccion
        movilidad.movil_docente = docente
        movilidad.movil_pago = pago
        movilidad.save()

        schema = MovilidadSchema()

        return {
            'status':True,
            'content':schema.dump(movilidad)
        }

    def delete(self,id):
        movilidad = Movilidad.get_by_id(id)
        movilidad.delete()
        
        schema = MovilidadSchema()
        
        context = {
            'status':True,
            'content':schema.dump(movilidad)
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
    
api_movilidad.add_resource(MovilidadResource,'/movilidad')
api_movilidad.add_resource(MovilidadDetailResource,'/movilidad/<id>')
# api_usuario.add_resource(AuthenticationResource,'/auth')
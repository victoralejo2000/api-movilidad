from flask import request
from flask_restful import Resource,Api
from .. import api
from ..models.colegio_models import Colegio
from ..schemas.colegio_schemas import ColegioSchema

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

api_colegio = Api(api)

class ColegioResource(Resource):
    
    def get(self):
        data = Colegio.get_all()
        schema = ColegioSchema(many=True)
        
        context = {
            'status':True,
            'message':'Lista de Colegios',
            'content':schema.dump(data)
        }
        return context
    
    def post(self):
        try:
            data = request.get_json()
            # password_hash = generate_password_hash(data['password'])
            
            colegio = Colegio()
            colegio.colegio_nombre = data['colegio_nombre']
            colegio.save()
            
            schema = ColegioSchema()
            return {
                'status':True,
                'content':schema.dump(colegio)
            }
            
        except Exception as e:
            return {
                'status':False,
                'message':str(e)
            },500
        
class ColegioDetailResource(Resource):

    def get(self,id):
        colegio = Colegio.get_by_id(id)
        schema = ColegioSchema()
        context = {
            'status':True,
            'context':schema.dump(colegio)
        }

        return context
    
    def put(self,id):
        data = request.get_json()
        colegio_nombre = data['colegio_nombre']
    
        colegio = Colegio.get_by_id(id)
        colegio.colegio_nombre = colegio_nombre
        colegio.save()

        schema = ColegioSchema()

        return {
            'status':True,
            'content':schema.dump(colegio)
        }

    def delete(self,id):
        colegio = Colegio.get_by_id(id)
        colegio.delete()
        
        schema = ColegioSchema()
        
        context = {
            'status':True,
            'content':schema.dump(colegio)
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
    
api_colegio.add_resource(ColegioResource,'/colegio')
api_colegio.add_resource(ColegioDetailResource,'/colegio/<id>')
# api_usuario.add_resource(AuthenticationResource,'/auth')
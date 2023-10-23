from flask import request
from flask_restful import Resource,Api
from .. import api
from ..models.vehiculo_models import Vehiculo
from ..schemas.vehiculo_schemas import VehiculoSchema

api_vehiculo = Api(api)

class VehiculoResource(Resource):
    
    def get(self):
        data = Vehiculo.get_all()
        schema = VehiculoSchema(many=True)
        
        context = {
            'status':True,
            'message':'lista de vehiculos',
            'content':schema.dump(data)
        }
        return context
    
    def post(self):
        try:
            data = request.get_json()
            
            vehiculo = Vehiculo()
            vehiculo.nombre = data['nombre']
            vehiculo.placa = data['placa']
            vehiculo.conductor = data['conductor']
            vehiculo.save()
            
            schema = VehiculoSchema()
            return {
                'status':True,
                'content':schema.dump(vehiculo)
            }
            
        except Exception as e:
            return {
                'status':False,
                'message':str(e)
            },500
        
class VehiculoDetailResource(Resource):

    def get(self,id):
        vehiculo = Vehiculo.get_by_id(id)
        schema = VehiculoSchema()
        context = {
            'status':True,
            'context':schema.dump(vehiculo)
        }

        return context
    
    def put(self,id):
        data = request.get_json()
        vehiculo_nombre = data['nombre']
        vehiculo_placa = data['placa']
        vehiculo_conductor = data['conductor']

        vehiculo = Usuario.get_by_id(id)
        vehiculo.nombre = nombre
        vehiculo.placa = placa
        vehiculo.conductor = conductor
        vehiculo.save()

        schema = VehiculoSchema()

        return {
            'status':True,
            'content':schema.dump(vehiculo)
        }

    def delete(self,id):
        vehiculo = Vehiculo.get_by_id(id)
        vehiculo.delete()
        
        schema = VehiculoSchema()
        
        context = {
            'status':True,
            'content':schema.dump(vehiculo)
        }
        
        return context
            

api_vehiculo.add_resource(VehiculoResource,'/vehiculo')
api_vehiculo.add_resource(VehiculoDetailResource,'/vehiculo/<id>')
#api_usuario.add_resource(AuthenticationResource,'/auth')
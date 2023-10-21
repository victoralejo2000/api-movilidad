from flask import Blueprint,jsonify

api = Blueprint('api',__name__,url_prefix='/api')

from .resources import (
    usuario_resources,
    alumno_resources
)

# from .models.alumno_models import Alumno

@api.route('/')
def index():
    context ={
        'message':'blueprint api'
    }
    return jsonify(context)
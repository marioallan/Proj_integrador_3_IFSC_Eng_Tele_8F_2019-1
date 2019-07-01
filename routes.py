import json
import time
import os

from flask import Blueprint, request, render_template
from models import Costumer, db, Measurement, image_path
import pytesseract as ocr
from PIL import Image # A Python Imaging Library (PIL)
from werkzeug import secure_filename

routes = Blueprint('routes', __name__)


def _build_response(response, status):
    return json.dumps(response), status, {'ContentType':'application/json'}

#----------------------------------------------------------------------------------

@routes.route('/', methods=['GET'])
def index():
    #return 'Web-service Flask esta em execução'
    return render_template('index.html')
#----------------------------------------------------------------------------------
@routes.route('/c', methods=['GET'])
def c():
    #return 'Web-service Flask esta em execução'
    return render_template('cadastro.html',text=json)
#----------------------------------------------------------------------------------

@routes.route('/upload', methods=['GET'])
def upload():
    #return 'Web-service Flask esta em execução'
    return render_template('upload.html')
#----------------------------------------------------------------------------------

@routes.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   #if request.method == 'POST':
      f = request.files['file']
      f.save(image_path + secure_filename(f.filename))
      return 'file uploaded successfully'

#----------------------------------------------------------------------------------

@routes.route('/limit', methods=['POST'])
def limit_route():
    try:
        data = request.get_json()
        unit = data.get('consumer_unity')
        limit = data.get('limit')
        if unit is None or limit is None:
            return _build_response({'error': 'Invalid body'}, 400)

        costumer = Costumer.query.filter_by(consumer_unit=unit).first()

        if costumer is None:
            new_costumer = Costumer(unit, limit)
            db.session.add(new_costumer)
            db.session.commit()
        else:
            costumer.consumption_limit = limit
            db.session.commit()

        return _build_response({'success': True}, 200)
    except Exception as error:
        return _build_response({'error': str(error)}, 500)
#----------------------------------------------------------------------------------

@routes.route('/image_update', methods=['POST'])
def image_update():
    try:
        unit = request.args.get('consumer_unit')
        print(unit)
        image = request.files['file']

        if unit is None or image is None:
            return _build_response({'error': 'No unit was specified'}, 400)

        costumer = Costumer.query.filter_by(consumer_unit=unit).first()

        if costumer is None:
            return _build_response({'error': 'Costumer not found'}, 404)

        timestamp = str(time.time())
        path = image_path + unit + '_' + timestamp + '_' +secure_filename(image.filename)
        image.save(path)

        img =Image.open(image) # ABRE A IMG REFERIDA
        # TODO: Function to get the measurement value from the image
        value = ocr.image_to_string(img, lang='eng', config='--psm 10') # CONVERTE A IMG PARA STRING COM OS PARAMETROS DE LINGUA INGLESA E PSM 10
        print(value)

        new_measurement = Measurement(value, path, costumer.id)
        db.session.add(new_measurement)
        db.session.commit()

        return _build_response({'success': True}, 200)
    except Exception as error:
        return _build_response({'error': str(error)}, 500)
#----------------------------------------------------------------------------------

@routes.route('/check', methods=['GET'])
def check():
    try:
        unit = request.args.get('consumer_unit')
        if unit is None:
            return _build_response({'error': 'No unit was specified'}, 400)

        costumer = Costumer.query.filter_by(consumer_unit=unit).first()
        if costumer is None:
            return _build_response({'error': 'Costumer not found'}, 404)

        last_measurement = Measurement.query \
            .filter_by(costumer_id=costumer.id) \
            .order_by(Measurement.created_at.desc()) \
            .first()

        response = {'continue': True} if last_measurement.value <= costumer.consumption_limit \
             else {'continue': False}

        return _build_response(response, 200)
    except Exception as error:
        return _build_response({'error': str(error)}, 500)

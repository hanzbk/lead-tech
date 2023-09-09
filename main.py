from flask import Flask, request, jsonify
import csv
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///proyecto.db'
db = SQLAlchemy(app)
api = Api(app)
cors = CORS(app)

class Proyecto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    show_id = db.Column(db.String(500), nullable=True)
    type = db.Column(db.String(500), nullable=True)
    title = db.Column(db.String(500), nullable=True)
    director = db.Column(db.String(500), nullable=True)
    cast = db.Column(db.String(500), nullable=True)
    country = db.Column(db.String(500), nullable=True)
    date_added = db.Column(db.String(500), nullable=True)
    release_year = db.Column(db.String(500), nullable=True)
    rating = db.Column(db.String(500), nullable=True)
    duration = db.Column(db.String(500), nullable=True)
    listed_in = db.Column(db.String(500), nullable=True)
    description = db.Column(db.String(5000), nullable=True)


    def serialize(self):

        return {
            'id': self.id,
            'show_id': self.show_id,
            'type': self.type,
            'title': self.title,
            'director': self.director,
            'cast': self.cast,
            'country': self.country,
            'date_added': self.date_added,
            'release_year': self.release_year,
            'rating': self.rating,
            'duration': self.duration,
            'listed_in': self.listed_in,
            'description': self.description,
        }

#Migrar datos a la base
with app.app_context():
    db.create_all()

class DataResource(Resource):
    def post(self):
        # Procesar y guardar los datos del CSV
        # Puedes utilizar la librería pandas para facilitar esta tarea
        print('POST')
        print('a recorrer')

        # Asegúrate de que se haya enviado un archivo CSV
        if 'csv_file' not in request.files:
            #return jsonify({'error': 'No se ha proporcionado un archivo CSV'}), 400
            return {'error': 'No se ha proporcionado un archivo CSV'}
        print('con archivo')
        csv_file = request.files['csv_file']

        # Lee los datos del CSV
        data = []
        reader = csv.DictReader(csv_file.read().decode('utf-8').splitlines())
        try:
            for row in reader:
                data.append({
                    'show_id': row['show_id'],
                    'type': row['type'],
                    'title': row['title'],
                    'director': row['director'],
                    'cast': row['cast'],
                    'country': row['country'],
                    'date_added': row['date_added'],
                    'release_year': row['release_year'],
                    'rating': row['rating'],
                    'duration': row['duration'],
                    'listed_in': row['listed_in'],
                    'description': row['description']
                })

            # Lista para rastrear elementos duplicados
            elementos_duplicados = []
            print('validar duplicados')

            # Insertar los datos en la base de datos y verificar duplicados
            with app.app_context():
                for item in data:
                    # Verificar si el elemento ya existe en la base de datos
                    existente = Proyecto.query.filter_by(show_id=item['show_id']).first()
                    if existente:
                        elementos_duplicados.append(existente.serialize())  # Agregar a la lista de duplicados
                    else:
                        # Si no es duplicado, insertarlo en la base de datos
                        proyecto = Proyecto(
                            show_id=item['show_id'],
                            type=item['type'],
                            title=item['title'],
                            director=item['director'],
                            cast=item['cast'],
                            country=item['country'],
                            date_added=item['date_added'],
                            release_year=item['release_year'],
                            rating=item['rating'],
                            duration=item['duration'],
                            listed_in=item['listed_in'],
                            description=item['description']
                        )
                        db.session.add(proyecto)
                db.session.commit()

            # Respuesta JSON con datos duplicados (si los hay)
            print('elementos_duplicados',elementos_duplicados)
            if elementos_duplicados:

                return {'message': 'Datos insertados en la base de datos con elementos duplicados',
                                'duplicados': elementos_duplicados}
            
            else:
                return {'message': 'Datos guardados correctamente'}
        except Exception as e:
            return {'message': 'Error en el servidor, consulte al administrador del sistema'}

      
            
        

    

    def get(self):
        # Consultar y retornar datos
        # Aquí debes escribir la lógica para consultar datos de la base de datos
        datos = Proyecto.query.all()[:100]
        
        print('GET')

        result = [dato.serialize() for dato in datos][:]
        print('result',result)
        return result

api.add_resource(DataResource, '/data')

if __name__ == '__main__':
    app.run()

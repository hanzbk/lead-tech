from flask import Flask, request, jsonify
import csv

app = Flask(__name__)

# Ruta para cargar el archivo CSV
@app.route('/upload-csv', methods=['POST'])
def upload_csv():
    try:
        # Asegúrate de que se haya enviado un archivo CSV
        if 'csvFile' not in request.files:
            return jsonify({'error': 'No se proporcionó un archivo CSV'}), 400
        
        csv_file = request.files['csvFile']
        
        # Lee el archivo CSV y almacena los datos en una lista de diccionarios
        data = []
        reader = csv.DictReader(csv_file)
        for row in reader:
            data.append(row)
        
        # Aquí puedes realizar cualquier procesamiento adicional con los datos
        
        return jsonify({'message': 'Archivo CSV cargado exitosamente', 'data': data}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

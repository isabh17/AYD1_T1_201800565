from flask import Flask, request, jsonify

app = Flask(__name__)

# Lista de canciones
canciones = []

# Endpoint POST: Agregar Canción
@app.route('/agregarCancion', methods=['POST'])
def agregar_cancion():
    data = request.get_json()
    nombre = data.get('nombre')
    artista = data.get('artista')
    album = data.get('album')  # Cambiar a 'genero' en el hotfix

    cancion = {
        'nombre': nombre,
        'artista': artista,
        'album': album
    }
    canciones.append(cancion)
    return jsonify(cancion), 201

# Endpoint GET: Ver Información
@app.route('/verInformacion', methods=['GET'])
def ver_informacion():
    return jsonify({
        'nombre': 'Tu Nombre',
        'carnet': '201800565'
    })

if __name__ == '__main__':
    app.run(debug=True)


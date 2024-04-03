# from flask import Flask, request, jsonify
# import redis

# app = Flask(__name__)
# redis_client = redis.Redis(host='localhost', port=6379, db=0)

# # Ruta para manejar las solicitudes de suma
# @app.route('/sumar', methods=['POST'])
# def sumar():
#     try:
#         data = request.json
#         num1 = float(data['numero1'])
#         num2 = float(data['numero2'])
#         resultado = num1 + num2

#         # Guardar el resultado en Redis
#         redis_client.set('resultado', resultado)

#         return jsonify({'resultado': resultado}), 200
#     except Exception as e:
#         return jsonify({'error': 'Error al sumar los números.'}), 500

# # Ruta para obtener el resultado almacenado en Redis
# @app.route('/resultado', methods=['GET'])
# def obtener_resultado():
#     try:
#         resultado = float(redis_client.get('resultado'))
#         return jsonify({'resultado': resultado}), 200
#     except Exception as e:
#         return jsonify({'error': 'Error al obtener el resultado.'}), 500

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, request, jsonify

app = Flask(__name__)

# Ruta raíz para servir el archivo HTML
@app.route('/')
def index():
    return app.send_static_file('index.html')

# Resto del código para la calculadora de suma y la integración con Redis
import redis
redis_client = redis.Redis(host='localhost', port=6379, db=0)

@app.route('/sumar', methods=['POST'])
def sumar():
    try:
        data = request.json
        num1 = float(data['numero1'])
        num2 = float(data['numero2'])
        resultado = num1 + num2

        redis_client.set('resultado', resultado)

        return jsonify({'resultado': resultado}), 200
    except Exception as e:
        return jsonify({'error': 'Error al sumar los números.'}), 500

@app.route('/resultado', methods=['GET'])
def obtener_resultado():
    try:
        resultado = float(redis_client.get('resultado'))
        return jsonify({'resultado': resultado}), 200
    except Exception as e:
        return jsonify({'error': 'Error al obtener el resultado.'}), 500

if __name__ == '__main__':
    app.run(debug=True)

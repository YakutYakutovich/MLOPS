from flask import Flask, request, jsonify
import numpy as np
import pickle  # Для загрузки модели

app = Flask(__name__)

# Загрузка модели (пример)
# model = pickle.load(open('model.pkl', 'rb'))

@app.route('/invocations', methods=['POST'])
def predict():
    try:
        data = request.json
        inputs = np.array(data['inputs'])
        
        # Пример предсказания (замените на вашу модель)
        prediction = 42  # model.predict(inputs)
        
        return jsonify({
            "prediction": float(prediction),
            "status": "success"
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)

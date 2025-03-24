from flask import Flask, request, jsonify
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['GET'])
def emotionDetector():
    # Obtener el texto enviado en los parámetros de la URL
    text_to_analyse = request.args.get('textToAnalyze', '')

    # Verificar si el texto no está vacío
    if not text_to_analyse:
        return jsonify({"error": "No text provided"}), 400

    # Llamar a la función emotion_detector para procesar el texto
    emotions = emotion_detector(text_to_analyse)

    # Formatear la salida para que coincida con la especificación
    output = (
        f"For the given statement, the system response is "
        f"'anger': {emotions['anger:']}, 'disgust': {emotions['disgust']}, "
        f"'fear': {emotions['fear']}, 'joy': {emotions['joy']}, "
        f"and 'sadness': {emotions['sadness']}. The dominant emotion is {emotions['dominant_emotion']}."
    )

    # Devolver la respuesta formateada
    return jsonify({"response": output})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

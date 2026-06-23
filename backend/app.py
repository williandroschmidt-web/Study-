from flask import Flask, request, jsonify
from flask_cors import CORS
from ia_estudos import gerar_resposta

app = Flask(__name__)
CORS(app)

@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({"status": "ok", "app": "Study+"})

@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json()

    pergunta = data.get("pergunta", "")
    materia = data.get("materia", "Geral")
    modo = data.get("modo", "explicar_resposta")

    resposta = gerar_resposta(materia, modo, pergunta)

    return jsonify({
        "ok": True,
        "resposta": resposta
    })

if __name__ == "__main__":
    app.run(debug=True, port=5000)

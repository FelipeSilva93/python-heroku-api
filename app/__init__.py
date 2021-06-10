from flask import Flask, request, jsonify


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def não_entre_em_panico():
        if request.headers.get('authorization') == 42:
            return jsonify({
                "42": 'a resposta para a vida, o universo e tudo mais'
            })
        else:
            return jsonify({
                "mensagem": 'não entre em panico'
            })

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

    @app.route('/about')
    def about():
        return 'About Us'

    @app.route('/add')
    def add():
        return 'Hello from add page'

    return app

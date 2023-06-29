from flask import Flask, request, send_file, jsonify
import os

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get('name', 'World')
    return 'Hello! you requested ' + ' with name ' + name

@app.route("/logo.png", methods=['GET'])
def plugin_logo():
    filename = 'logo.png'
    return send_file(filename, mimetype='image/png')

@app.route("/.well-known/ai-plugin.json", methods=['GET'])
def plugin_manifest():
    with open("./.well-known/ai-plugin.json") as f:
        text = f.read()
        return jsonify(text)

@app.route("/openapi.yaml", methods=['GET'])
def openapi_spec():
    with open("openapi.yaml") as f:
        text = f.read()
        return jsonify(text)

if __name__ == "__main__":
    port = int(os.getenv('PORT', 80))
    print(f'Listening on port {port}')
    app.run(host='0.0.0.0', port=port)

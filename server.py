from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get('name', 'World')
    return 'Hello! you requested ' + ' with name ' + name

if __name__ == "__main__":
    port = int(os.getenv('PORT', 80))
    print('Listening on port %s' % (port))
    app.run(host='0.0.0.0', port=port)

from flask import flask

app = Flask(__name__)

@app.route('/')
def_index():
    return 'Hello Index Page'

if __name__ == '__main__':
    app.run()
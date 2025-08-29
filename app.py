from flask import Flask, jsonify, send_from_directory

app = Flask(__name__, static_url_path='', static_folder='.')

@app.route('/')
def root():
    return send_from_directory('.', 'index.html')

@app.route('/tips')
def tips():
    return jsonify(tips=['connect with peers','practice mindfulness','seek support'])

if __name__ == '__main__':
    app.run()

#!flask/bin/python
from flask import Flask, jsonify

app = Flask(__name__)

games = [
    {
        'id': 1,
        'title': u'Warcraft3',
        'description': u'Loctar ogar! Zag zag!',
        'done': False
    },
    {
        'id': 2,
        'title': u'Battlefield2',
        'description': u'piu piu piu wargame',
        'done': False
    }
]

@app.route('/api/v1/games', methods=['GET'])
def get_games():
    return jsonify({'games': games})

if __name__ == '__main__':
    app.run(debug=True)
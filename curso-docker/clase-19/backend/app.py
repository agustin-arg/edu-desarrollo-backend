from flask import Flask,jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/getMyInfo')
def getMyInfo():
    value = {
        "name": "Agustín",
        "lastname": "Leiva",
        "socialMedia":
        {
            "facebookUser": "AgustinLeiva",
            "instagramUser": "AgustinLeiva",
            "xUser": "AgustinLeiva",
            "linkedin": "AgustinLeiva",
            "githubUser": "AgustinLeiva"
        },
        "blog": "https://AgustinLeiva.com",
        "author": "Agusti nLeiva
    }

    return jsonify(value)

if __name__ == '__main__':
    app.run(port=5000)
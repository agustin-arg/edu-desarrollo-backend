from flask import Flask, request, jsonify

app= Flask(__name__)

@app.route("/")
def hello():
    return "Hello word"

@app.route("/about")
def about():
    return "This app is the note"

@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        return "Form send correctly", 201
    return "Page to contact"

@app.route('/api/info')
def api_info():
    data = {
        "nombre": "Note app",
        "version": "1.1.1"
    }
    return jsonify(data), 200
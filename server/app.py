from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    make = requests.get('http://make_api:5000/get_make')
    model = requests.get('http://model_api:5000/get_model')
    mot = requests.post('http://mot_api:5000/get_mot', data=make.text, data=model.text)
    return render_template ('index.html', make=make.text, model=model.text, mot=mot.text)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
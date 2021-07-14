from flask import Flask, render_template
from application.models import Vehicles 
from sqlalchemy import desc
from application import app, db
import requests

app = Flask(__name__)

@app.route('/')
def index():
    make = requests.get('http://make_api:5000/get_make')
    model = requests.get('http://model_api:5000/get_model')
    mot = requests.post('http://mot_api:5000/get_mot', json={'make':make.text, 'model':model.text})
    vehicle = Vehicles(make = make.text, model = model.text, mot = mot.text)

    db.session.add(vehicle)
    db.session.commit()
    vehicles = Vehicles.query.order_by(Vehicles.id.desc()).limit(5)
    
    return render_template ('index.html', make=make.text, model=model.text, vehicles=vehicles, mot=mot.text)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
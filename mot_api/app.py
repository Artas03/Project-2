from flask import Flask, request, Response, jsonify
import random 

app = Flask(__name__)

@app.route('/get_mot', methods=['GET','POST'])
def get_mot():
    make = request.data.decode('utf-8')
    vowels = ["a","e", "i", "o", "u"]
    make = make.lower()

    newCar = []
    for i in make:
        if i in vowels:
            newCar.append(i)
    merged = "".join(newCar)
    return jsonify(answer=merged)

if __name__ == "__main__":
    app.run(port=5000, debug=True)
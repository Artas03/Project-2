from flask import Flask, request, Response
import random 

app = Flask(__name__)

@app.route('/get_make', methods=['GET'])
def get_make():
    make = random.choice(['BMW','Mercedes','Vauxhall','Honda','Audi','Volkswagen'])
    return Response(make)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
from flask import Flask, request, Response
import random 

app = Flask(__name__)

@app.route('/get_model', methods=['GET'])
def get_model():
    model = random.choice(['4 series','C63s','GTC','Civic','RS7','Scirocco'])
    return Response(model)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
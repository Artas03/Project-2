from flask import Flask, request, Response 

app = Flask(__name__)

@app.route('/get_mot', methods=['GET','POST'])
def get_mot():
    item = request.get_json()

    if item['make'] == 'BMW' and item['model'] == '4 series':
        mot = '3'
    elif item['make'] == 'BMW' and item['model'] == 'C63s':
        mot = '0'
    elif item['make'] == 'BMW' and item['model'] == 'GTC':
        mot = '0'
    elif item['make'] == 'BMW' and item['model'] == 'Civic':
        mot = '2'
    elif item['make'] == 'BMW' and item['model'] == 'RS7':
        mot = '0'
    elif item['make'] == 'BMW' and item['model'] == 'Scirocco':
        mot = '3'
    elif item['make'] == 'Mercedes' and item['model'] == '4 series':
        mot = '6'
    elif item['make'] == 'Mercedes' and item['model'] == 'C63s':
        mot = '3'
    elif item['make'] == 'Mercedes' and item['model'] == 'GTC':
        mot = '3'
    elif item['make'] == 'Mercedes' and item['model'] == 'Civic':
        mot = '5'
    elif item['make'] == 'Mercedes' and item['model'] == 'RS7':
        mot = '3'
    elif item['make'] == 'Mercedes' and item['model'] == 'Scirocco':
        mot = '6'
    elif item['make'] == 'Vauxhall' and item['model'] == '4 series':
        mot = '6'
    elif item['make'] == 'Vauxhall' and item['model'] == 'C63s':
        mot = '3'
    elif item['make'] == 'Vauxhall' and item['model'] == 'GTC':
        mot = '3'
    elif item['make'] == 'Vauxhall' and item['model'] == 'Civic':
        mot = '5'
    elif item['make'] == 'Vauxhall' and item['model'] == 'RS7':
        mot = '3'
    elif item['make'] == 'Vauxhall' and item['model'] == 'Scirocco':
        mot = '6'
    elif item['make'] == 'Honda' and item['model'] == '4 series':
        mot = '5'
    elif item['make'] == 'Honda' and item['model'] == 'C63s':
        mot = '2'
    elif item['make'] == 'Honda' and item['model'] == 'GTC':
        mot = '2'
    elif item['make'] == 'Honda' and item['model'] == 'Civic':
        mot = '4'
    elif item['make'] == 'Honda' and item['model'] == 'RS7':
        mot = '2'
    elif item['make'] == 'Honda' and item['model'] == 'Scirocco':
        mot = '5'
    elif item['make'] == 'Audi' and item['model'] == '4 series':
        mot = '5'
    elif item['make'] == 'Audi' and item['model'] == 'C63s':
        mot = '2'
    elif item['make'] == 'Audi' and item['model'] == 'GTC':
        mot = '2'
    elif item['make'] == 'Audi' and item['model'] == 'Civic':
        mot = '4'
    elif item['make'] == 'Audi' and item['model'] == 'RS7':
        mot = '2'
    elif item['make'] == 'Audi' and item['model'] == 'Scirocco':
        mot = '5'
    elif item['make'] == 'Volkswagen' and item['model'] == '4 series':
        mot = '6'
    elif item['make'] == 'Volkswagen' and item['model'] == 'C63s':
        mot = '3'
    elif item['make'] == 'Volkswagen' and item['model'] == 'GTC':
        mot = '3'
    elif item['make'] == 'Volkswagen' and item['model'] == 'Civic':
        mot = '5'
    elif item['make'] == 'Volkswagen' and item['model'] == 'RS7':
        mot = '3'
    elif item['make'] == 'Volkswagen' and item['model'] == 'Scirocco':
        mot = '6'
    else:
        mot = '0'

    return Response(str(mot))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003, debug=True)
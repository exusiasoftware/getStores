from flask import Flask, jsonify, request, render_template
from flask_cors import CORS

app = Flask(__name__)


# This will enable CORS for all routes
CORS(app) 


stores = [
        {

            'name': 'My Wonderful Store',
            'items': [ 
                {
                'name': 'My Item',
                'price': 15.99
                },
                {
                'name': 'My Item 2',
                'price': 15.99
                },
                {
                'name': 'My Item 3',
                'price': 15.99
                }

            ]
        }

]


#home page of the app
@app.route('/') 
def home():
    return render_template('/index.html')

# POST /store data: {name:}
@app.route('/store', methods=['POST'])
def create_store():
    #pass
    request_data = request.get_json()
    new_store = {
          'name': request_data['name'],
          #'items': []
    }
   
    stores.append(new_store)
    return jsonify(new_store)


# GET /store/<string:name>
@app.route('/store/<string:name>') 
def get_store(name):
   for store in stores:
       if store['name'] == name:
           return jsonify(store)


# GET /store
@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})

# GET /store/<string:name>/item {name:,price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
        store['items'].append(new_item)
        return jsonify(new_item)
    return jsonify({'message': 'store not found'})     

# GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
    return jsonify({'message': 'store not found'}) 


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)
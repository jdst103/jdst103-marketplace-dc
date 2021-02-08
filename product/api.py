# Product service

#want simple restful api
from flask import Flask
from flask_restful import Resource, Api

#instantiate these objects
app = Flask(__name__)
api = Api(app)

#product class that extends resource
class Product(Resource):
    def get(self):
        #get method will return json below - e.g we selling the product items
        return {
            'products': ['88 key nord stage 3',
                        'Bass Amp',
                        'Sustain pedal',
                        'Piano stool']
        }

#rooting
api.add_resource(Product, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)

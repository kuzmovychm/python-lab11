from app import app, db
from models.toy import Toy
from flask import request, jsonify
from views.toy_schema import ToySchema


toy_schema = ToySchema()
toys_schema = ToySchema(many=True)


# endpoint to create a new toy
@app.route('/toys', methods=['POST'])
def add_toy():
    price = request.json['price']
    size = request.json['size']

    new_toy = Toy(price, size)

    db.session.add(new_toy)
    db.session.commit()

    return toy_schema.jsonify(new_toy)


# endpoint to show all toys
@app.route('/toys', methods=['GET'])
def show_toys():
    all_toys = Toy.query.all()
    result = toys_schema.dump(all_toys)
    return jsonify(result.data)


# endpoint to show toy by id
@app.route('/toys/<id>', methods=['GET'])
def show_toy_by_id(id):
    toy = Toy.query.get(id)
    return toy_schema.jsonify(toy)


# endpoint to update toy
@app.route('/toys/<id>', methods=['PUT'])
def update_toy(id):
    toy = Toy.query.get(id)
    new_price = request.json['price']
    new_size = request.json['size']

    toy.price = new_price
    toy.size = new_size

    db.session.commit()

    return toy_schema.jsonify(toy)


# endpoint to delete toy
@app.route('/toys/<id>')
def delete_toy_by_id(id):
    toy = Toy.query.get(id)
    db.session.delete(toy)
    db.session.commit()

    return toy_schema.jsonify(toy)



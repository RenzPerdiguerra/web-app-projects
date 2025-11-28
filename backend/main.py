# endpoints for products utilities
# endpoints for orders utilities
# endpoints for other orders utilities
from flask import request, jsonify
from config import app, db
from model import Products

@app.route('/get_products', methods=['GET'])
def get_products():
    products = Products.query.all()
    products_json = list(map(lambda x: x.to_json(), products))
    
    return jsonify({"products": products_json}) #200 is the default answer

@app.route('/insert_product', methods=['POST'])
def insert_product():
    category = request.json.get('category')
    g_name = request.json.get('g_name')
    b_name = request.json.get('b_name')
    d_arrived = request.json.get('d_arrived')
    d_expired = request.json.get('d_expired')
    cost = request.json.get('d_cost')
    price = request.json.get('d_price')
    qty = request.json.get('d_qty')
    stock_status = request.json.get('stock_status')
    
    if (not g_name or not b_name) or not cost:
        return (
            jsonify({"message": "You must include a generic or brand name and its cost"}),
                400,
    )
    
    new_product = Products(category=category,g_name=g_name,b_name=b_name,d_arrived=d_arrived,
                           d_expired=d_expired,cost=cost,price=price,qty=qty,stock_status=stock_status)
    try:
        db.session.add(new_product)
        db.session.commit()
    except Exception as e:
        return jsonify ({"message": str(e)}), 400
    
    return jsonify({"message": "New product inserted"}), 201

@app.route('/update_product/<int:prod_id>', methods=['PATCH'])
def update_product():
    product = Products.query.get('prod_id')

    if not product:
        return jsonify({"message": "Product not found"}), 404
    
    data = request.json
    product.g_name = data.get("gName", product.g_name)
    product.b_name = data.get("bName", product.b_name)
    product.cost = data.get("cost", product.cost)
    
    db.session.commit()
    
    return jsonify({"message": "Product updated"}), 200

@app.route('/delete_product/<int:prod_id>', methods=['DELETE'])
def delete_product():
    product = Products.query.get('prod_id')
    
    if not product:
        return jsonify({"message": "Product not found"}), 404
    
    db.session.delete(product)
    db.session.commit()
    
    return jsonify({"message": "Product deleted"}), 200
    
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    
    app.run(debug=True)
    
    
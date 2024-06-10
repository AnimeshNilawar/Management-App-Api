from flask import Flask, jsonify, request
from database.create import createTables
from database.UserOperations import createUser, update_User_details,getAllUser,getSpecificUser
from database.productsOperations import add_product, getAllProducts, getSpecificProduct, updateProductDetails
from database.orderOperations import orderDetails, updateOrderDetails, getAllOrders, getOrderDetailsByFilter


app = Flask(__name__)

@app.route('/CreateUser', methods=['POST'])
def createUserRoute():
    name = request.form['name']
    password = request.form['password']
    address = request.form['address']
    email = request.form['email']
    phone = request.form['phone']
    pincode = request.form['pincode']

    if createUser(name=name, password=password, address=address, email=email, phone=phone, pincode=pincode):
        response = {
            'status': 200,
            'message': 'Successfully created'
        }
        return jsonify(response), 200
    else:
        response = {
            'status': 500,
            'message': 'Failed to create user'
        }
        return jsonify(response), 500

@app.route('/getAllUser', methods=['GET'])
def getAllUserRoute():
    users = getAllUser()
    try:
        return jsonify(users), 200
    except Exception as e:
        return jsonify({'status': '500','message': str(e) }), 500
    
@app.route('/getSpecificUser', methods=['GET'])
def getSpecificUserRoute():
    user_id = request.form['user_id']
    user = getSpecificUser(user_id)
    try:
        return jsonify(user), 200
    except Exception as e:
        return jsonify({'status': '500', 'message': str(e) }), 500
    
@app.route('/updateUser', methods=['PATCH'])
def updateUserRoute():
    try:
        id = request.form['id']
        updateUser = {}
        for key, value in request.form.items():
            if key != 'id':
                updateUser[key] = value
            update_User_details(id, **updateUser)

            return jsonify({'status': 200, 'message': 'User updated successfully'}), 200
    except Exception as e:
        return jsonify({'status': 500, 'message': str(e)}), 500
    

@app.route('/CreateProduct', methods=['POST'])
def createProductRoute():
    try:
        name = request.form['name']
        brand = request.form['brand']
        price = request.form['price']
        category = request.form['category']
        stock = request.form['stock']
        isActive = request.form['isActive']

        if add_product(name=name, brand=brand, price=price, category=category, stock=stock, isActive=isActive):
            response = {
                'status': 200,
                'message': 'Successfully created'
            }
            return jsonify(response), 200
    except Exception as e:
        response = {
            'status': 500,
            'message': str(e)
        }
        return jsonify(response), 500
    
@app.route('/getAllProducts', methods=['GET'])
def getAllProductsRoute():
    products = getAllProducts()
    try:
        return jsonify(products), 200
    except Exception as e:
        response = {
            'status': 500,
            'message': str(e)
        }
        return jsonify(response), 500

@app.route('/getSpecificProduct', methods=['GET'])
def getSpecificProductRoute():
    product_id = request.form['product_id']
    product = getSpecificProduct(product_id)
    try:
        return jsonify(product), 200
    except Exception as e:
        response = {
            'status': 500,
            'message': str(e)
        }
        return jsonify(response), 500
    
@app.route('/updateProduct', methods=['PATCH'])
def updateProductRoute():
    try:
        id = request.form['product_id']
        updateProduct = {}
        for key, value in request.form.items():
            if key != 'id':
                updateProduct[key] = value
            updateProductDetails(id, **updateProduct)
            response = {
                'status': 200,
                'message': 'Product updated successfully'
            }
            return jsonify(response), 200
    except Exception as e:
        response = {
            'status': 500,
            'message': str(e)
        }
        return jsonify(response), 500

@app.route('/orderDetails', methods=['POST'])
def orderDetailsRoute():
    try:
        user_id = request.form['user_id']
        product_id = request.form['product_id']
        status = request.form['status']
        quantity = request.form['quantity']
        total_amount = request.form['total_amount']

        if orderDetails(user_id=user_id, product_id=product_id, status=status, quantity=quantity, total_amount=total_amount):
            response = {
            'status': 200,
            'message': 'Order placed successfully'
        }
        return jsonify(response), 200
    except Exception as e:
        response = {
            'status': 500,
            'message': str(e)
        }
        return jsonify(response), 500
    
@app.route('/getAllOrders', methods=['GET'])
def getAllOrdersRoute():
    orders = getAllOrders()
    try:
        return jsonify(orders), 200
    except Exception as e:
        response = {
            'status': 500,
            'message': str(e)
        }
        return jsonify(response), 500
    
@app.route('/getOrderDetailsByFilter', methods=['GET'])
def getOrderDetailsByFilterRoute():
    user_id = request.form['user_id']
    isApproved = request.form['isApproved']
    orders = getOrderDetailsByFilter(user_id, isApproved)
    try:
        return jsonify(orders), 200
    except Exception as e:
        response = {
            'status': 500,
            'message': str(e)
        }
        return jsonify(response), 500
    
@app.route('/updateOrder', methods=['PATCH'])
def updateOrderRoute():
    try:
        id = request.form['id']
        updateOrder = {}
        for key, value in request.form.items():
            if key != 'id':
                updateOrder[key] = value
            updateOrderDetails(id, **updateOrder)
            response = {
                'status': 200,
                'message': 'Order updated successfully'
            }
            return jsonify(response), 200
    except Exception as e:
        response = {
            'status': 500,
            'message': str(e)
        }
        return jsonify(response), 500



if __name__ == '__main__':
    createTables()
    app.run(debug=True)

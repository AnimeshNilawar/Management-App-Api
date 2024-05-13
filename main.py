from flask import Flask, jsonify, request
from database.create import createUser, createTables
from database.GetUsers import getAllUser, getSpecificUser
from database.userOperation import blockedAPi, ApprovedAPi, updateUserLevelAPi
from database.productsOperations import add_product, productisActiveAPi, updatePriceAPi, updateStockAPi

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

@app.route('/getAllUsers', methods=['GET'])
def getAllUsers():
    return jsonify(getAllUser())

@app.route('/', methods=['GET'])
def home():
    return "Hello"

@app.route('/getSpecificUsers', methods=['GET']) 
def getSpecificUsers():
    user_id = request.args.get('user_id')
    if user_id is None:
        response = {
            'status': 400,
            'message': 'User ID not provided'
        }
        return jsonify(response), 400
    else:
        user = getSpecificUser(user_id)
        if user:
            response = {
                'status': 200,
                'message': 'User found',
                'user': user
            }
            return jsonify(response), 200
        else:
            response = {
                'status': 404,
                'message': 'User not found'
            }
            return jsonify(response), 404
    

@app.route('/userBlocked', methods=['PATCH'])
def userBlocked():
    id = request.form['id']
    blocked = request.form['blocked']
    if blockedAPi(id=id, blocked=blocked):
        response = {
            'status': 200,
            'message': 'User blocked successfully'
        }
        return jsonify(response), 200
    else:
        response = {
            'status': 500,
            'message': 'Failed to block user'
        }
        return jsonify(response), 500

@app.route('/userApproved', methods=['PATCH'])
def userApproved():
    id = request.form['id']
    approved = request.form['approved']
    if ApprovedAPi(id=id, approved=approved):
        response = {
            'status': 200,
            'message': 'User approved successfully'
        }
        return jsonify(response), 200
    else:
        response = {
            'status': 500,
            'message': 'Failed to approve user'
        }
        return jsonify(response), 500

@app.route('/userLevel', methods=['PATCH'])  
def userLevel():
    id = request.form['id']
    level = request.form['level']
    if updateUserLevelAPi(id=id, level=level):
        response = {
            'status': 200,
            'message': 'User level updated successfully'
        }
        return jsonify(response), 200
    else:
        response = {
            'status': 500,
            'message': 'Failed to update user level'
        }
        return jsonify(response), 500

@app.route('/createProduct', methods=['POST'])
def createProduct():
    name = request.form['name']
    brand = request.form['brand']
    description = request.form['description']
    price = request.form['price']
    category = request.form['category']
    stock = request.form['stock']
    isActive = request.form['isActive']

    if add_product(name=name, brand=brand, description=description, price=price, category=category, stock=stock, isActive=isActive):
        response = {
            'status': 200,
            'message': 'Successfully created'
        }
        return jsonify(response), 200
    else:
        response = {
            'status': 500,
            'message': 'Failed to create product'
        }
        return jsonify(response), 500
    
@app.route('/productisActive', methods=['PATCH'])
def productisActive():
    name = request.form['name']
    isActive = request.form['isActive']
    if productisActiveAPi(name=name, isActive=isActive):
        response = {
            'status': 200,
            'message': 'Product status updated successfully'
        }
        return jsonify(response), 200
    else:
        response = {
            'status': 500,
            'message': 'Failed to update product status'
        }
        return jsonify(response), 500

@app.route('/updatePrice', methods=['PATCH'])
def updatePrice():
    name = request.form['name']
    price = request.form['price']

    if updatePriceAPi(name=name, price=price):
        response = {
            'status': 200,
            'message': 'Price updated successfully'
        }
        return jsonify(response), 200
    else:
        response = {
            'status': 500,
            'message': 'Failed to update price'
        }
        return jsonify(response), 500
    
@app.route('/updateStock', methods=['PATCH'])
def updateStock():
    name = request.form['name']
    stock = request.form['stock']

    if updateStockAPi(name=name, stock=stock):
        response = {
            'status': 200,
            'message': 'Stock updated successfully'
        }
        return jsonify(response), 200
    else:
        response = {
            'status': 500,
            'message': 'Failed to update stock'
        }
        return jsonify(response), 500


if __name__ == '__main__':
    createTables()
    app.run(debug=True)

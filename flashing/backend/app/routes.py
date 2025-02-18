from flask import Blueprint, request, jsonify
from app import db
from app.models import Transaction
from app.auth import token_required

routes = Blueprint('routes', __name__)

@routes.route('/api/transactions', methods=['GET'])
@token_required
def get_transactions():
    transactions = Transaction.query.all()
    return jsonify([transaction.to_dict() for transaction in transactions]), 200

@routes.route('/api/transactions', methods=['POST'])
@token_required
def create_transaction():
    data = request.get_json()
    new_transaction = Transaction(**data)
    db.session.add(new_transaction)
    db.session.commit()
    return jsonify(new_transaction.to_dict()), 201

@routes.route('/api/transactions/<int:transaction_id>', methods=['GET'])
@token_required
def get_transaction(transaction_id):
    transaction = Transaction.query.get_or_404(transaction_id)
    return jsonify(transaction.to_dict()), 200

@routes.route('/api/transactions/<int:transaction_id>', methods=['DELETE'])
@token_required
def delete_transaction(transaction_id):
    transaction = Transaction.query.get_or_404(transaction_id)
    db.session.delete(transaction)
    db.session.commit()
    return jsonify({'message': 'Transaction deleted'}), 204

@routes.route('/api/login', methods=['POST'])
def login():
    # Logic for user login
    pass

@routes.route('/api/register', methods=['POST'])
def register():
    # Logic for user registration
    pass

@routes.route('/api/payments', methods=['POST'])
def process_payment():
    # Logic for processing payments
    pass
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from .models import db, User, Transaction
from .paypal_service import send_paypal_transfer
from .receipt_service import generate_receipt
from .email_service import send_payment_email

main = Blueprint('main', __name__)

@main.route('/transactions', methods=['GET'])
@jwt_required()
def get_transactions():
    user_id = get_jwt_identity()
    transactions = Transaction.query.filter_by(user_id=user_id).all()
    
    return jsonify([{
        'id': tx.id,
        'receiver_email': tx.receiver_email,
        'amount': tx.amount,
        'currency': tx.currency,
        'status': tx.status,
        'paypal_transaction_id': tx.paypal_transaction_id,
        'created_at': tx.created_at.strftime('%Y-%m-%d %H:%M:%S')
    } for tx in transactions])

@main.route('/send-payment', methods=['POST'])
@jwt_required()
def send_payment():
    data = request.get_json()
    user_id = get_jwt_identity()
    
    receiver_email = data.get('receiver_email')
    amount = data.get('amount')
    currency = data.get('currency', 'USD')

    user = User.query.get(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404

    transaction_id, status = send_paypal_transfer(receiver_email, amount, currency)
    
    new_transaction = Transaction(
        user_id=user_id,
        receiver_email=receiver_email,
        amount=amount,
        currency=currency,
        status=status,
        paypal_transaction_id=transaction_id
    )
    db.session.add(new_transaction)
    db.session.commit()

    receipt_pdf = generate_receipt(new_transaction)
    send_payment_email(receiver_email, new_transaction, receipt_pdf)

    return jsonify({'message': 'Payment initiated', 'transaction_id': transaction_id, 'status': status}), 200

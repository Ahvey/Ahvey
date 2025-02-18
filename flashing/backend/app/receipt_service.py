from flask import jsonify
from datetime import datetime

class ReceiptService:
    def __init__(self):
        self.receipts = []

    def generate_receipt(self, transaction_id, amount, user_email):
        receipt = {
            'transaction_id': transaction_id,
            'amount': amount,
            'user_email': user_email,
            'date': datetime.utcnow().isoformat()
        }
        self.receipts.append(receipt)
        return receipt

    def get_receipts(self):
        return jsonify(self.receipts)

    def get_receipt_by_transaction_id(self, transaction_id):
        for receipt in self.receipts:
            if receipt['transaction_id'] == transaction_id:
                return jsonify(receipt)
        return jsonify({'error': 'Receipt not found'}), 404
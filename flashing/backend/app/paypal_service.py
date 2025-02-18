from flask import current_app
import requests

class PayPalService:
    def __init__(self):
        self.client_id = current_app.config['PAYPAL_CLIENT_ID']
        self.client_secret = current_app.config['PAYPAL_CLIENT_SECRET']
        self.base_url = "https://api.paypal.com"  # Use sandbox URL for testing

    def get_access_token(self):
        url = f"{self.base_url}/v1/oauth2/token"
        headers = {
            "Accept": "application/json",
            "Accept-Language": "en_US"
        }
        response = requests.post(url, headers=headers, auth=(self.client_id, self.client_secret), data={"grant_type": "client_credentials"})
        response_data = response.json()
        return response_data.get("access_token")

    def create_payment(self, amount, currency="USD"):
        access_token = self.get_access_token()
        url = f"{self.base_url}/v1/payments/payment"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {access_token}"
        }
        payment_data = {
            "intent": "sale",
            "payer": {
                "payment_method": "paypal"
            },
            "transactions": [{
                "amount": {
                    "total": str(amount),
                    "currency": currency
                },
                "description": "Payment description"
            }],
            "redirect_urls": {
                "return_url": "http://localhost:5000/payment/success",
                "cancel_url": "http://localhost:5000/payment/cancel"
            }
        }
        response = requests.post(url, headers=headers, json=payment_data)
        return response.json()

    def execute_payment(self, payment_id, payer_id):
        access_token = self.get_access_token()
        url = f"{self.base_url}/v1/payments/payment/{payment_id}/execute"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {access_token}"
        }
        execute_data = {
            "payer_id": payer_id
        }
        response = requests.post(url, headers=headers, json=execute_data)
        return response.json()
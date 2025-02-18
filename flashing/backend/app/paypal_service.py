import requests
import os

PAYPAL_API_BASE = os.getenv('PAYPAL_API_BASE')
PAYPAL_CLIENT_ID = os.getenv('PAYPAL_CLIENT_ID')
PAYPAL_CLIENT_SECRET = os.getenv('PAYPAL_CLIENT_SECRET')

def get_access_token():
    response = requests.post(
        f"{PAYPAL_API_BASE}/v1/oauth2/token",
        auth=(PAYPAL_CLIENT_ID, PAYPAL_CLIENT_SECRET),
        data={'grant_type': 'client_credentials'}
    )
    return response.json().get("access_token")

def send_paypal_transfer(receiver_email, amount, currency="USD"):
    access_token = get_access_token()
    url = f"{PAYPAL_API_BASE}/v1/payments/payouts"
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}"
    }
    
    data = {
        "sender_batch_header": {"email_subject": "You have received a payment"},
        "items": [{
            "recipient_type": "EMAIL",
            "amount": {"value": amount, "currency": currency},
            "receiver": receiver_email,
            "note": "PayPal transfer",
            "sender_item_id": "transaction_12345"
        }]
    }
    
    response = requests.post(url, headers=headers, json=data)
    payout = response.json()
    
    transaction_id = payout.get("batch_header", {}).get("payout_batch_id", "N/A")
    status = "Pending" if transaction_id != "N/A" else "Failed"
    
    return transaction_id, status

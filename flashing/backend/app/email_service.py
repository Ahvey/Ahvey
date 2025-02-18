import smtplib
from email.message import EmailMessage
import os

SMTP_SERVER = os.getenv('MAIL_SERVER')
SMTP_PORT = int(os.getenv('MAIL_PORT'))
SMTP_USERNAME = os.getenv('MAIL_USERNAME')
SMTP_PASSWORD = os.getenv('MAIL_PASSWORD')

def send_payment_email(receiver_email, transaction, receipt_pdf):
    msg = EmailMessage()
    msg['Subject'] = 'PayPal Payment Notification'
    msg['From'] = SMTP_USERNAME
    msg['To'] = receiver_email
    msg.set_content(f"""
        Dear {receiver_email},

        You have received a pending PayPal payment of {transaction.amount} {transaction.currency}.
        
        To accept this payment, please visit your PayPal account.

        Regards,
        PayPal Team
    """)

    with open(receipt_pdf, 'rb') as f:
        msg.add_attachment(f.read(), maintype='application', subtype='pdf', filename="receipt.pdf")

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        server.send_message(msg)

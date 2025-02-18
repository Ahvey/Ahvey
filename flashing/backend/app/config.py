class Config:
    SECRET_KEY = 'your_secret_key_here'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'  # Update with your database URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PAYPAL_CLIENT_ID = 'your_paypal_client_id_here'
    PAYPAL_CLIENT_SECRET = 'your_paypal_client_secret_here'
    MAIL_SERVER = 'smtp.example.com'  # Update with your mail server
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'your_email@example.com'  # Update with your email
    MAIL_PASSWORD = 'your_email_password_here'  # Update with your email password
    ADMIN_EMAIL = 'admin@example.com'  # Update with your admin email
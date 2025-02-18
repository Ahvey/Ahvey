📌 Project Title

PayPal Payment Processing App

🚀 A full-stack application that integrates PayPal API to handle payments, send receipts, and notify users via email.

📖 Table of Contents
	•	Features
	•	Tech Stack
	•	Project Structure
	•	Installation
	•	Environment Variables
	•	API Documentation
	•	Deployment Guide
	•	License

✨ Features

✅ User Payments: Send & receive PayPal payments
✅ Transaction Logging: Stores payment details in a database
✅ Receipts & Notifications: Generates receipts & sends email notifications
✅ PayPal Integration: Uses PayPal REST API for payments
✅ Admin Panel: Manage transactions & user accounts
✅ Security: Uses JWT authentication & environment variables

🛠️ Tech Stack

Technology	Purpose
Flask	Backend (API)
React.js	Frontend (User Interface)
PostgreSQL	Database (Supabase)
PayPal API	Payment Processing
Netlify	Frontend Hosting
Render	Backend Hosting
SMTP Email	Sending notifications

📁 Project Structure

📦 project-root
 ┣ 📂 backend
 ┃ ┣ 📂 app
 ┃ ┃ ┣ 📜 models.py
 ┃ ┃ ┣ 📜 routes.py
 ┃ ┃ ┣ 📜 utils.py
 ┃ ┣ 📜 app.py
 ┃ ┣ 📜 requirements.txt
 ┣ 📂 frontend
 ┃ ┣ 📂 src
 ┃ ┃ ┣ 📂 components
 ┃ ┃ ┣ 📂 pages
 ┃ ┃ ┣ 📜 App.js
 ┃ ┣ 📜 package.json
 ┣ 📜 .env
 ┣ 📜 README.md

⚙️ Installation

1️⃣ Clone the Repository

git clone https://github.com/your-username/paypal-app.git
cd paypal-app

2️⃣ Setup Backend (Flask)

cd backend
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt

3️⃣ Setup Frontend (React)

cd frontend
npm install

4️⃣ Run the App
	•	Backend (Flask)

cd backend
flask run


	•	Frontend (React)

cd frontend
npm start

🔑 Environment Variables

Create a .env file in both backend/ and frontend/:

Backend (backend/.env)

SECRET_KEY=your_secret_key
PAYPAL_CLIENT_ID=your_paypal_client_id
PAYPAL_SECRET=your_paypal_secret
DATABASE_URL=postgresql://your_db_url
CORS_ALLOWED_ORIGINS=https://your-frontend-url.netlify.app
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USERNAME=your_email@gmail.com
EMAIL_PASSWORD=your_email_password

Frontend (frontend/.env)

REACT_APP_API_URL=https://your-backend-url.onrender.com
REACT_APP_PAYPAL_CLIENT_ID=your_paypal_client_id

📡 API Documentation

📌 Base URL

https://your-backend-url.onrender.com/api

🛒 Payment Endpoints

1️⃣ Create PayPal Payment
	•	Endpoint: POST /paypal/create-payment
	•	Description: Initiates a payment with PayPal
	•	Request Body:

{
  "amount": "50.00",
  "currency": "USD",
  "receiver_email": "receiver@example.com"
}


	•	Response Example:

{
  "payment_id": "PAY-12345678",
  "approval_url": "https://paypal.com/approve-payment"
}



2️⃣ Execute PayPal Payment
	•	Endpoint: POST /paypal/execute-payment
	•	Description: Completes a PayPal transaction
	•	Request Body:

{
  "payment_id": "PAY-12345678",
  "payer_id": "PAYER-987654"
}


	•	Response Example:

{
  "status": "success",
  "transaction_id": "TRANSACTION-12345"
}

📜 Transaction Endpoints

3️⃣ Get All Transactions
	•	Endpoint: GET /transactions
	•	Description: Fetches all transactions of the user
	•	Headers:

Authorization: Bearer <your_jwt_token>


	•	Response Example:

[
  {
    "transaction_id": "12345",
    "amount": "50.00",
    "status": "Completed"
  }
]



4️⃣ Get Transaction by ID
	•	Endpoint: GET /transactions/{transaction_id}
	•	Description: Fetch details of a single transaction
	•	Response Example:

{
  "transaction_id": "12345",
  "amount": "50.00",
  "status": "Completed",
  "created_at": "2025-02-18T12:00:00Z"
}

🔐 User Endpoints

5️⃣ Get User Profile
	•	Endpoint: GET /users/me
	•	Description: Retrieves current user profile
	•	Headers:

Authorization: Bearer <your_jwt_token>


	•	Response Example:

{
  "user_id": "1",
  "email": "user@example.com",
  "created_at": "2025-02-18T12:00:00Z"
}

🚀 Deployment Guide

1️⃣ Deploy Backend (Flask) on Render
	1.	Push your backend code to GitHub
	2.	Sign up on Render
	3.	Create a new Web Service
	4.	Connect your GitHub repository
	5.	Set up the Build & Start Command

pip install -r requirements.txt
gunicorn app:app


	6.	Add Environment Variables
	7.	Click Deploy 🚀

2️⃣ Deploy Database (PostgreSQL) on Supabase
	1.	Sign up on Supabase
	2.	Create a new project
	3.	Copy Database URL
	4.	Add it to DATABASE_URL in your .env file

3️⃣ Deploy Frontend (React) on Netlify
	1.	Push your frontend code to GitHub
	2.	Sign up on Netlify
	3.	Connect your GitHub repo & set Build Command:

npm run build


	4.	Set Publish Directory: build
	5.	Deploy & update REACT_APP_API_URL in .env

📜 License

This project is licensed under the MIT License.

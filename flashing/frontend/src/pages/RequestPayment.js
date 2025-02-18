import React, { useState } from "react";

function RequestPayment() {
    const [receiverEmail, setReceiverEmail] = useState("");
    const [amount, setAmount] = useState("");
    const [currency, setCurrency] = useState("USD");

    const handlePayment = async (e) => {
        e.preventDefault();
        const token = localStorage.getItem("token");

        const response = await fetch("http://localhost:5000/send-payment", {
            method: "POST",
            headers: { 
                "Content-Type": "application/json",
                Authorization: `Bearer ${token}`
            },
            body: JSON.stringify({ receiver_email: receiverEmail, amount, currency })
        });

        const data = await response.json();
        if (response.ok) {
            alert(`Payment initiated: ${data.transaction_id}`);
        } else {
            alert("Payment failed");
        }
    };

    return (
        <div>
            <h2>Send PayPal Payment</h2>
            <form onSubmit={handlePayment}>
                <input type="email" placeholder="Receiver Email" value={receiverEmail} onChange={(e) => setReceiverEmail(e.target.value)} required />
                <input type="number" placeholder="Amount" value={amount} onChange={(e) => setAmount(e.target.value)} required />
                <select value={currency} onChange={(e) => setCurrency(e.target.value)}>
                    <option value="USD">USD</option>
                    <option value="EUR">EUR</option>
                </select>
                <button type="submit">Send Payment</button>
            </form>
        </div>
    );
}

export default RequestPayment;

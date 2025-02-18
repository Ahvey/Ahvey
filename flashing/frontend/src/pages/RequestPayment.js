import React, { useState } from 'react';

const RequestPayment = () => {
    const [amount, setAmount] = useState('');
    const [description, setDescription] = useState('');
    const [error, setError] = useState('');
    const [success, setSuccess] = useState('');

    const handlePaymentRequest = async (e) => {
        e.preventDefault();
        setError('');
        setSuccess('');

        if (!amount || !description) {
            setError('Please fill in all fields.');
            return;
        }

        try {
            const response = await fetch('/api/request-payment', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ amount, description }),
            });

            if (!response.ok) {
                throw new Error('Payment request failed.');
            }

            const data = await response.json();
            setSuccess(`Payment request successful: ${data.message}`);
        } catch (err) {
            setError(err.message);
        }
    };

    return (
        <div>
            <h1>Request Payment</h1>
            <form onSubmit={handlePaymentRequest}>
                <div>
                    <label>Amount:</label>
                    <input
                        type="number"
                        value={amount}
                        onChange={(e) => setAmount(e.target.value)}
                        required
                    />
                </div>
                <div>
                    <label>Description:</label>
                    <input
                        type="text"
                        value={description}
                        onChange={(e) => setDescription(e.target.value)}
                        required
                    />
                </div>
                <button type="submit">Request Payment</button>
            </form>
            {error && <p style={{ color: 'red' }}>{error}</p>}
            {success && <p style={{ color: 'green' }}>{success}</p>}
        </div>
    );
};

export default RequestPayment;
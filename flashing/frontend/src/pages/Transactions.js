import React, { useEffect, useState } from "react";

function Transactions() {
    const [transactions, setTransactions] = useState([]);

    useEffect(() => {
        const fetchTransactions = async () => {
            const token = localStorage.getItem("token");
            const response = await fetch("http://localhost:5000/transactions", {
                headers: { Authorization: `Bearer ${token}` }
            });

            const data = await response.json();
            if (response.ok) {
                setTransactions(data);
            } else {
                alert("Failed to load transactions");
            }
        };

        fetchTransactions();
    }, []);

    return (
        <div>
            <h2>Transaction History</h2>
            <ul>
                {transactions.map((tx) => (
                    <li key={tx.id}>
                        {tx.amount} {tx.currency} to {tx.receiver_email} - Status: {tx.status}
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default Transactions;

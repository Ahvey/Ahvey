import React, { useEffect, useState } from "react";

function AdminDashboard() {
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
            <h2>Admin Dashboard</h2>
            <table>
                <thead>
                    <tr>
                        <th>Receiver Email</th>
                        <th>Amount</th>
                        <th>Currency</th>
                        <th>Status</th>
                    </tr>
                </thead>
                <tbody>
                    {transactions.map((tx) => (
                        <tr key={tx.id}>
                            <td>{tx.receiver_email}</td>
                            <td>{tx.amount}</td>
                            <td>{tx.currency}</td>
                            <td>{tx.status}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}

export default AdminDashboard;

SELECT
    Customers.customer_name,
    SUM(Orders.amount) AS Total_Amount
FROM Customers
INNER JOIN Orders
ON Customers.customer_id=Orders.customer_id
GROUP BY Customers.customer_name;

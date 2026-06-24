SELECT
    Customers.customer_name,
    Orders.amount
FROM Customers
INNER JOIN Orders
ON Customers.customer_id=Orders.customer_id;
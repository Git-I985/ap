SELECT product.name, COUNT(ordertoproduct.product_id) as 'count'
FROM `ordertoproduct`
         INNER JOIN product ON product.id = ordertoproduct.product_id
GROUP BY `product_id`
ORDER BY count ASC;

SELECT c.company, COUNT(client_id) as count
FROM `order`
         INNER JOIN client c on `order`.client_id = c.id
GROUP BY client_id
ORDER BY count ASC;

SELECT client.company, SUM(amount) as total_count, SUM(product.sale_price) as total_price
FROM ordertoproduct
         INNER JOIN `order` ON ordertoproduct.order_id = `order`.id
         INNER JOIN `client` ON client.id = `order`.client_id
         INNER JOIN product ON product.id = `ordertoproduct`.product_id
GROUP BY order_id
ORDER BY total_count ASC;
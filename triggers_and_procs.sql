DROP PROCEDURE IF EXISTS alinaproj.calculate_sale_price;
delimiter //
CREATE PROCEDURE alinaproj.calculate_sale_price(buy_price int, margin int, out sale_price int)
begin
    SET sale_price = buy_price + (margin * (buy_price / 100));
end//
delimiter ;

DROP TRIGGER IF EXISTS alinaproj.on_products_insert;
delimiter //
CREATE TRIGGER alinaproj.on_products_insert
    BEFORE INSERT
    ON alinaproj.product
    FOR EACH ROW
BEGIN
    set @sale_price = 0;
    call alinaproj.calculate_sale_price(NEW.buy_price, NEW.margin, @sale_price);
    SET NEW.sale_price = @sale_price;
END//
delimiter ;
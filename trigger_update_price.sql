use sql12707743;

CREATE TABLE cart_items_temp (
    cart_item_id INT PRIMARY KEY,
    total_price DECIMAL(10,2)
);

DELIMITER //

CREATE TRIGGER update_total_price
BEFORE UPDATE ON cart_items
FOR EACH ROW
BEGIN
    DECLARE itemPrice DECIMAL(10,2);

    -- Fetch the item price from the menu_items table
    SELECT price INTO itemPrice FROM menu_items WHERE menu_items.item_id = NEW.item_id;

    -- Calculate the total price and assign it to the NEW row
    SET NEW.total_price = itemPrice * NEW.quantity;
END //

DELIMITER ;


DELIMITER //

CREATE TRIGGER after_update_total_price
AFTER INSERT ON cart_items_temp
FOR EACH ROW
BEGIN
    -- Update the cart_items table with the total price
    UPDATE cart_items
    SET total_price = NEW.total_price
    WHERE cart_item_id = NEW.cart_item_id;
    
    -- Remove the entry from the temporary table
    DELETE FROM cart_items_temp WHERE cart_item_id = NEW.cart_item_id;
END //

DELIMITER ;
show triggers;

use sql12707743;
DELIMITER //

CREATE TRIGGER update_total_price
AFTER UPDATE ON cart_items
FOR EACH ROW
BEGIN
    DECLARE itemPrice DECIMAL(10,2);

    -- Fetch the item price from the menu_items table
    SELECT price INTO itemPrice FROM menu_items WHERE menu_items.item_id = NEW.item_id;

    -- Calculate the total price and update the cart_items table
    UPDATE cart_items
    SET total_price = itemPrice * NEW.quantity
    WHERE cart_item_id = NEW.cart_item_id;
END //

DELIMITER ;
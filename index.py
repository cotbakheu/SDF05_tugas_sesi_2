def count_price_after_discount(unit_price, quantity, total_items):
    subtotal = unit_price * quantity

    if total_items > 100:
        discount_rate = 0.10
    else:
        discount_rate = 0.05

    price_after_discount = subtotal * (1 - discount_rate)

    return price_after_discount

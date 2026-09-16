def count_price_after_discount(unit_price, quantity, total_items):
    subtotal = unit_price * quantity

    if total_items > 100:
        discount_rate = 0.10
    else:
        discount_rate = 0.05

    price_after_discount = subtotal * (1 - discount_rate)

    return price_after_discount

def count_delivery_fee(total_price, is_member, delivery_fee):
    if not is_member:
        return total_price + delivery_fee
    return total_price

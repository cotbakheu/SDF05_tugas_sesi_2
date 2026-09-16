def count_total_price(unit_price, quantity, is_member = False, delivery_fee = 7000):
  
  total_price = count_price_after_discount(unit_price, quantity)

  total_price = count_delivery_fee(total_price, is_member, delivery_fee)
    
  return total_price

def count_price_after_discount(unit_price, quantity):
    subtotal = unit_price * quantity

    if quantity > 100:
        discount_rate = 0.10
    else:
        discount_rate = 0.05

    price_after_discount = subtotal * (1 - discount_rate)

    return price_after_discount

def count_delivery_fee(total_price, is_member, delivery_fee):
    if not is_member:
        return total_price + delivery_fee
    return total_price

# Nama yang penting adalah total_price yang mana merupakan total yang harus 
# dibayar oleh pembeli, termasuk count_price_after_discount dan count_delivery_fee 
# jika berlaku. Fungsi ini menghitung total harga berdasarkan harga per item, jumlah item, 
# status keanggotaan, dan biaya pengiriman.
  

print(count_total_price(1000, 200))

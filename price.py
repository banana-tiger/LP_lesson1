from decimal import Decimal

def format_price(price):
    price = Decimal(price)
    return f"Цена: {int(price)} руб. или {round(price, 4)}"

temp_var = format_price(56.245657)

print(temp_var)
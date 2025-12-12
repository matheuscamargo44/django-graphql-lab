# 1. Cadastre em um dicionário 5 produtos e seus respectivos preços, depois mostre o conteúdo do dicionário com um produto por linha.
# 1. Register 5 products and their respective prices in a dictionary, then show the dictionary content with one product per line.

products = {
    "Mechanical Keyboard": 250.00,
    "Gaming Mouse": 129.90,
    "24 Monitor": 899.00,
    "HDMI Cable": 35.50, 
    "Laptop Stand": 75.00
}

for product, price in products.items():
    print(f"Product: {product} | Price: {price:.2f}")

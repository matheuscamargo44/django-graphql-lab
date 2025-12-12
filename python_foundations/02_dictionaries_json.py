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
    print(f"Product: {product} | Price: {price:.2f}         ")

# 2. Carregue um dicionário onde a chave seja o nome de um aluno e o valor seja uma lista contendo 3 notas desse aluno. No final, imprima as notas e as médias de cada aluno.
# 2. Create a dictionary where the key is the student's name and the value is a list containing 3 grades. Finally, print the grades and the average for each student.

gradebook = {  
    "Matheus": [8.5, 9.0, 9.5],
    "Ana": [7.0, 8.5, 3.0],
    "Jorge": [6.0, 7.0, 6.5]
}

for student, grades in gradebook.items():
    
    average = sum(grades) / len(grades)
    print(f"Student: {student} | Grades: {grades} | Average: {average:.2f}")
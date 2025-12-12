import random
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

# 3. Crie dois dicionários com conteúdos afins e em seguida junte os dois dicionários em uma lista. Mostre o conteúdo do dicionário.
# 3. Create two dictionaries with related content and then join the two dictionaries into a list. Display the content of the dictionary.

hardware = {
    "Processor": "Ryzen 5 5600X",
    "Graphics card": "GTX 1650"
}

peripherals = {
    "Mouse": "ATK 9 Series",
    "Keyboard": "HyperX Alloy Origins"
}

inventory = [hardware, peripherals]

print(inventory)

# 4. Cadastre 5 funcionários em um dicionário, pelo teclado, com as seguintes chaves: nome, idade, cargo, salário. No final, mostre o conteúdo do dicionário e a média dos salários.
# 4. Register 5 employees in a dictionary via keyboard input containing: name, age, position, salary.
employees = []

for i in range(5):
    name = input("Type the name: ")
    age = int(input("Type the age: "))
    position = input ("Type the position: ")
    salary = float(input("Type the salary: "))

    worker = {
        "Name": name,
        "Age" : age,
        "Position" : position,
        "Salary": salary 
    }

    employees.append(worker)

print (employees)  

total_salary = 0

for worker in employees:
    total_salary += worker["Salary"]

average = total_salary / len(employees)
print(f"\nAverage Salary: $ {average:.2f}")

# 5 Cadastre em uma tupla 5 nomes. Em seguida crie um dicionário, onde a chave deverá ser um número aleatório entre 0 e 100 e o valor deverá ser os nomes cadastrados na tupla.
# 5. Register 5 names in a tuple. Then, create a dictionary where the keys are random numbers between 0 and 100, and the values are the names from the tuple.

temp_list = []

for i in range(5):
    name = input("Digite o nome: ")
    temp_list.append(name)

names_tuple = tuple(temp_list)

random_dict = {}

for name in names_tuple:
    random_key = random.randint(0, 100)

    while random_key in random_dict:
        random_key = random.randint(0, 100)
    random_dict[random_key] = name

print(random_dict)
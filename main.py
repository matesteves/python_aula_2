# Inteiros (int)
# Escreva um programa que soma dois números inteiros inseridos pelo usuário.

#a = int(input("Qual o primeiro número? "))
#b = int(input("Qual o segundo número? "))
#c = a + b
#print(f"A soma é: {c}")

# Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.

#a = int(input("Qual o número? "))
#print(a % 3)

# Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.

#a = int(input("Qual o primeiro número? "))
#b = int(input("Qual o segundo número? "))
#c = a * b
#print(f"O produto é: {c}")

# Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.

#a = int(input("Qual o primeiro número? "))
#b = int(input("Qual o segundo número? "))
#c = a // b
#print(f"A divisão é: {c}")

# Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

#a = int(input("Qual o primeiro número? "))
#c = a ** 2
#print(f"O quadrado é: {c}")


# Números de Ponto Flutuante (float)
# Escreva um programa que receba dois números flutuantes e realize sua adição.

#a = float(input("Qual o primeiro número? "))
#b = float(input("Qual o segundo número? "))
#c = a + b
#print(f"A soma é: {c}")

# Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.

#a = float(input("Qual o primeiro número? "))
#b = float(input("Qual o segundo número? "))
#c = (a + b)/ 2
#print(f"A média é: {c}")

# Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).

#a = float(input("Qual o número? "))
#b = int(input("Qual o expoente? "))
#c = a ** b
#print(f"A potência é: {c}")

# Faça um programa que converta a temperatura de Celsius para Fahrenheit.

#a = float(input("Qual a temperatura em Celsius? "))
#c = (a * 9/5) + 32
#print(f"A temperatura em Fahrenheit é: {c}")

# Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.

#a = float(input("Qual o raio do círculo? "))
#c = 3.14*a**2
#print("A área do círculo é: ", c)

# Strings (str)
# Escreva um programa que receba uma string do usuário e a converta para maiúsculas.

#a = input("Qual a frase? ")
#print(a.upper())

# Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.

#a = input("Qual o seu nome? ")
#print(a.lower())

# Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.

#a = input("Qual a frase? ")
#print(a.strip())

# Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.

#a = input("Qual a data? ")
#
# print(f"O dia é: {a[0:2]}, o mês é: {a[3:5]}, o ano é: {a[6:]}")
 
# Escreva um programa que concatene duas strings fornecidas pelo usuário.

#a = input("Qual o seu nome? ")
#b = input("Qual o seu sobrenome? ")
#print(a + " " + b)

# Booleanos (bool)
# Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.

#a = input("Qual o primeiro valor booleano? ")
#b = input("Qual o segundo valor booleano? ")

#print(a and b)

# Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.

#a = input("Qual o primeiro valor booleano? ").strip().capitalize() == "True"
#b = input("Qual o segundo valor booleano? ").strip().capitalize() == "True"
#
#print(a and b)

# Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.

#a = input("Qual o valor booleano? ").strip().capitalize() == "True"
#print("Valor invertido: ", not a)

# Faça um programa que compare se dois números fornecidos pelo usuário são iguais.

#a = input("Qual o primeiro número? ")
#b = input("Qual o segundo número? ")

#print(a == b)

# Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

#a = input("Qual o primeiro número? ")
#b = input("Qual o segundo número? ")

#print(a != b)

#Escreva um programa que converta a temperatura de Celsius para Fahrenheit. O programa deve solicitar ao usuário a temperatura em Celsius e, utilizando #try-except, garantir que a entrada seja numérica, tratando qualquer ValueError. Imprima o resultado em Fahrenheit ou uma mensagem de erro se a entrada não #for válida.

#try:
#    a = float(input("Qual a temperatura em Celsius? "))
#    c = (a * 9/5) + 32
#    print("A temperatura em Fahrenheit é: ", c)
#except:
#    print("Não é um número.")

#Crie um programa que verifica se uma palavra ou frase é um palíndromo (lê-se igualmente de trás para frente, desconsiderando espaços e pontuações). Utilize #try-except para garantir que a entrada seja uma string. Dica: Utilize a função isinstance() para verificar o tipo da entrada.
#"socorram-me, subi no onibus em marrocos"

#entrada = input("Digite uma palavra ou frase: ")
#if isinstance(entrada, str):
#    formatado = entrada.replace(" ", "").lower()
#    if formatado == formatado[::-1]:
#        print("É um palíndromo.")
#    else:
#        print("Não é um palíndromo.")
#else:
#    print("Entrada inválida. Por favor, digite uma palavra ou frase.")

#Desenvolva uma calculadora simples que aceite duas entradas numéricas e um operador (+, -, *, /) do usuário. Use try-except para lidar com divisões por #zero e entradas não numéricas. Utilize if-elif-else para realizar a operação matemática baseada no operador fornecido. Imprima o resultado ou uma mensagem #de erro apropriada.

#try:
#    a = float(input("Qual o primeiro número? "))
#    b = float(input("Qual o segundo número? "))
#    c = input("Qual a operação? (+, -, *, /)")
#    if c == "+":
#        resultado = a + b
#    elif c == "-":
#        resultado = a - b
#    elif c == "*":
#        resultado = a * b
#    elif c == '/' and b != 0:
#        resultado = a / b
#    else:
#        print("Não é um operador.")
#except: 
#    print("Entrada Inválida.")

#Escreva um programa que solicite ao usuário para digitar um número. Utilize try-except para assegurar que a entrada seja numérica e utilize if-elif-else #para classificar o número como "positivo", "negativo" ou "zero". Adicionalmente, identifique se o número é "par" ou "ímpar".

#try:
#    a = float(input("Qual o número? "))
#    if a > 0 and a % 2 == 0:
#        print("Positivo par")
#    elif a > 0 and a % 2 != 0:
#        print("Positivo ímpar")
#    elif a < 0 and a % 2 != 0:
#        print("Negativo ímpar")
#    elif a < 0 and a % 2 == 0:
#        print("Negativo par")
#    else:
#        print("zero")
#except:
#    print("Não é um número.")


#Crie um script que solicite ao usuário uma lista de números separados por vírgula. O programa deve converter a string de entrada em uma lista de números #inteiros. Utilize try-except para tratar a conversão de cada número e validar que cada elemento da lista convertida é um inteiro. Se a conversão falhar ou #um elemento não for um inteiro, imprima uma mensagem de erro. Se a conversão for bem-sucedida para todos os elementos, imprima a lista de inteiros.

a = input("Qual a lista? ")

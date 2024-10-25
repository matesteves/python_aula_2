#refatorar o exercício da aula 1 para evitar erros

nome = input('Qual seu nome? ')
if any(char.isdigit() for char in nome):
    print("não pode conter números")
elif len(nome.split()) == 0:
    print("o nome não pode estar em branco")
else:
    try:
        salario = float(input('Qual o seu salário? '))
        porcentagem = float(input('Qual o valor da porcentagem de bônus? '))

        bonus = 1000 + (salario * porcentagem)/100

        print("Nome: ", nome, "\nSalário: ", salario, "\nPorcentagem: ", porcentagem, "\nBônus: ", bonus)
    except:
        print('Não é um número.')
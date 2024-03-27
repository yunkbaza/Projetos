def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def multi(x, y):
    return x * y

def div(x, y):
    if y == 0:
        return "Erro: Divisão por 0 não existe"
    return x / y

def calculadora():
    num1 = float(input("Insira o seu primeiro número: "))
    operacao = input("Insira a operação (+, -, *, /): ")
    num2 = float(input("Insira o segundo número: "))

    if operacao == "+":
        resultado = add(num1, num2)
    elif operacao == "-":
        resultado = sub(num1, num2)
    elif operacao == "*":
        resultado = multi(num1, num2)
    elif operacao == "/":
        resultado = div(num1, num2)
    else:
        resultado = "Erro: operação inválida"

    print("O resultado é: " + str(resultado))

if __name__ == '__main__':
    calculadora()



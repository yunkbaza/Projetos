def calcula_taxa():
    
    salario = float(input("Insira o nome do trabalhador: "))

    if salario <= 1903.98:
        taxa = 0
    elif salario <= 2826.65:
        taxa = (salario - 1903.98) * 0.075
    elif salario <= 3751.05:
        taxa = (salario - 2826.66) * 0.15 + 7.5 * 0.075
    elif salario <= 4664.68:
        taxa = (salario - 3751.06) * 0.225 + 35.0 * 0.15 + 10.5 * 0.075
    else:
        taxa = (salario - 4664.69) * 0.275 + 142.5 * 0.225 + 48.5 * 0.15 + 14.5 * 0.075

    print("A taxa gerada por essa renda familiar é de: R$ {:.2f}".format(taxa))

calcula_taxa()


nome_vendedor = input('Insira o nome do vendedor: ')
salario_fixo = float(input('Insira o salário: '))
total_vendas = float(input('Insira o valor do total de vendas: '))


vendas_por_dia = {'Segunda': 0, 'Terca': 0, 'Quarta': 0, 'Quinta': 0, 'Sexta': 0, 'Sabado': 0, 'Domingo': 0}
dias_vendas = ['Segunda', 'Terca', 'Quarta', 'Quinta', 'Sexta', 'Sabado', 'Domingo']
dia_atual = 0
while dia_atual < 7:
    dias_vendas = input(f'Insira as vendas é {dias_vendas[dia_atual]}: ')
    vendas_por_dia[dias_vendas[dia_atual]] = float(dias_vendas)
    dia_atual += 1


comissao = 0
total_comissao = 0
for dia, vendas in vendas_por_dia.items():
    if dia in ['Segunda', 'Terca', 'Quarta']:
        commissao = 0.2
    elif dia in ['Quinta', 'Sexta']:
        commissao = 0.15
    elif dia in ['Sabado', 'Domingo']:
        commissao = 0.1
    else:
        commissao = 0
    total_comissao += vendas * commissao

salario_total = salario_fixo + total_comissao

print(f'O salário total é {nome_vendedor} is ${salario_total:.2f}')
"""
Dado o salário fixo, o valor das vendas efetuadas pelo vendedor de uma empresa e
sabendo-se que ele recebe uma comissão de 3% sobre o total das vendas até R$
1.500,00 e 5% sobre o que ultrapassar este valor, calcular e escrever o seu salário
total.
"""

salario_fixo = float(input('Digite o salário fixo do vendedor: '))
total_vendas = float(input('Digite o valor total das vendas do vendedor: '))

comissao = 0
if total_vendas <= 1500:
    comissao = total_vendas * 0.03
else:
    comissao = (1500 * 0.03) + ((total_vendas - 1500) * 0.05)

salario_total = salario_fixo + comissao
print('O salário total do vendedor será de R$ %.2f' % salario_total)
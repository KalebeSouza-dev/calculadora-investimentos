# Desenvolvido por Kalebe Souza
# Todos os direitos reservados © 2024
# @kalebe_silv

def calculo(valor_inicial, aporte_mensal, juros_anual, periodo):
    # Calculando juros mensais e juros por período
    juros_mensal = (1 + (juros_anual / 100)) ** (1 / 12) - 1
    juros_por_periodo = (1 + juros_mensal) ** periodo

    # Calculando o montante e o valor do aporte
    valorMontante = valor_inicial * juros_por_periodo
    valorAporte = (aporte_mensal / juros_mensal) * (juros_por_periodo - 1)

    # Calculando o valor final, valor dos juros e valor investido
    valorFinal = valorMontante + valorAporte
    valorJuros = valorFinal - (valor_inicial + periodo * aporte_mensal)
    valorInvestido = valorFinal - valorJuros

    # Formatando os resultados
    print('-=-' * 13)
    print(f"{'  Valor Final:':<20} {'R$ ':>5}{valorFinal:>10.2f}")
    print(f"{'  Valor Juros:':<20} {'R$ ':>5}{valorJuros:>10.2f}")
    print(f"{'  Valor Investido:':<20} {'R$ ':>5}{valorInvestido:>10.2f}")
    print('-=-' * 13)

    return

valor_inicial = float(input('Valor Inicial: '))
aporte_mensal = float(input('Aporte Mensal: '))
juros_anual = float(input('Juros Anual: '))
periodo = float(input('Período: '))
calculo(valor_inicial, aporte_mensal, juros_anual, periodo)
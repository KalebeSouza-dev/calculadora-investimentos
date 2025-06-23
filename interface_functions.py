# Desenvolvido por Kalebe Souza
# Todos os direitos reservados © 2024
# @kalebe_silv

import flet as ft

def title(nome):  
    return ft.Column(
        [ft.Text(nome, style=ft.TextStyle(size=48, weight=ft.FontWeight.BOLD))],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

def calculo(input_valor_inicial, input_aporte_mensal, input_juros_anual, input_periodo):
    valor_inicial = float(input_valor_inicial.value)
    aporte_mensal = float(input_aporte_mensal.value)
    juros_anual = float(input_juros_anual.value)
    periodo = int(input_periodo.value)

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
    vF = f"{'Valor Final:':<20} {'R$ ':>5}{valorFinal:>10.2f}"
    vJ = f"{'Valor Juros:':<20} {'R$ ':>5}{valorJuros:>10.2f}"
    vI = f"{'Valor Investido:':<20} {'R$ ':>5}{valorInvestido:>10.2f}"

    return vF, vJ, vI

def resultado(vF, vJ, vI):
    return [
        ft.Text("RESULTADO", style=ft.TextStyle(size=32, weight=ft.FontWeight.BOLD)),
        ft.Divider(),
        ft.Text(vF),
        ft.Text(vJ),
        ft.Text(vI),
        ft.Divider(),
    ]

def focus_next(e, next_input):
        next_input.focus()
    
def pular(a, b, c, d, calcular):
    a.on_submit = lambda e: focus_next(e, b)
    b.on_submit = lambda e: focus_next(e, c)
    c.on_submit = lambda e: focus_next(e, d)
    d.on_submit = lambda e: calcular(e)
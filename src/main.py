# Desenvolvido por Kalebe Souza
# Todos os direitos reservados © 2024
# @kalebe_silv

import flet as ft
from interface_functions import title, calculo, resultado, focus_next, pular

def main(page: ft.Page):
    page.title = "ÁPICE: Calculadora Financeira"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Criando os inputs
    valor_inicial = ft.TextField(label="Valor inicial", keyboard_type="number", autofocus=True)
    aporte_mensal = ft.TextField(label="Aporte mensal", keyboard_type="number")
    juros_anual = ft.TextField(label="Taxa de juros anual (%)", keyboard_type="number")
    periodo = ft.TextField(label="Período em meses", keyboard_type="number")

    # Função para calcular e exibir o resultado
    def calcular(event=None):
        try:
            vF, vJ, vI = calculo(valor_inicial, aporte_mensal, juros_anual, periodo)

            # Limpando e reconfigurando a página
            page.controls.clear()
            page.add(title("ÁPICE"))
            # page.add(imagem_logo)
            page.add(valor_inicial, aporte_mensal, juros_anual, periodo, calcular_button)
            
            # Exibindo o resultado
            page.add(*resultado(vF, vJ, vI))
            page.update()

        except ValueError:
            page.controls.append(ft.Text("Por favor, insira valores válidos nos campos!"))
            page.update()

    # pular inputs
    focus_next
    pular(valor_inicial, aporte_mensal, juros_anual, periodo, calcular)

    calcular_button = ft.ElevatedButton("Calcular", on_click=calcular)

    # Adicionando os elementos iniciais à página
    page.add(title("ÁPICE"))
    # page.add(imagem_logo)
    page.add(valor_inicial, aporte_mensal, juros_anual, periodo, calcular_button)

# Executando o aplicativo
ft.app(target=main)

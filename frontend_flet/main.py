import flet as ft
from pages.carrinhos import carrinhos_view

def main(page: ft.Page):
    page.title = "Sistema de Aluguel de Carrinhos"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Inicializar a tela de carrinhos
    carrinhos_view(page)

ft.app(target=main)

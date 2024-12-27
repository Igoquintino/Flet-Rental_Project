import flet as ft

def main(page: ft.Page):
    page.title = "Teste Flet"
    page.add(ft.Text("Flet está funcionando!"))

ft.app(target=main)

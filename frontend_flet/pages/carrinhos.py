import flet as ft
from services.carrinhos import listar_carrinhos

def carrinhos_view(page: ft.Page):
    # Obter a lista de carrinhos
    carrinhos = listar_carrinhos()

    # Exibir os carrinhos em uma tabela
    if carrinhos:
        page.add(ft.Text("Lista de Carrinhos", size=24))
        table = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("ID")),
                ft.DataColumn(ft.Text("Modelo")),
                ft.DataColumn(ft.Text("Status")),
            ],
            rows=[
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(str(carrinho["id"]))),
                        ft.DataCell(ft.Text(carrinho["nome"])),
                        ft.DataCell(ft.Text(carrinho["estado"])),
                    ]
                )
                for carrinho in carrinhos
            ],
        )
        page.add(table)
    else:
        page.add(ft.Text("Nenhum carrinho encontrado ou erro ao carregar dados.", size=16))

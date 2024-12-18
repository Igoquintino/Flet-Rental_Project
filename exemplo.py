import flet as ft

def main(page: ft.Page):
    # adiciona controlles na pagina
    page.padding = 0
    page.window_width = 400
    page.window_height = 600  
    
    page.controls.append(ft.Text("Hello World"))
    page.update()
    # se quiser, pode usar sem ta colocando .control.apend assim: page.add(ft.Text("insira o texto aqui"))
    

ft.app(port= 8550, target=main)

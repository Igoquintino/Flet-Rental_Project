import flet as ft

def main(page: ft.Page):
    # adiciona controlles na pagina
    page.title = "Falando sobre conteiner"
    page.padding = 50
    page.window_width = 1080
    page.window_height = 720 
    page.controls.append(ft.Text("Hello World"))
    
    
    page.update()
    
    # adicionando conteiner na pagina
    c1 = ft.Container(
        content = ft.ElevatedButton("botão elevado no conteiner"),
        bgcolor= ft.colors.YELLOW,
        padding= 10,
        )
    page.add(c1)
    
    # se quiser, pode usar sem ta colocando .control.apend assim: page.add(ft.Text("insira o texto aqui"))
    # 52, 1,19,40,57,37 números da mega-sena
    
ft.app(target=main)
# ft.app(port= 8550, target=main)

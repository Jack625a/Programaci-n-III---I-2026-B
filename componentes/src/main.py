import flet as ft #paso 1. iMPORTACION


def main(page: ft.Page): #FUNCION PRINCIPAL
    #PASO 2. AGREGAR LA BARRA DE NAVEGACION
    page.bottom_appbar=ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(label="Inicio",icon=ft.Icons.HOME),
            ft.NavigationBarDestination(label="Opcion2",icon=ft.Icons.CATCHING_POKEMON),
            ft.NavigationBarDestination(label="Productos",icon=ft.Icons.SPORTS_SOCCER),
            ft.NavigationBarDestination(label="TikTok",icon=ft.Icons.TIKTOK)
        ],
        bgcolor="blue"
    )
    #Paso 3. CABECERA
    page.appbar=ft.AppBar(title="Aplicacion",bgcolor="blue",center_title=True,color="white")
    
    page.add( #INTERFAZ
        #Imagen
        ft.Image(src="https://preview.redd.it/cutest-starters-of-every-generation-with-gifs-v0-rqjwfhkr3bb71.gif?width=500&auto=webp&s=75f1c25b80dcb8cdd1fb24950aec1c30ed6f2a5c")   
    )
ft.run(main) #EJECUCION

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
        ft.Image(src="https://www.infoworld.com/wp-content/uploads/2025/09/2253770-0-22359500-1757007490-1200px-burmese_python_02-100637340-orig.jpg?quality=50&strip=all&w=1024",
                 width=250)   
    )
ft.run(main) #EJECUCION

import flet as ft #paso 1. iMPORTACION
import flet_video as ftv

def click():
    print("Se hizo click")

def main(page: ft.Page): #FUNCION PRINCIPAL
    #PASO 2. AGREGAR LA BARRA DE NAVEGACION
    page.scroll=ft.ScrollMode.ADAPTIVE
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
        ft.Image(src="https://preview.redd.it/cutest-starters-of-every-generation-with-gifs-v0-rqjwfhkr3bb71.gif?width=500&auto=webp&s=75f1c25b80dcb8cdd1fb24950aec1c30ed6f2a5c", border_radius=ft.BorderRadius(10,10,10,10)),  
        #COMPONENTES DE INTERFAZ
        #Botones
        ft.Button("Prueba",icon=ft.Icons.FACE,color="red",on_click=click),
        ft.ElevatedButton("Prueba2"),
        ft.CupertinoFilledButton("Prueba3",icon=ft.Icons.GPS_FIXED,bgcolor="green"),
        ft.ListView([
            ft.Image(src="https://keepcoding.io/wp-content/smush-webp/2021/09/Java-Logo-1024x576.jpg.webp",height=50),
            ft.Image(src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1280px-Python-logo-notext.svg.png",height=50),
             ],
        scroll=ft.ScrollMode.ADAPTIVE,
        height=150
        ),
        ft.Column(
            controls=[
                        ftv.Video(
                    title="Prueba Video",
                    playlist=[
                        ftv.VideoMedia(resource="https://user-images.githubusercontent.com/28951144/229373720-14d69157-1a56-4a78-a2f4-d7a134d7c3e9.mp4")
                    ],
                    autoplay=True,
                    expand=True
                )
                
            ],
            height=550,
        )
        
        


    )
ft.run(main) #EJECUCION

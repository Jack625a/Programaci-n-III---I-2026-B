import flet as ft
import requests



token=""
idBaseDatos=""
nombreTabla="Persona"

url=f"https://api.airtable.com/v0/{idBaseDatos}/{nombreTabla}"

headers={
    "Authorization":f"Bearer {token}"
}

respuesta=requests.get(url,headers=headers)



def main(page: ft.Page):
    page.appbar=ft.AppBar(title="Trabajo Final")

    page.bottom_appbar=ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(label="Opcion1",icon=ft.Icons.TIKTOK),
            ft.NavigationBarDestination(label="Opcion2",icon=ft.Icons.FACE),
            ft.NavigationBarDestination(label="Opcion3",icon=ft.Icons.GPS_NOT_FIXED),
            ft.NavigationBarDestination(label="Opcion4",icon=ft.Icons.PERM_CAMERA_MIC)
        ]
    )

    
    page.add(
        ft.Image(src="https://cei.es/wp-content/uploads/python-detalle.png")
        
    )


ft.run(main)

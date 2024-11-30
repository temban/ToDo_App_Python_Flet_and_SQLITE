import flet as ft


def create_sidebar(page):
    return ft.Container(
        content=ft.Column(
            controls=[
                ft.IconButton(
                    icon=ft.icons.HOME,
                    icon_size=40,
                    icon_color="white",
                    on_click=lambda e: page.go("/"),  # Navigate to home page
                ),
                ft.IconButton(
                    icon=ft.icons.VIEW_LIST,
                    icon_size=40,
                    icon_color="white",
                    on_click=lambda e: page.go("/tasks"),  # Navigate to tasks page
                ),
                ft.IconButton(
                    icon=ft.icons.SETTINGS,
                    icon_size=40,
                    icon_color="white",
                    on_click=lambda e: page.go("/settings"),  # Navigate to settings page
                ),
            ],
            spacing=30,
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        bgcolor=ft.colors.DEEP_PURPLE,
        width=80,
        height=page.height,
        padding=ft.padding.all(10),
    )

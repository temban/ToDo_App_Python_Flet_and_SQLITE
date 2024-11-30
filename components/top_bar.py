import flet as ft


def create_top_bar(page):
    def on_backward_button_click(e):
        print("Backward button clicked")

    def on_forward_button_click(e):
        print("Forward button clicked")

    return ft.Row(
        controls=[
            ft.Column(
                controls=[
                    ft.Text("18 November 2024", size=20, weight=ft.FontWeight.BOLD),
                    ft.Text("Sunday", size=16),
                ],
                alignment=ft.CrossAxisAlignment.CENTER,
                spacing=4,
            ),
            ft.Container(
                content=ft.IconButton(ft.icons.ARROW_BACK, on_click=on_backward_button_click),
                width=40,
                height=40,
                bgcolor="grey",
                border_radius=5,
                margin=ft.margin.only(left=850),
            ),
            ft.Container(
                content=ft.IconButton(ft.icons.ARROW_FORWARD, on_click=on_forward_button_click),
                width=40,
                height=40,
                bgcolor="grey",
                border_radius=5,
            ),
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        height=50,
    )

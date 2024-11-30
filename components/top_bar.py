import flet as ft
import datetime


def create_top_bar(page, selected_day=None):
    def on_backward_button_click(e):
        print("Backward button clicked")

    def on_forward_button_click(e):
        print("Forward button clicked")

    # If selected_day is not provided, set it to today's date
    if not selected_day:
        selected_day = datetime.datetime.today().strftime("%Y-%m-%d")

    # Convert selected_day to a datetime object
    today = datetime.datetime.strptime(selected_day, "%Y-%m-%d")

    # Format the date and day of the week
    date_str = today.strftime("%d %B %Y")  # Format as "18 November 2024"
    day_of_week = today.strftime("%A")  # Format as "Sunday"

    return ft.Row(
        controls=[
            ft.Column(
                controls=[
                    ft.Text(date_str, size=20, weight=ft.FontWeight.BOLD),
                    ft.Text(day_of_week, size=16),
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

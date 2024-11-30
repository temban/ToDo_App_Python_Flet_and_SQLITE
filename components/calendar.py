import flet as ft
from utils.task_helpers import update_tasks_for_selected_day


def create_calendar_row(page, selected_day):
    def create_date_box(date, label, selected_day):
        is_selected = date == selected_day
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text(label, size=14),
                    ft.Text(date, size=14),
                ],
                alignment=ft.CrossAxisAlignment.CENTER,
            ),
            bgcolor=ft.colors.LIGHT_BLUE if is_selected else ft.colors.WHITE,
            width=100,
            height=250,
            margin=ft.margin.only(top=20),
            padding=ft.padding.only(left=30, top=7, bottom=5, right=30),
            on_click=lambda e: on_date_selected(date),
        )

    def on_date_selected(selected_date):
        nonlocal selected_day
        selected_day = selected_date
        page.update()

    return ft.Row(
        controls=[
            create_date_box("30", "SUN", selected_day),
            create_date_box("31", "MON", selected_day),
            create_date_box("1", "TUE", selected_day),
            create_date_box("2", "WED", selected_day),
            create_date_box("3", "THU", selected_day),
            create_date_box("4", "FRI", selected_day),
            create_date_box("5", "SAT", selected_day),
        ],
        alignment=ft.MainAxisAlignment.SPACE_AROUND,
        height=80,
    )

import flet as ft
from utils.task_helpers import update_tasks_for_selected_day

def create_task_section(page, selected_day):
    return ft.Container(
        content=ft.ListView(
            controls=[
                ft.Text("Task of today", size=18, weight=ft.FontWeight.BOLD),
                *update_tasks_for_selected_day(selected_day, page),  # Pass both selected_day and page
            ],
            spacing=10,
            expand=True,
        ),
        padding=ft.padding.only(left=20, right=50),
        height=400,
    )

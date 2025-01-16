import flet as ft
from utils.database import get_all_tasks



def update_tasks_for_selected_day(day, page):  # Pass page as an argument
    from components.dialogs import handle_update_task_dialog
    def create_task_row(time, task_id, task_name, deadline, note):
        u_dlg_modal = ft.AlertDialog()

        return ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Row(controls=[ft.Text(time, size=16, width=200)]),
                        ft.Container(
                            content=ft.Row(
                                controls=[ft.Checkbox(label=task_name, width=250)],
                                alignment=ft.MainAxisAlignment.START,
                            ),
                            width=350,
                            margin=ft.margin.only(right=300),
                        ),
                        ft.Row(
                            controls=[
                                ft.Icon(ft.icons.CIRCLE, color="yellow", size=16),
                                ft.Icon(ft.icons.CIRCLE, color="red", size=16),
                                ft.IconButton(
                                    icon=ft.icons.EDIT,
                                    tooltip="Edit Task",
                                    on_click=lambda e: handle_update_task_dialog(
                                        page, u_dlg_modal, task_id, task_name, deadline, note
                                    ),
                                ),
                            ],
                            spacing=5,
                            alignment=ft.MainAxisAlignment.END,
                            width=80,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    height=50,
                ),
                ft.Divider(height=1, color="grey"),
            ]
        )

    tasks = get_all_tasks()  # Fetch tasks from the database

    task_rows = []
    for task in tasks:
        task_id = task[0]  # ID
        task_name = task[1]  # Label
        task_deadline = task[2]  # Deadline
        task_note = task[3]  # Note
        task_rows.append(create_task_row(task_deadline, task_id, task_name, task_deadline, task_note))

    return task_rows

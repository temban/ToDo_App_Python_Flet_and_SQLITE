import flet as ft
from utils.database import get_all_tasks
from components.dialogs import handle_update_task_dialog


def update_tasks_for_selected_day(day, page):  # Pass page as an argument
    def create_task_row(time, task_name):
        u_dlg_modal = ft.AlertDialog()

        # Create the task row with a margin on the left side for Text and Checkbox
        return ft.Column(
            controls=[
                ft.Row(
                    controls=[

                        ft.Row(controls=[ft.Text(time, size=16, width=200)]),

                        # Left section (Text and Checkbox wrapped in a Container with margin)
                        ft.Container(
                            content=ft.Row(
                                controls=[
                                    ft.Checkbox(label=task_name, width=250),
                                ],
                                alignment=ft.MainAxisAlignment.START,  # Align content in the Row
                            ),
                            width=350,
                            margin=ft.margin.only(right=300),  # Apply margin to the left section container
                        ),

                        # Right section (Icons for status and edit button)
                        ft.Row(
                            controls=[
                                ft.Icon(ft.icons.CIRCLE, color="yellow", size=16),
                                ft.Icon(ft.icons.CIRCLE, color="red", size=16),
                                ft.IconButton(
                                    icon=ft.icons.EDIT,  # Edit icon for update functionality
                                    tooltip="Edit Task",  # Tooltip for the button
                                    on_click=lambda e: handle_update_task_dialog(page, u_dlg_modal, e),
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
                # ft.margin.only(bottom=200)
            ]
        )

    tasks = get_all_tasks()  # Fetch tasks from the database

    task_rows = []
    for task in tasks:
        task_name = task[1]
        task_time = task[2]  # For example, you can modify this based on task data
        task_rows.append(create_task_row(task_time, task_name))

    return task_rows

import flet as ft
from utils.database import insert_task, get_all_tasks  # Import the required functions

def handle_add_task_dialog(page, dlg_modal, e):
    # Create fields to input task details
    label_field = ft.TextField(label="Label of Task", width=300)
    deadline_field = ft.TextField(label="Date of Deadline", width=300)
    note_field = ft.TextField(label="Note", width=300)

    # Define the function to save the task
    def save_task(e):
        label = label_field.value
        deadline = deadline_field.value
        note = note_field.value

        # Insert the task into the database using the insert_task function
        insert_task(label, deadline, note)

        # Fetch updated tasks and update the UI immediately after saving the task
        tasks = get_all_tasks()

        # Clear the current task list container (if any) and re-render the list
        task_items = []
        for task in tasks:
            task_items.append(ft.Text(f"Task: {task[1]}, Deadline: {task[2]}, Note: {task[3]}"))

        # Assuming you have a task container (e.g., task_list) to hold the task items
        task_list_container = ft.Column(task_items)  # This assumes you have a Column or another container for tasks
        page.controls.append(task_list_container)  # Add the updated task list to the page
        page.update()  # Update the page to reflect changes

        # Close the dialog after saving the task
        handle_close(page, None, dlg_modal, e)

    left_section = ft.Container(
        content=ft.Column(
            [
                ft.Text(size=30, color=ft.colors.WHITE),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        bgcolor=ft.colors.BLUE_600,
        width=300,
        height=400,
    )

    right_section = ft.Container(
        content=ft.Column(
            [
                ft.Row(
                    [
                        ft.Container(
                            content=ft.IconButton(
                                icon=ft.icons.CLOSE,
                                icon_size=30,
                                on_click=lambda e: handle_close(page, None, dlg_modal, e),
                                bgcolor=ft.colors.TRANSPARENT,
                            ),
                            padding=ft.padding.only(right=10, bottom=10, top=10),
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.END,
                ),
                ft.Text("NEW TASK", size=24, weight="bold", text_align="center"),
                label_field,
                deadline_field,
                note_field,
                ft.ElevatedButton("Save", bgcolor=ft.colors.BLUE_600, color=ft.colors.WHITE, width=100, height=40, on_click=save_task),
            ],
            alignment=ft.MainAxisAlignment.START,
            spacing=15,
        ),
        bgcolor=ft.colors.WHITE,
        width=500,
        height=400,
        padding=ft.padding.only(left=80),
    )

    # Dialog content to display
    dlg_modal.content = ft.Row(
        [left_section, right_section],
        alignment=ft.MainAxisAlignment.START,
    )
    # Open the dialog on the page
    page.open(dlg_modal)

def handle_close(page, u_dlg_modal, dlg_modal, e):
    if dlg_modal:  # Check if dlg_modal is not None
        page.close(dlg_modal)  # Close the add task dialog
    if u_dlg_modal:  # Check if u_dlg_modal is not None
        page.close(u_dlg_modal)  # Close the update task dialog
    page.add(ft.Text(f"Modal dialog closed with action: {e.control.text}"))


def handle_update_task_dialog(page, u_dlg_modal, e):
    update_left_section = ft.Container(
        content=ft.Column(
            [
                ft.Text(size=30, color=ft.colors.WHITE),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        bgcolor=ft.colors.YELLOW,
        width=300,
        height=400,
    )
    update_right_section = ft.Container(
        content=ft.Column([
            ft.Row(
                [
                    ft.Container(
                        content=ft.IconButton(
                            icon=ft.icons.CLOSE,
                            icon_size=30,
                            on_click=lambda e: handle_close(page, u_dlg_modal, None, e),
                            bgcolor=ft.colors.TRANSPARENT,
                        ),
                        padding=ft.padding.only(right=10, bottom=10, top=10),
                    ),
                ],
                alignment=ft.MainAxisAlignment.END,
            ),
            ft.Text("UPDATE TASK", size=24, weight="bold", text_align="center"),
            ft.TextField(label="Label of Task", width=300),
            ft.TextField(label="Date of Deadline", width=300),
            ft.TextField(label="Note", width=300),
            ft.ElevatedButton("Update", bgcolor=ft.colors.YELLOW, color=ft.colors.WHITE, width=100, height=40),
        ],
            alignment=ft.MainAxisAlignment.START, spacing=15),
        bgcolor=ft.colors.WHITE,
        width=500,
        height=400,
        padding=ft.padding.only(left=80),
        # margin=ft.margin.only(top=160),
    )
    u_dlg_modal.content = ft.Row(
        [update_left_section, update_right_section],
        alignment=ft.MainAxisAlignment.START,
    )
    u_dlg_modal.on_dismiss = lambda e: page.add(ft.Text("Modal dialog dismissed"))

    page.open(u_dlg_modal)

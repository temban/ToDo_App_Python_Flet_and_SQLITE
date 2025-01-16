import flet as ft

from components.calendar import create_calendar_row
from components.sidebar import create_sidebar
from components.task_list import create_task_section
from components.top_bar import create_top_bar
from utils.database import insert_task, get_all_tasks, update_task_in_db  # Import the required functions
from utils.task_helpers import update_tasks_for_selected_day


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


def handle_update_task_dialog(page, u_dlg_modal, task_id, label, deadline, note):
    # Create TextFields preloaded with the task's information
    label_field = ft.TextField(label="Label of Task", width=300, value=label)
    deadline_field = ft.TextField(label="Date of Deadline", width=300, value=deadline)
    note_field = ft.TextField(label="Note", width=300, value=note)

    # Update button handler
    def update_task(e):
        updated_label = label_field.value
        updated_deadline = deadline_field.value
        updated_note = note_field.value

        # Call database update function
        update_task_in_db(task_id, updated_label, updated_deadline, updated_note)

        # Show snackbar notification
        page.snack_bar = ft.SnackBar(
            content=ft.Text("Task updated successfully"),
            duration=7000,
        )
        page.snack_bar.open = True
        page.update()  # Refresh the page to reflect the changes

        # Refresh task section after updating
        selected_day = "30"  # Use the selected day as needed
        task_section = create_task_section(page, selected_day)
        page.controls.clear()
        sidebar = create_sidebar(page)
        top_bar = create_top_bar(page)
        calendar_row = create_calendar_row(page, selected_day)

        main_content = ft.Container(
            content=ft.Column(
                controls=[
                    top_bar,
                    calendar_row,
                    task_section,  # Newly generated task section
                ],
                alignment=ft.MainAxisAlignment.START,
            ),
            padding=ft.padding.all(20),
            width=page.width - 80,
        )

        page.add(
            ft.Row(
                controls=[
                    sidebar,
                    main_content,
                ],
            )
        )
        page.update()  # Refresh the page to reflect the updated task section

        # Close the dialog
        handle_close(page, u_dlg_modal, None, e)

    # Left section
    update_left_section = ft.Container(
        content=ft.Column(
            [ft.Text(size=30, color=ft.colors.WHITE)],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        bgcolor=ft.colors.YELLOW,
        width=300,
        height=400,
    )

    # Right section
    update_right_section = ft.Container(
        content=ft.Column(
            [
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
                label_field,
                deadline_field,
                note_field,
                ft.ElevatedButton("Update", bgcolor=ft.colors.YELLOW, color=ft.colors.WHITE, width=100, height=40, on_click=update_task),
            ],
            alignment=ft.MainAxisAlignment.START,
            spacing=15,
        ),
        bgcolor=ft.colors.WHITE,
        width=500,
        height=400,
        padding=ft.padding.only(left=80),
    )

    # Set modal content
    u_dlg_modal.content = ft.Row(
        [update_left_section, update_right_section],
        alignment=ft.MainAxisAlignment.START,
    )
    page.open(u_dlg_modal)

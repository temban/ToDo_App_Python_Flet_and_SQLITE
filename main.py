import flet as ft
from components.calendar import create_calendar_row
from components.sidebar import create_sidebar
from components.top_bar import create_top_bar
from components.dialogs import handle_add_task_dialog, handle_update_task_dialog
from components.task_list import create_task_section
from components.settings import Settings
import auth  # Import the authentication module

def main(page: ft.Page):
    page.title = "Task Scheduler"
    page.padding = 0
    page.theme_mode = ft.ThemeMode.LIGHT

    current_user_id = None  # Track the current logged-in user

    # Callback to handle successful login
    def on_login_success(user_id):
        nonlocal current_user_id
        current_user_id = user_id
        render_home_page()

    # Render the Home Page
    def render_home_page():
        if current_user_id is None:
            # If user is not logged in, show the auth page
            auth.show_auth_page(page, on_login_success)
            return  # Stop further execution

        page.controls.clear()

        selected_day = "30"  # Use the current selected day or dynamically update this
        sidebar = create_sidebar(page)
        top_bar = create_top_bar(page)
        calendar_row = create_calendar_row(page, selected_day)

        # Add a function to reload the task section after a task update
        def reload_task_section():
            # Reload the task section for the selected day
            task_section = create_task_section(page, selected_day)
            main_content.controls[3] = task_section  # Update the task section
            page.update()  # Refresh the page to reflect the changes

        # Pass `reload_task_section` to update tasks in the dialog
        dlg_modal = ft.AlertDialog()

        add_task_button = ft.Container(
            content=ft.FloatingActionButton(
                content=ft.Text("+"),
                bgcolor="blue",
                on_click=lambda e: handle_add_task_dialog(page, dlg_modal, e),
            ),
            alignment=ft.alignment.center,
            width=400,
            height=100,
            margin=ft.margin.only(top=20, left=1000),
        )

        main_content = ft.Container(
            content=ft.Column(
                controls=[
                    top_bar,
                    calendar_row,
                    add_task_button,
                    create_task_section(page, selected_day),
                ],
                alignment=ft.MainAxisAlignment.START,
            ),
            padding=ft.padding.all(20),
            width=page.width - 80,
        )

        page.add(
            ft.Row(
                controls=[sidebar, main_content],
            )
        )

        # Update the dialog to handle task updates with the reload callback
        def handle_task_update_dialog(task_id, label, deadline, note):
            handle_update_task_dialog(page, dlg_modal, task_id, label, deadline, note, reload_task_section)

        # For handling task updates (you can implement a button or action that calls handle_task_update_dialog)
        # Example: handle_task_update_dialog(task_id, label, deadline, note)

        page.update()

    # Render the Settings Page
    def render_settings_page():
        page.controls.clear()
        sidebar = create_sidebar(page)
        settings_layout = Settings(page).build()
        page.add(ft.Row(controls=[sidebar, settings_layout]))
        page.update()

    # Route Change Handler
    def route_change(event):
        if event.route == "/":
            render_home_page()
        elif event.route == "/settings":
            render_settings_page()
        elif event.route == "/login":  # Handle the login route
            auth.show_auth_page(page, on_login_success)  # Display the login page
        else:
            page.controls.clear()
            page.add(ft.Text("Page not found", size=30, color="red"))
            page.update()

    # Assign route handler
    page.on_route_change = route_change

    # Force navigation to the login page first
    page.go("/login")  # This should trigger the login page route

ft.app(target=main)

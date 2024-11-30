import flet as ft
import sqlite3
import bcrypt


# Database setup
def setup_database():
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            email TEXT NOT NULL,
            phone_number TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()


setup_database()


# User Authentication Functions
def register_user(username, password, email, phone_number):
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    try:
        cursor.execute("INSERT INTO users (username, password, email, phone_number) VALUES (?, ?, ?, ?)",
                       (username, hashed_password, email, phone_number))
        conn.commit()
        conn.close()
        return True
    except sqlite3.IntegrityError:
        conn.close()
        return False


def login_user(username, password):
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    conn.close()
    if user and bcrypt.checkpw(password.encode('utf-8'), user[2]):
        return user[0]  # Return user ID
    return None


# Auth Page
def show_auth_page(page: ft.Page, on_login_success):
    page.clean()
    page.title = "Login/Register"

    def show_login():
        page.clean()

        # Create the form fields and buttons
        username_field = ft.TextField(label="Username", width=300)
        password_field = ft.TextField(label="Password", password=True, width=300)
        error_message = ft.Text(color=ft.colors.RED)

        # "Remember Me" Checkbox
        remember_me_checkbox = ft.Checkbox(label="Remember Me", value=False)

        # "Don't have an account?" Button
        register_button = ft.TextButton("Don't have an account?", on_click=lambda e: show_register())

        # Handle login button click
        def handle_login(e):
            user_id = login_user(username_field.value, password_field.value)
            if user_id:
                on_login_success(user_id)  # Pass user ID back to main page
            else:
                error_message.value = "Invalid username or password"
                page.update()

        login_button = ft.Column(
            [
                ft.Container(
                    content=ft.ElevatedButton(
                        text="Login",
                        bgcolor=ft.colors.BLUE,
                        height=50,
                        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5)),
                        on_click=handle_login
                    ),
                    width=300,
                ),
            ],
            spacing=10,
        )

        # Row layout for the checkbox and register button on the same line
        bottom_row = ft.Row(
            [remember_me_checkbox, register_button],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=10  # Adjust the space between them
        )

        # Centralized form layout using Container for centering
        form_column = ft.Column([
            ft.Text("Login", size=30, weight=ft.FontWeight.BOLD),
            username_field,
            password_field,
            bottom_row,  # Add the Row for checkbox and register button
            login_button,
            error_message
        ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER)

        # Use Container to center the form_column
        page.add(
            ft.Container(
                content=form_column,
                alignment=ft.alignment.center,  # Center the content
                width=page.width,
                height=page.height,
                padding=ft.padding.all(20)
            )
        )
        page.update()

    def show_register():
        page.clean()

        # Create the form fields for registration
        username_field = ft.TextField(label="Username", width=300)
        password_field = ft.TextField(label="Password", password=True, width=300)
        email_field = ft.TextField(label="Email", width=300)
        phone_field = ft.TextField(label="Phone Number", width=300)
        error_message = ft.Text(color=ft.colors.RED)

        def handle_register(e):
            # Register the user with username, password, email, and phone number
            if register_user(username_field.value, password_field.value, email_field.value, phone_field.value):
                show_login()
            else:
                error_message.value = "Username already exists"
                page.update()

        login_button = ft.TextButton("Already have an account!", on_click=lambda e: show_login())
        register_button = ft.Column(
            [
                ft.Container(
                    content=ft.ElevatedButton(
                        text="Register",
                        bgcolor=ft.colors.BLUE,
                        height=50,
                        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5)),
                        on_click=handle_register
                    ),
                    width=300,
                ),
            ],
            spacing=10,
        )

        # Centralized form layout with button alignment beneath fields
        form_column = ft.Column([
            ft.Text("Register", size=30, weight=ft.FontWeight.BOLD),
            username_field,
            password_field,
            email_field,
            phone_field,
            login_button,
            register_button,
            error_message
        ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER)

        # Use Container to center the form_column
        page.add(
            ft.Container(
                content=form_column,
                alignment=ft.alignment.center,  # Center the content
                width=page.width,
                height=page.height,
                padding=ft.padding.all(20)
            )
        )
        page.update()

    show_login()

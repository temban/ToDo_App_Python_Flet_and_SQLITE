import flet as ft


class Settings:
    def __init__(self, page: ft.Page):
        self.page = page

    def build(self):
        # Export section
        export_section = ft.Column(
            [
                ft.Text("Export", style="titleMedium"),
                ft.Container(
                    content=ft.ElevatedButton(
                        text="Export to JSON",
                        bgcolor=ft.colors.YELLOW,
                        color=ft.colors.BLACK,
                        height=50,
                        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5)),
                    ),
                    width=250,
                ),
            ],
            spacing=10,
        )

        # Mail section
        mail_section = ft.Column(
            [
                ft.Text("Mail gestion", style="titleMedium"),
                ft.Container(
                    content=ft.ElevatedButton(
                        text="Send mail",
                        bgcolor=ft.colors.BLUE,
                        height=50,
                        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5)),
                    ),
                    width=250,
                ),
            ],
            spacing=10,
        )

        # Other section
        other_section = ft.Column(
            [
                ft.Text("Other option", style="titleMedium"),
                ft.Container(
                    content=ft.ElevatedButton(
                        text="Send mail",
                        bgcolor=ft.colors.GREY_300,
                        height=50,
                        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5)),
                    ),
                    width=250,
                ),
            ],
            spacing=10,
        )

        # Reset section
        reset_section = ft.Column(
            [
                ft.Text("Reset option", style="titleMedium"),
                ft.Container(
                    content=ft.ElevatedButton(
                        text="Destroy all data of account",
                        bgcolor=ft.colors.RED,
                        height=50,
                        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5)),
                    ),
                    width=250,
                ),
            ],
            spacing=10,
        )

        # Left options layout with vertical divider
        left_options = ft.Container(
            content=ft.Column(
                [
                    export_section,
                    mail_section,
                    ft.VerticalDivider(width=2, color=ft.colors.BLUE),  # Divider inside the left section
                    other_section,
                    reset_section,
                ],
                spacing=20,
            ),
            expand=True,
            padding=10,
            margin=ft.margin.only(left=80),  # Add left margin to left options section
        )

        # Right column - Personal Data
        personal_data = ft.Container(
            content=ft.Column(
                [
                    ft.Text("Personal Data", style="headlineSmall"),
                    ft.Text("and Other options", size=12),
                    ft.TextField(label="Name", value="Ryan"),
                    ft.TextField(label="Password", password=True, value="********"),
                    ft.TextField(label="Email", value=".......@gmail.com"),
                    ft.Container(
                        content=ft.ElevatedButton(
                            text="Save",
                            bgcolor=ft.colors.BLUE,
                            height=50,
                            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5)),
                        ),
                        width=120,
                    ),
                ],
                spacing=15,
            ),
            expand=True,
            padding=10,
            margin=ft.margin.only(right=100),  # Add right margin to personal data section
        )

        # Main layout
        return ft.Row(
            controls=[
                left_options,
                ft.Divider(height=1, color="grey"),
                personal_data,
            ],
            alignment=ft.MainAxisAlignment.START,
            expand=True,
        )

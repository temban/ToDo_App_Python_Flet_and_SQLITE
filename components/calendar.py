import flet as ft
import datetime


def create_calendar_row(page, selected_day=None, on_date_selected=None):
    # If selected_day is not provided or is in an invalid format, set it to today's date
    if not selected_day:
        selected_day = datetime.datetime.today().strftime("%Y-%m-%d")

    # If selected_day is just a day (e.g., '30'), we assume it's in the current month and year
    if len(selected_day) == 2 and selected_day.isdigit():
        today = datetime.datetime.today()
        selected_day = f"{today.year}-{today.month:02d}-{selected_day}"

    # Convert selected_day to datetime object
    today = datetime.datetime.strptime(selected_day, "%Y-%m-%d")

    # Calculate the start of the week (Sunday) and the days for the current week
    start_of_week = today - datetime.timedelta(days=today.weekday() + 1)  # Adjust to get the Sunday of the current week
    week_dates = [start_of_week + datetime.timedelta(days=i) for i in range(7)]  # List of dates for the week

    def create_date_box(date, label):
        is_selected = date.date() == today.date()  # Check if the date is today
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text(label, size=14),
                    ft.Text(str(date.day), size=14),  # Show day of the month
                ],
                alignment=ft.CrossAxisAlignment.CENTER,
            ),
            bgcolor=ft.colors.LIGHT_BLUE if is_selected else ft.colors.WHITE,
            width=100,
            height=250,
            margin=ft.margin.only(top=20),
            padding=ft.padding.only(left=30, top=7, bottom=5, right=30),
            on_click=lambda e: on_date_selected(date),  # Pass the selected date to the callback
        )

    # Create a row of date boxes for the week
    return ft.Row(
        controls=[
            create_date_box(week_dates[0], "SUN"),
            create_date_box(week_dates[1], "MON"),
            create_date_box(week_dates[2], "TUE"),
            create_date_box(week_dates[3], "WED"),
            create_date_box(week_dates[4], "THU"),
            create_date_box(week_dates[5], "FRI"),
            create_date_box(week_dates[6], "SAT"),
        ],
        alignment=ft.MainAxisAlignment.SPACE_AROUND,
        height=80,
    )

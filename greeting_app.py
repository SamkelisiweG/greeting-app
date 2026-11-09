import flet as ft


def main(page: ft.Page):
    page.title = "Greeting App"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Controls stored in variables so the handler can read/change them
    name_field = ft.TextField(label="Enter your name", width=300)
    greeting = ft.Text("", size=24, weight=ft.FontWeight.BOLD)

    def greet_click(e):
        greeting.value = f"Hello, {name_field.value}!"
        page.update()

    greet_button = ft.Button("Greet Me", on_click=greet_click)

    page.add(
        ft.Column(
            [name_field, greet_button, greeting],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )


ft.run(main)

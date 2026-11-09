
import flet as ft


def main(page: ft.Page):

    page.title = "Greeting App"

    # TextField for entering the user's name
    name_field = ft.TextField(
        label="Enter your name",
        hint_text="Type your name here"
    )

    # Text control to display the greeting
    greeting_text = ft.Text(
        "",
        size=20
    )

    # Button click function
    def greet_me(e):
        name = name_field.value.strip()

        if name:
            greeting_text.value = f"Hello, {name}!"
        else:
            greeting_text.value = "Please enter your name."

        page.update()

    # Greet Me button
    greet_button = ft.ElevatedButton(
        text="Greet Me",
        on_click=greet_me
    )

    # Arrange controls vertically
    page.add(
        ft.Column(
            controls=[
                ft.Text("Welcome to the Greeting App", size=25),
                name_field,
                greet_button,
                greeting_text
            ]
        )
    )


ft.run(main)

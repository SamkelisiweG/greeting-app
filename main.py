
import flet as ft


def main(page: ft.Page):
    page.title = "Greeting App"

    # Store the user's name
    name = ""

    # Home screen name field
    name_field = ft.TextField(
        label="Enter your name",
        hint_text="Your name"
    )

    # Continue button function
    async def continue_click(e):
        nonlocal name

        name = name_field.value.strip()

        if not name:
            dialog = ft.AlertDialog(
                title=ft.Text("Missing Name"),
                content=ft.Text("Please enter your name.")
            )
            page.show_dialog(dialog)
        else:
            await page.push_route("/greeting")

    # Back button function
    async def back_click(e):
        await page.push_route("/")

    # Display the correct screen
    def route_change(e):
        page.views.clear()

        if page.route == "/":
            page.views.append(
                ft.View(
                    route="/",
                    controls=[
                        ft.Text(
                            "Welcome to the Greeting App",
                            size=25,
                            weight=ft.FontWeight.BOLD
                        ),
                        name_field,
                        ft.Button(
                            "Continue",
                            on_click=continue_click
                        )
                    ],
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                )
            )

        elif page.route == "/greeting":
            page.views.append(
                ft.View(
                    route="/greeting",
                    controls=[
                        ft.Text(
                            f"Hello, {name}!",
                            size=30,
                            weight=ft.FontWeight.BOLD
                        ),
                        ft.Button(
                            "Back",
                            on_click=back_click
                        )
                    ],
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                )
            )

        page.update()

    page.on_route_change = route_change

    # Show the home screen first
    route_change(None)


ft.run(main)

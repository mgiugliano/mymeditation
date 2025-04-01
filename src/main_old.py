import flet as ft


def main(page: ft.Page):
    counter = ft.Text("0", size=50, data=0)

    def increment_click(e):
        counter.data += 1
        counter.value = str(counter.data)
        counter.update()

    def decrement_click(e):
        counter.data -= 1
        counter.value = str(counter.data)
        counter.update()


    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.Icons.ADD, on_click=increment_click
    )

    # Let's add a second floating action button to decrement the counter
    page.floating_action_button1 = ft.FloatingActionButton(
        icon=ft.Icons.ADD, on_click=decrement_click
    )


    page.floating_action_button1.tooltip = "Decrement"
    page.floating_action_button.tooltip = "Increment"

    # Set the page title
    page.title = "Counter App"

    # Set the page size
    #page.window_width = 400
    #page.window_height = 300

    # Set the page background color
    #page.window_bgcolor = ft.colors.BLUE_50
    # Set the page icon
    page.window_icon = "https://flet.dev/favicon.png"
    # Set the page font
    page.fonts = {
        "Roboto": "https://fonts.googleapis.com/css2?family=Roboto:wght@400&display=swap"
    }

    page.add(
        ft.SafeArea(
            ft.Container(
                counter,
                alignment=ft.alignment.center,
            ),
            expand=True,
        )
    )


ft.app(main)

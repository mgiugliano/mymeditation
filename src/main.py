import flet as ft
import flet_audio as fta

import time
import os

app_data_path = os.getenv("FLET_APP_STORAGE_DATA")


from flet import (
    ElevatedButton,
    FilePicker,
    FilePickerResultEvent,
    ProgressRing,
    Page,
    Column,
    Row,
    Text,
    icons,
)


# Let's create an app that implements a count-down timer of 10 seconds
# The timer will start when the user clicks the "Start" button. And it will
# play a sound when the timer reaches 0.

def main(page: ft.Page):
    page.title = "Countdown Timer"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER

    # Create a Text widget to display the countdown
    countdown_text = ft.Text("3", size=200, color=ft.colors.RED)

    # Create a button to start the countdown
    start_button = ft.ElevatedButton("Start", on_click=lambda e: start_countdown())

    # Create a sound object to play when the countdown reaches 0
    #sound = ft.Sound(src="https://www.soundjay.com/button/beep-07.wav")

    my_sound_path = os.path.join(app_data_path, "bell-a-99888.mp3")

    sound = fta.Audio(src = my_sound_path, volume=1.0, autoplay=False)
    page.overlay.append(sound)

    def start_countdown():
        # Disable the button to prevent multiple clicks
        start_button.disabled = True
        page.update()

        # Start the countdown from 10 to 0
        for i in range(3, -1, -1):
            pr.value = i / 3.
            countdown_text.value = str(i)
            page.update()
            if i == 0:
                #countdown_text.color = ft.colors.GREEN
                sound.play()
                #sound.play()
            time.sleep(1)

        # Enable the button again after the countdown
        start_button.disabled = False
        page.update()


    pr = ProgressRing(width=160, height=160, stroke_width=20)

    page.add(
        #Text("Circular progress indicator", style="headlineSmall"),
        #Row([pr, Text("Wait for the completion...")]),
        Row([pr]),
        )



    # Add the widgets to the page
    page.add(countdown_text, start_button)


    # Pick files dialog
    def pick_files_result(e: FilePickerResultEvent):
        selected_files.value = (
            ", ".join(map(lambda f: f.name, e.files)) if e.files else "Cancelled!"
        )
        selected_files.update()

    pick_files_dialog = FilePicker(on_result=pick_files_result)
    selected_files = Text()

    # Save file dialog
#    def save_file_result(e: FilePickerResultEvent):
#        save_file_path.value = e.path if e.path else "Cancelled!"
#        save_file_path.update()
#
#    save_file_dialog = FilePicker(on_result=save_file_result)
#    save_file_path = Text()
#
#    # Open directory dialog
#    def get_directory_result(e: FilePickerResultEvent):
#        directory_path.value = e.path if e.path else "Cancelled!"
#        directory_path.update()
#
#    get_directory_dialog = FilePicker(on_result=get_directory_result)
#    directory_path = Text()

    # hide all dialogs in overlay
#    page.overlay.extend([pick_files_dialog, save_file_dialog, get_directory_dialog])
    page.overlay.extend([pick_files_dialog])

    page.add(
        Row(
            [
                ElevatedButton(
                    "Pick files",
                    icon=icons.UPLOAD_FILE,
                    on_click=lambda _: pick_files_dialog.pick_files(
                        allow_multiple=True
                    ),
                ),
                selected_files,
            ]
        ),
#        Row(
#            [
#                ElevatedButton(
#                    "Save file",
#                    icon=icons.SAVE,
#                    on_click=lambda _: save_file_dialog.save_file(),
#                    disabled=page.web,
#                ),
#                save_file_path,
#            ]
#        ),
#        Row(
#            [
#                ElevatedButton(
#                    "Open directory",
#                    icon=icons.FOLDER_OPEN,
#                    on_click=lambda _: get_directory_dialog.get_directory_path(),
#                    disabled=page.web,
#                ),
#                directory_path,
#            ]
#        ),
    )



if __name__ == "__main__":
    ft.app(main, assets_dir="assets")
# Note: Make sure to install the flet library before running this code
# pip install flet
# This code creates a simple countdown timer using the Flet library.
# It includes a button to start the countdown and plays a sound when it reaches 0.
# The countdown starts from 10 and decrements every second.
# The countdown text is displayed in red and the button is disabled during the countdown.



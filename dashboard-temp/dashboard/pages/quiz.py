import reflex as rx
from reflex.components.radix import themes as rdxt

from dashboard.navigation import dashboard_sidebar, navbar
from dashboard.styles import BACKGROUND_COLOR, FONT_FAMILY
import requests
import json


class FormState(rx.State):
    form_data: dict = {}

    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data
        print(self.form_data)

def quiz() -> rx.Component:
    return rx.chakra.box(
        dashboard_sidebar,
        rx.chakra.box(
            navbar(heading="Quiz"),
            rx.chakra.box(
                rx.vstack(
                    # rx.form(
                        rdxt.text("Enter User ID"),
                        rx.vstack(
                            # rx.form(
                                rx.flex(
                                    rx.input(
                                        placeholder="User ID",
                                        name="user_id",
                                        id="user-id",
                                        type="number",
                                        required=True
                                    ),
                                    rx.button("Submit to see your memory card", id="userIdButton"),
                                    direction="row",
                                    spacing='3',
                                ),
                            #     on_submit=PhotoState.handle_submit, reset_on_submit=True
                            # ),
                            rx.spacer(spacing='8'),
                            rx.card(
                                rx.image(id='memory', sizes=3),
                                rdxt.text(hidden=True, id='memoryId'),
                                class_name='w-2/3'
                            ),
                            rdxt.text("Talk about this memory", size='5'),
                            rx.spacer(spacing='1'),
                            rx.flex(
                            rx.button("Start", id="startRecording"),
                            rx.button("Stop", id="stopRecording"),
                            rx.html("<canvas id='visualizerCanvas' width='700' height='50'></canvas>"),
                            direction='row',
                            justify='center',
                            align='center',
                            width='full',
                            spacing='3',
                            ),
                            rdxt.card(
                            rdxt.text("What you said:", size='2', class_name='w-full text-center'),
                            rdxt.text(id="transcript", size='4'),
                            class_name='bg-black'
                            ),
                                
                            rx.button("Submit", type="submit"),
                        ),
                    #     on_submit=FormState.handle_submit,
                    #     reset_on_submit=True,
                    # ),
                                        rx.script(src='/transcription.js')
                ),
                margin_top="calc(50px +  2em)",
                padding="3em",
            ),
            padding_left="250px",
        ),
        background_color=BACKGROUND_COLOR,
        font_family=FONT_FAMILY,
        padding_bottom="4em",
    )

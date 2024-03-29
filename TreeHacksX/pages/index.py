"""The index page."""

from TreeHacksX.templates import template
import reflex as rx
from .dashboard import TableState



@template(route="/", title="Index")
def index() -> rx.Component:

    return rx.chakra.Stack(
        direction="column",
        spacing="20",
        children=[
            rx.chakra.Stack(
                direction="column",
                spacing="20",
                children=[
                    rx.chakra.heading("Question  1", font_size="3em"),
                    rx.chakra.text("This is the first question in the quiz."),
                    rx.image(src="/assets/arcade.jpg", alt="An example image"),
                    rx.chakra.text("Here is a caption to go with the image."),
                    rx.chakra.text(
                        "Click the button below to describe when and where this memory is from"
                    ),
                    rx.html('<button id="startRecording">Start Recording</button><button id="stopRecording" disabled>Stop Recording</button><audio id="audioPlayer" controls></audio>'),
                    rx.html('<p id="transcript"></p>'),
                    rx.button("Click to talk", on_click=rx.call_script('myInitCode()')),

                    # rx.alert_dialog.root(
                    #     rx.alert_dialog.trigger(
                    #         rx.button("Click to talk"),
                    #     ),
                    #     rx.alert_dialog.content(
                    #         rx.html('<button id="startRecording">Start Recording</button><button id="stopRecording" disabled>Stop Recording</button><audio id="audioPlayer" controls></audio>'),
                    #         rx.alert_dialog.title("Talk in microphone"),
                    #         rx.button("Click to talk", on_click=rx.call_script('myInitCode()')),
                    #         rx.chakra.Spacer(height="5px"),
                    #         rx.alert_dialog.description(
                    #             "Now just talk out loud",
                    #         ),
                    #         rx.chakra.Spacer(height="20px"),  
                    #         rx.flex(
                    #             rx.alert_dialog.cancel(
                    #                 rx.button("Cancel"),
                    #             ),
                    #             rx.alert_dialog.action(
                    #                 rx.button(
                    #                     "Done"
                    #                 ),
                    #             ),
                    #             spacing="3",
                    #         ),
                    #     ),
                    # ),
                ]
            ),
            rx.chakra.Stack(
                direction="column",
                spacing="20",
                children=[
                    rx.chakra.heading("Question  2", font_size="3em"),
                    rx.chakra.text("This is the second question in the quiz."),
                    rx.image(src="/assets/arcade.jpg", alt="An example image"),
                    rx.chakra.text("Here is a caption to go with the image."),
                    rx.chakra.text(
                        "Click the button below to describe when and where this memory is from"
                    ),
                    rx.alert_dialog.root(
                        rx.alert_dialog.trigger(
                            rx.button("Click to talk"),
                        ),
                        rx.alert_dialog.content(
                            rx.alert_dialog.title("Talk in microphone"),
                            rx.chakra.Spacer(height="5px"),
                            rx.alert_dialog.description(
                                "Now just talk out loud",
                            ),
                            rx.chakra.Spacer(height="20px"),
                            rx.flex(
                                rx.alert_dialog.cancel(
                                    rx.button("Cancel"),
                                ),
                                rx.alert_dialog.action(
                                    rx.button("Done"),
                                ),
                                spacing="3",
                            ),
                        ),
                    ),
                    rx.script(src='/transcription.js')
                ]
            ),
            rx.chakra.Stack(
                direction="column",
                spacing="20",
                children=[
                    rx.chakra.heading("Question  3", font_size="3em"),
                    rx.chakra.text("This is the third question in the quiz."),
                    rx.image(src="/assets/arcade.jpg", alt="An example image"),
                    rx.chakra.text("Here is a caption to go with the image."),
                    rx.chakra.text(
                        "Click the button below to describe when and where this memory is from"
                    ),
                    rx.alert_dialog.root(
                        rx.alert_dialog.trigger(
                            rx.button("Click to talk"),
                        ),
                        rx.alert_dialog.content(
                            rx.alert_dialog.title("Talk in microphone"),
                            rx.chakra.Spacer(height="5px"),
                            rx.alert_dialog.description(
                                "Now just talk out loud",
                            ),
                            rx.chakra.Spacer(height="20px"),
                            rx.flex(
                                rx.alert_dialog.cancel(
                                    rx.button("Cancel"),
                                ),
                                rx.alert_dialog.action(
                                    rx.button("Done"),
                                ),
                                spacing="3",
                            ),
                        ),
                    ),
                ],
            ),
            rx.button("Submit", on_click=TableState.get_results),
        ],
    )

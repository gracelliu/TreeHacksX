import reflex as rx
from reflex.components.radix import themes as rdxt

from dashboard.navigation import dashboard_sidebar, navbar
from dashboard.styles import BACKGROUND_COLOR, FONT_FAMILY


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
                    rx.form(
                        rdxt.text("Enter User ID"),
                        rx.vstack(
                            rx.input(
                                placeholder="User ID",
                                name="user_id",
                                type="number",
                                required=True
                            ),
                            rx.spacer(spacing='8'),
                            rdxt.text("image"),
                            rx.spacer(spacing='8'),
                            rdxt.text("caption"),
                            rx.spacer(spacing='8'),
                            rdxt.text(
                                "click the button below to describe when and where this memory is from"),
                            rx.alert_dialog.root(
                                rx.alert_dialog.trigger(
                                    rx.button("Click to talk"),
                                ),
                                rx.alert_dialog.content(
                                    rx.alert_dialog.title(
                                        "Talk in microphone"),
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
                            rx.button("Submit", type="submit"),
                        ),
                        on_submit=FormState.handle_submit,
                        reset_on_submit=True,
                    ),
                    rx.text(FormState.form_data.to_string()),
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

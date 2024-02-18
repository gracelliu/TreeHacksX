import reflex as rx

from dashboard.navigation import dashboard_sidebar, navbar
from dashboard.styles import BACKGROUND_COLOR, FONT_FAMILY
from dashboard.components.chat import action_bar, chat

def friends() -> rx.Component:
    return rx.chakra.box(
        dashboard_sidebar,
        rx.chakra.box(
            navbar(heading="Friends"),
            rx.chakra.box(
                rx.text("Temp"),
                chat(),
                action_bar(),
                margin_top="calc(50px + 2em)",
                padding="2em",
            ),
            padding_left="250px",
        ),
        background_color=BACKGROUND_COLOR,
        font_family=FONT_FAMILY,
        padding_bottom="4em",
    )

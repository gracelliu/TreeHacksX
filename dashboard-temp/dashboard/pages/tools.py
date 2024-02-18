import reflex as rx
from reflex.components.radix import themes as rdxt

from dashboard.navigation import dashboard_sidebar, navbar
from dashboard.styles import BACKGROUND_COLOR, FONT_FAMILY


def quiz() -> rx.Component:
    return rx.chakra.box(
        dashboard_sidebar,
        rx.chakra.box(
            navbar(heading="Quiz"),
            rx.chakra.box(
                rdxt.text("placeholder"),
                margin_top="calc(50px + 2em)",
                padding="2em",
            ),
            padding_left="250px",
        ),
        background_color=BACKGROUND_COLOR,
        font_family=FONT_FAMILY,
        padding_bottom="4em",
    )

# idk just a placeholder for now
print("hello")
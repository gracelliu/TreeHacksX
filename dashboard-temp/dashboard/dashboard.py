"""The main Dashboard App."""

from rxconfig import config

import reflex as rx

from dashboard.styles import BACKGROUND_COLOR, FONT_FAMILY, THEME, STYLESHEETS

from dashboard.pages.friends import friends
from dashboard.pages.quiz import quiz
from dashboard.pages.index import index

# Create app instance and add index page.
app = rx.App(
    theme=THEME,
    stylesheets=STYLESHEETS,
)

app.add_page(index, route="/")
app.add_page(friends, route="/friends")
app.add_page(quiz, route="/quiz")

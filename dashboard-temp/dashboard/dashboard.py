"""The main Dashboard App."""

from rxconfig import config

import reflex as rx

from dashboard.styles import BACKGROUND_COLOR, FONT_FAMILY, THEME, STYLESHEETS

from dashboard.pages.friends import friends
from dashboard.pages.memory import quiz
from dashboard.pages.index import index

# Create app instance and add index page.
app = rx.App(
    theme=THEME,
    stylesheets=STYLESHEETS,
)

# async def get_photo_link(user_id: int):
#     client, conn = create_connection()
#     return get_photo(conn, user_id)
                        
# async def quiz_submit(client, conn, image_id: int, description: str, user_id: int):
#     client, conn = create_connection()
#     return check_similarity(client, conn, image_id, description, user_id)

# app.api.add_api_route("/photo", get_photo_link)
# app.api.add_api_route("/submit", quiz_submit)

app.add_page(index, route="/")
app.add_page(friends, route="/friends")
app.add_page(quiz, route="/memory")

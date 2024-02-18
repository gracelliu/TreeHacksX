import reflex as rx

from dashboard.navigation import dashboard_sidebar, navbar
from dashboard.styles import BACKGROUND_COLOR, FONT_FAMILY
from dashboard.components.chat import action_bar, chat

# from reflex.components.component import Component
# from typing import Any, Dict, List, Union
# from reflex.vars import Var

# from stream-chat import StreamChat


# class Chat(rx.Component):
#     library = "stream-chat-react"
#     tag = "Chat"
#     import os
#     api_key: rx.Var[str] = os.getenv("GETSTREAM_API_KEY")
#     secret_key = os.getenv("GETSTREAM_API_KEY")
#     is_default = True

#     def __init__(self):
#         super.__init__()
#         self.client = StreamChat(api_key=self.api_key, api_secret=self.secret_key)
#         self.token = self.client.create_token("user")

    
# class Channel(rx.Component):
#     library = "stream-chat-react"
#     tag = "Channel"
    
#     def __init__(self, ):



def friends() -> rx.Component:
    return rx.chakra.box(
        dashboard_sidebar,
        rx.chakra.box(
            navbar(heading="Friends"),
            rx.chakra.box(
                rx.text("Temp"),
                rx.html('<iframe src="http://127.0.0.1:4000">'),
                  # chat(),
                # action_bar(),
                margin_top="calc(50px + 2em)",
                padding="2em",
            ),
            padding_left="250px",
        ),
        background_color=BACKGROUND_COLOR,
        font_family=FONT_FAMILY,
        padding_bottom="4em",
    )

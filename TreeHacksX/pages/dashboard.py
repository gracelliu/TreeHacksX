"""The dashboard page."""
from TreeHacksX.templates import template

import reflex as rx
from typing import List


class TableState(rx.State):
    data: List = [
        ["Lionel", "Messi", "Lionel: Thanks for reaching out!"],
        ["Christiano", "Ronaldo", "You: Looks like we share"],
    ]
    columns: List[str] = ["First Name", "Last Name", "Last Message"]


@template(route="/dashboard", title="Dashboard")
def dashboard() -> rx.Component:
    """The dashboard page.

    Returns:
        The UI for the dashboard page.
    """
    data = [
        {"name": "Page A", "uv": 4000, "pv": 2400, "amt": 2400},
        {"name": "Page B", "uv": 3000, "pv": 1398, "amt": 2210},
        {"name": "Page C", "uv": 2000, "pv": 9800, "amt": 2290},
        {"name": "Page D", "uv": 2780, "pv": 3908, "amt": 2000},
        {"name": "Page E", "uv": 1890, "pv": 4800, "amt": 2181},
        {"name": "Page F", "uv": 2390, "pv": 3800, "amt": 2500},
        {"name": "Page G", "uv": 3490, "pv": 4300, "amt": 2100},
    ]

    data2 = [
    {"value": 100, "name": "Sent", "fill": "#8884d8"},
    {"value": 80, "name": "Viewed", "fill": "#83a6ed"},
    {"value": 50, "name": "Clicked", "fill": "#8dd1e1"},
    {"value": 40, "name": "Add to Cart", "fill": "#82ca9d"},
    {"value": 26, "name": "Purchased", "fill": "#a4de6c"},
]
    

    return rx.chakra.vstack(
        rx.chakra.heading("Dashboard", font_size="3em"),
        rx.chakra.text("Welcome to our app!"),
        rx.chakra.heading("Messageboard", font_size="1em"),
        rx.chakra.text(
            "Look at all your messages from the senior you paired best with!",
        ),
        rx.flex(
            rx.spacer(),
            rx.table.root(
                rx.table.body(
                    rx.table.row(
                        rx.table.cell(rx.avatar(fallback="DS")),
                        rx.table.row_header_cell(
                            rx.alert_dialog.root(
                                rx.alert_dialog.trigger(
                                    rx.button("Danilo Ricci"),
                                ),
                                rx.alert_dialog.content(
                                    rx.alert_dialog.title("Chat with Danilo"),
                                    rx.card(
                                        rx.link(
                                            rx.flex(
                                                rx.box(
                                                    rx.text(
                                                        "How are you, Joe?"
                                                    ),
                                                    rx.text(
                                                        "|"
                                                    ),
                                                    rx.text(
                                                        "Good Danilo, how r u?"
                                                    ),
                                                    rx.text(
                                                        "|"
                                                    ),
                                                    rx.text(
                                                        "Fine thank you"
                                                    )
                                                ),
                                                spacing="5",
                                            ),
                                        ),
                                        as_child=True
                                    ),
                                    rx.spacer(),
                                    rx.container(
                                        rx.input(placeholder="Type here..."),
                                        rx.button("Send",
                                                  color_scheme="red",
                                                  ),
                                        spacing='2',
                                        width='100%',
                                        flex_grow=1
                                    ),
                                    rx.spacer(),
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
                                size=4,
                            )
                        ),
                        rx.table.cell("danilo@example.com"),
                        rx.table.cell("Paris, France"),
                        align="center",
                    ),
                    rx.table.row(
                        rx.table.cell(rx.avatar(fallback="ZA")),
                        rx.table.row_header_cell(
                            rx.alert_dialog.root(
                                rx.alert_dialog.trigger(
                                    rx.button("Zahra Ambessa"),
                                ),
                                rx.alert_dialog.content(
                                    rx.alert_dialog.title("Chat with Zahra"),
                                    rx.card(
                                        rx.link(
                                            rx.flex(
                                                rx.box(
                                                    rx.text(
                                                        "How are you, Joe?"
                                                    ),
                                                    rx.text(
                                                        "|"
                                                    ),
                                                    rx.text(
                                                        "Good Zahra, how r u?"
                                                    ),
                                                    rx.text(
                                                        "|"
                                                    ),
                                                    rx.text(
                                                        "Fine thank you"
                                                    )
                                                ),
                                                spacing="5",
                                            ),
                                        ),
                                        as_child=True
                                    ),
                                    rx.spacer(),
                                    rx.container(
                                        rx.input(placeholder="Type here..."),
                                        rx.button("Send",
                                                  color_scheme="red",
                                                  ),
                                        spacing='2',
                                        width='100%',
                                        flex_grow=1
                                    ),
                                    rx.spacer(),
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
                                size=4,
                            )
                        ),
                        rx.table.cell("zahra@example.com"),
                        rx.table.cell("Tokyo, Japan"),
                        align="center",
                    ),
                    rx.table.row(
                        rx.table.cell(rx.avatar(fallback="JE")),
                        rx.table.row_header_cell(
                            rx.alert_dialog.root(
                                rx.alert_dialog.trigger(
                                    rx.button("Jasper Eriksson"),
                                ),
                                rx.alert_dialog.content(
                                    rx.alert_dialog.title("Chat with Jasper"),
                                    rx.card(
                                        rx.link(
                                            rx.flex(
                                                rx.box(
                                                    rx.text(
                                                        "How are you, Joe?"
                                                    ),
                                                    rx.text(
                                                        "|"
                                                    ),
                                                    rx.text(
                                                        "Good Jasper, how r u?"
                                                    ),
                                                    rx.text(
                                                        "|"
                                                    ),
                                                    rx.text(
                                                        "Fine thank you"
                                                    )
                                                ),
                                                spacing="5",
                                            ),
                                        ),
                                        as_child=True
                                    ),
                                    rx.spacer(),
                                    rx.container(
                                        rx.input(placeholder="Type here..."),
                                        rx.button("Send",
                                                  color_scheme="red",
                                                  ),
                                        spacing='2',
                                        width='100%',
                                        flex_grow=1
                                    ),
                                    rx.spacer(),
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
                                size=4,
                            )
                        ),
                        rx.table.cell("jasper@example.com"),
                        rx.table.cell("San Jose, CA"),
                        align="center",
                    ),
                ),
            ),
            direction="column",
            spacing="2",
        ),
        rx.chakra.heading("Chart 1", font_size="1em"),
        rx.recharts.area_chart(
            rx.recharts.area(
                data_key="uv", stroke="#8884d8", fill="#8884d8"
            ),
            rx.recharts.x_axis(data_key="Your Vitals"),
            rx.recharts.y_axis(),
            data=data,
        ),
        rx.chakra.heading("Chart 2", font_size="1em"),
        rx.recharts.bar_chart(
            rx.recharts.bar(
                data_key="uv", stroke="#8884d8", fill="#8884d8"
            ),
            rx.recharts.x_axis(data_key="name"),
            rx.recharts.y_axis(),
            data=data,
        ),
        rx.chakra.heading("Chart 3", font_size="1em"),
        rx.recharts.funnel_chart(
    rx.recharts.funnel(
        rx.recharts.label_list(
            position="right",
            data_key="name",
            fill="#000",
            stroke="none",
        ),
        rx.recharts.label_list(
            position="right",
            data_key="name",
            fill="#000",
            stroke="none",
        ),
        data_key="value",
        data=data2,
    ),
    rx.recharts.graphing_tooltip(),
    width=730,
    height=250,
)
    )

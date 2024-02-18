"""The main index page."""

import reflex as rx
from reflex.components.radix import themes as rdxt

from dashboard.data import (
    line_chart_data,
    lines,
    pie_chart_data,
    mood_lines,
    mood_chart_data,
    stat_card_data,
    bar_chart_data,
    bars,
    tabular_data,
    radar_chart_data,
)
from dashboard.graphs import (
    line_chart,
    pie_chart,
    stat_card,
    bar_chart,
    table,
    radar_chart
)
from dashboard.navigation import dashboard_sidebar, navbar
from dashboard.styles import BACKGROUND_COLOR, FONT_FAMILY


# Content in a grid layout.
def content_grid():
    return rx.chakra.grid(
        
        # Stat cards.
        *[rx.chakra.grid_item(stat_card(*c), col_span=1, row_span=1) for c in stat_card_data],
        
        # Cognitive performance line chart.
        rx.chakra.grid_item(
            rx.chakra.heading("Cognitive Performance Over Time", size="md"),
            line_chart(data=line_chart_data, data_key="name", lines=lines),
            col_span=4,
            row_span=2,
        ),

        # Remember vs dont remember cards Bar chart
        rx.chakra.grid_item(
            rx.chakra.heading("Daily Memory Recall Performance", size="md"),
            bar_chart(data=bar_chart_data, data_key="value", bars=bars),
            col_span=4,
            row_span=2,
        ),
        
        # Mood line chart.
        rx.chakra.grid_item(
            rx.chakra.heading("Mood over time", size="md"),
            line_chart(data=mood_chart_data, data_key="name", lines=mood_lines),
            col_span=4,
            row_span=2,
        ),
        
        # catergory Pie chart.
        rx.chakra.grid_item(
            rx.chakra.heading("Category of Memory Cards", size="md"),
            pie_chart(data=pie_chart_data, data_key="value", name_key="name"),
            col_span=4,
            row_span=3,
        ),

        # Radar chart
        rx.chakra.grid_item(
            rx.chakra.heading("Relative Memory Strengths per Category", size="md"),
            radar_chart(data=radar_chart_data),
            col_span=4,
            row_span=1,
        ),

        # friend table
        rx.chakra.grid_item(
            rx.chakra.heading("Friends", size="md"),
            table(tabular_data=tabular_data), col_span=4, row_span=2
        ),

        # formatting
        rx.chakra.grid_item(col_span=2, bg="lightgreen"),
        rx.chakra.grid_item(col_span=2, bg="yellow"),
        rx.chakra.grid_item(col_span=4, bg="orange"),
        template_columns="repeat(4, 1fr)",
        width="100%",
        gap=4,
        row_gap=8,
    )


def index() -> rx.Component:
    return rdxt.box(
        rx.theme_panel(),
        dashboard_sidebar,
        rx.chakra.box(
            navbar(heading="Dashboard"),
            rx.chakra.box(
                content_grid(),
                margin_top="calc(50px + 2em)",
                padding="2em",
            ),
            padding_left="250px",
        ),
        background_color=BACKGROUND_COLOR,
        font_family=FONT_FAMILY,
        padding_bottom="4em",
    )

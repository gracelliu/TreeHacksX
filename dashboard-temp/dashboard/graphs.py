"""Library of customized graphs and tables for the dashboard."""
import reflex as rx
from reflex.components.radix import themes as rdxt

def card(*children, **props):
    return rdxt.card(
        *children,
        box_shadow="rgba(0, 0, 0, 0.1) 0px 4px 6px -1px, rgba(0, 0, 0, 0.06) 0px 2px 4px -1px;",
        **props,
    )

# stat cards
def stat_card(title: str, stat, delta) -> rx.Component:
    color = "var(--red-9)" if delta[0] == "-" else "var(--green-9)"
    arrow = "decrease" if delta[0] == "-" else "increase"
    return card(
        rx.chakra.hstack(
            rx.chakra.vstack(
                rdxt.text(title),
                rx.chakra.stat(
                    rx.chakra.hstack(
                        rx.chakra.stat_number(stat, color=color),
                        rx.chakra.stat_help_text(rx.chakra.stat_arrow(type_=arrow), delta[1:]),
                    ),
                ),
            ),
        ),
    )

# contact table
def table(tabular_data: list[list]):
    return rdxt.table.root(
        rdxt.table.header(
            rdxt.table.row(
                *[rdxt.table.column_header_cell(cell) for cell in tabular_data[0]],
            ),
        ),
        rdxt.table.body(
            *[
                rdxt.table.row(
                    *[
                        rdxt.table.row_header_cell(cell)
                        if i == 0
                        else rdxt.table.cell(cell)
                        for i, cell in enumerate(row)
                    ],
                )
                for row in tabular_data[1:]
            ],
        ),
    )


# line chart
class Line(rx.Base):
    data_key: str
    stroke: str

def line_chart(data: rx.Var | list[dict], data_key: str, lines: list[Line]):
    return card(
        rx.recharts.line_chart(
            *[
                rx.recharts.line(data_key=line.data_key, stroke=line.stroke)
                for line in lines
            ],
            rx.recharts.x_axis(data_key=data_key),
            rx.recharts.y_axis(),
            rx.recharts.legend(),
            data=data,
            height=300,
        )
    )

# bar chart
class Bar(rx.Base):
        data_key: str
        fill: str

def bar_chart(data: rx.Var | list[dict], data_key: str, bars: list[Bar]):
    return card(
        rx.recharts.bar_chart(
            *[
                rx.recharts.bar(data_key=bar.data_key, fill=bar.fill)
                for bar in bars
            ],
        rx.recharts.x_axis(data_key="name"),
        rx.recharts.y_axis(name="number of cards"),
            rx.recharts.legend(),
            data=data,
            height=400,
        )
    )

# pie chart
def pie_chart(data: rx.Var | list[dict], data_key: str, name_key: str):
    return card(
        rx.recharts.pie_chart(
            rx.recharts.pie(
                data=data,
                data_key=data_key,
                name_key=name_key,
                cx="50%",
                cy="50%",
                label=True,
            ),
            rx.recharts.legend(),
            height=300,
        )
    )

# radar chart
class Radar(rx.Base):
    data_key: str
    stroke: str
    fill: str

def radar_chart(data):
    return card(
        rx.recharts.radar_chart(
            rx.recharts.radar(
            data_key="A",
            stroke="#8884d8",
            fill="#8884d8",
            ),
            rx.recharts.polar_grid(),
            rx.recharts.polar_angle_axis(data_key="topic"),
            data=data,
            height=400,
        )
    )


# class Area(rx.Base):
#     data_key: str
#     stroke: str
#     fill: str


# def area_chart(data: rx.Var | list[dict], data_key: str, areas: list[Area]):
#     return card(
#         rx.recharts.area_chart(
#             *[
#                 rx.recharts.area(
#                     data_key=area.data_key, stroke=area.stroke, fill=area.fill
#                 )
#                 for area in areas
#             ],
#             rx.recharts.x_axis(data_key=data_key),
#             rx.recharts.y_axis(),
#             rx.recharts.legend(),
#             data=data,
#             height=400,
#         )
#     )

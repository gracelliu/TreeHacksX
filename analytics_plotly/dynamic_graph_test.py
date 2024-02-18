import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
import numpy as np

# Generate a sample dataset
np.random.seed(42)  # For reproducibility
dates = pd.date_range(start="2024-01-01", periods=100, freq="D")
values = np.random.rand(100)  # Generate 100 random values

df = pd.DataFrame({"Date": dates, "Value": values})

# Initialize Dash app
app = dash.Dash(__name__)

# App layout
app.layout = html.Div(
    [
        dcc.DatePickerRange(
            id="date-picker-range",
            start_date=df["Date"].min(),
            end_date=df["Date"].max(),
            display_format="YYYY-MM-DD",
        ),
        dcc.Graph(id="graph"),
    ]
)


# Callback to update graph based on date selection
@app.callback(
    Output("graph", "figure"),
    [Input("date-picker-range", "start_date"), Input("date-picker-range", "end_date")],
)
def update_graph(start_date, end_date):
    # Filter dataframe based on selected date range
    filtered_df = df[(df["Date"] >= start_date) & (df["Date"] <= end_date)]

    # Create figure
    fig = go.Figure(
        data=go.Scatter(
            x=filtered_df["Date"], y=filtered_df["Value"], mode="lines+markers"
        )
    )

    # Update layout
    fig.update_layout(
        title="Value over Time",
        xaxis_title="Date",
        yaxis_title="Value",
        yaxis=dict(range=[0, 1]),
    )

    return fig


# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)

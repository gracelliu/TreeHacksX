import pandas as pd
import numpy as np

dummy_start_date = "2019-01-01"
dummy_end_date = "2021-10-03"
# date range from start date to end date and random
# column named value using amount of days as shape
dummy_df = pd.DataFrame(
    {
        "ds": pd.date_range(dummy_start_date, dummy_end_date),
        "value": np.random.randint(
            low=0,
            high=30,
            size=(
                pd.to_datetime(dummy_end_date) - pd.to_datetime(dummy_start_date)
            ).days
            + 1,
        ),
    }
)

from plotly_calplot import calplot

# creating the plot
fig = calplot(
    dummy_df,
    x="ds",
    y="value",
    gap=0,
    colorscale="blues",
    years_title=True,
    month_lines_width=3,
    month_lines_color="#000",
)
fig.show()

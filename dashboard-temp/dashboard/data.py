"""Mock data to populate the dashboard charts and tables."""

from dashboard.graphs import Line, Bar, Radar
from reflex.components.radix import themes as rdxt

# stat card
stat_card_data = [
    [
        "Cognitive Performance Score",
        "0.76",
        "-8%",
    ],
    [
        "Total Memory Cards Attempted",
        "26",
        "+7",
    ],
    [
        "Mood Today",
        "Sad",
        "-1",
    ],
    [
        "Top Memory Category",
        "Family & Relations",
        "0",
    ],
]

# line chart
line_chart_data = [
    {"name": "Mon, Feb 12", "Cosine Similarity Score": 0.1},
    {"name": "Tue, Feb 13", "Cosine Similarity Score": 0.6},
    {"name": "Wed, Feb 14", "Cosine Similarity Score": 0.3},
    {"name": "Thu, Feb 15", "Cosine Similarity Score": 0.2},
    {"name": "Fri, Feb 16", "Cosine Similarity Score": 0.35},
    {"name": "Sat, Feb 17", "Cosine Similarity Score": 0.15},
    {"name": "Sun, Feb 18", "Cosine Similarity Score": 0.45},
]

lines = [
    Line(data_key="Cosine Similarity Score", stroke="#8884d8"),
]

# another line chart
mood_chart_data = [
    {"name": "Mon, Feb 12", "Mood": -1},
    {"name": "Tue, Feb 13", "Mood": 0},
    {"name": "Wed, Feb 14", "Mood": 0},
    {"name": "Thu, Feb 15", "Mood": 1},
    {"name": "Fri, Feb 16", "Mood": -1},
    {"name": "Sat, Feb 17", "Mood": 1},
    {"name": "Sun, Feb 18", "Mood": 0},
]


########## fix
mood_lines = [
    Line(data_key="Mood", stroke="var(--green-7)"),
]
# this isnt that good. should have colour 



# pie chart
pie_chart_data = [
    {"name": "Health", "value": 27, "fill": "var(--red-7)"},
    {"name": "Family", "value": 46, "fill": "var(--green-7)"},
    {"name": "Retirement", "value": 14, "fill": "var(--purple-7)"},
    {"name": "Hobbies", "value": 13, "fill": "var(--blue-7)"},
    {"name": "Technology", "value": 8, "fill": "var(--yellow-7)"},
    {"name": "Housing", "value": 22, "fill": "var(--pink-7)"},
]

# bar chart
bar_chart_data = [
    {"name": "Mon, Feb 12", "Remember": 12, "Don\'t Remember": -4},
    {"name": "Tue, Feb 13", "Remember": 23, "Don\'t Remember": -7},
    {"name": "Wed, Feb 14", "Remember": 13, "Don\'t Remember": -18},
    {"name": "Thu, Feb 15", "Remember": 15, "Don\'t Remember": -9},
    {"name": "Fri, Feb 16", "Remember": 10, "Don\'t Remember": -5},
    {"name": "Sat, Feb 17", "Remember": 20, "Don\'t Remember": -10},
    {"name": "Sun, Feb 18", "Remember": 15, "Don\'t Remember": -5},
]

bars = [
    Bar(data_key="Remember", fill="var(--blue-7)"),
    # Bar(data_key="value", fill="var(--green-7)"),
    # Bar(data_key="value", fill="var(--purple-7)"),
    Bar(data_key="Don\'t Remember", fill="var(--red-7)"),
    # Bar(data_key="value", fill="var(--yellow-7)"),
    # Bar(data_key="value", fill="var(--pink-7)"),
]

radar_chart_data = [
    {
        "topic": "Health",
        "A": 83,
        "fullMark": 150,
    },
    {
        "topic": "Family",
        "A": 128,
        "fullMark": 150,
    },
    {
        "topic": "Retirement",
        "A": 86,
        "fullMark": 150,
    },
    {
        "topic": "Hobbies",
        "A": 65,
        "fullMark": 150,
    },
    {
        "topic": "Technology",
        "A": 12,
        "fullMark": 150,
    },
    {
        "topic": "Housing",
        "A": 90,
        "fullMark": 150,
    },
]

# tabular friends data
tabular_data = [
    ["Name", "Username", "Top Common Interest"],
    ["Brad Pita", "bradpita", rdxt.badge("Family")],
    ["Scarlet Johamster", "scarletjohamster", rdxt.badge("Health")],
    ["Leonardo DiCappuccino", "leonardodicappuccino", rdxt.badge("Retirement")],
    ["Taylor Swiss", "taylorswiss", rdxt.badge("Hobbies")],
    ["Katy Cherry", "katycherry", rdxt.badge("Housing")],
    ["Justin Thyme", "justinthyme", rdxt.badge("Technology")],
    ["Oprah Windfree", "oprahwindfre", rdxt.badge("Health")],
    ["Johnny Depth", "johnnydepth", rdxt.badge("Family")],
    ["Harry Stylesheet", "harrystylesheet", rdxt.badge("Retirement")]
]

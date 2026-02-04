import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px
from dash.dependencies import Input, Output


df = pd.read_csv("sales.csv")
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

fig = px.line(df,x="date",y="Sales",
    title="Pink Morsel Sales Over Time"
)


fig.update_traces(line=dict(width=3))
fig.update_layout(
    plot_bgcolor="white",
    paper_bgcolor="#f9f9f9",
    title_x=0.5,
    xaxis_title = "Date",
    yaxis_title = "Total Sales ($)"
)

app = dash.Dash(__name__)

app.layout = html.Div(
    style={
        "fontFamily": "Arial",
        "backgroundColor": "#f9f9f9",
        "padding": "30px"
    },
    children=[
        html.H1(
            "Soul Foods Pink Morsel Sales Dashboard",
            style={"textAlign": "center", "color": "#2c3e50"}
        ),

        dcc.RadioItems(
            id="region-selector",
            options=[
                {"label": "All", "value": "all"},
                {"label": "North", "value": "north"},
                {"label": "East", "value": "east"},
                {"label": "South", "value": "south"},
                {"label": "West", "value": "west"},
            ],
            value="all",
            labelStyle={"display": "inline-block", "margin-right": "20px"},
            style={"textAlign": "center", "marginBottom": "20px"}
        ),

        dcc.Graph(id="sales-line-chart")
    ]
)

@app.callback(
    Output("sales-line-chart", "figure"),
    Input("region-selector", "value")
)
def update_chart(selected_region):

    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["region"].str.lower() == selected_region]

    daily_sales = filtered_df.groupby("date", as_index=False)["Sales"].sum()

    fig = px.line(daily_sales, x="date", y="Sales")

    fig.update_layout(
        title="Pink Morsel Sales Over Time",
        xaxis_title="date",
        yaxis_title="Total Sales ($)"
    )

    return fig

if __name__ == "__main__":
    app.run(debug=True)

import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px

df = pd.read_csv("sales.csv")
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")
df = df.groupby("date", as_index=False)["Sales"].sum()

fig = px.line(df,x="date",y="Sales",
    title="Pink Morsel Sales Over Time"
)

fig.update_layout(
    xaxis_title="date",
    yaxis_title="Total Sales ($)"
)

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Soul Foods Pink Morsel Sales Visualiser"),

    dcc.Graph(
        id="sales-line-chart",
        figure=fig
    )
])
if __name__ == "__main__":
    app.run(debug=True)

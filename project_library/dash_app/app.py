import plotly.express as px
import dataiku
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

from dash_app.callbacks import *
from dash_app.components import *
from dash_app.style import *

def build_app(app):
    # This loads dummy data into a dataframe
    df = pd.DataFrame({
        "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
        "Amount": [4, 1, 2, 2, 4, 5],
        "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
    }) \
     \
    # Uncomment the following to read your own dataset
    #dataset = dataiku.Dataset("YOUR_DATASET_NAME_HERE")
    #df = dataset.get_dataframe()

    fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

    app.layout = html.Div(children=[
        html.H1(children='Hello Dash'),

        dcc.Graph(
            id='example-graph',
            figure=fig
        )
    ])
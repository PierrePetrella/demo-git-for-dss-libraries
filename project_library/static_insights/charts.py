import dataiku
from dataiku import insights
import plotly.express as px


def build_scatter_plot(df):
    df = px.data.iris()
    fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species")
    insights.save_plotly("plotly-insight", fig)


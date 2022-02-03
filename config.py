import dash
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
import requests
from dash import html, callback, Output, Input, dcc
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta
from dateutil.parser import parse


app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    # meta_tags=[
        # {'name': 'viewport', 'content': 'width=device-width, initial-scale=1.0, maximum-scale=1.2, minimum-scale=0.5,'}]
)
template = "plotly_dark"

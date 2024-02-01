import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output, callback
from Structure_and_Variables import *
import json

########################################################
# app code
app = Dash(__name__)

names = []
for loc in location:
    for com in comm_type:
        for prod in prod_type:
            for t in time:
                names.append(loc + '  ' + com + '  ' + prod + '  ' + t)

# json made by scraper.py
with open('info.json') as f:
    data_file = json.load(f)

app.layout = html.Div([
    html.Div("WASDE Data", className='Title', style={'font-size': '35px'}),
    html.Div(
        className='flex-element',
        children=[
            html.Br(),
            dcc.Checklist(
                id='checkbox',
                options=[{'label': i, 'value': i} for i in names],
                style={'max-height': '350px', 'overflow-y': 'auto'},
                value=names[0:2]
            ),
        ]),
    dcc.Graph(id='line-plot'),
    html.Div(className='info',
             children = [
                 html.P("- 2 Yr Actual refers to accurate numbers 2 years prior to date on graph"),
                 html.P("- Last Yr Est. refers to estimated numbers 1 year prior to date on graph"),
                 html.P("- This yr Projected refers to estimated numbers on this date on graph")
             ])
])


@callback(
    Output('line-plot', 'figure'),
    Input('checkbox', 'value'))
def update_graph(selected_data):
    # build initial frame with first element
    data = selected_data[0]
    look = data.split('  ')
    info = data_file \
        [look[0]] \
        [look[1]] \
        [look[2]] \
        [look[3]]

    first_data_dates = []
    first_data_values = []
    for i in range(len(info)):
        first_data_dates.append(info[i][0])
        first_data_values.append(info[i][1])
    for_frame = {'Date': first_data_dates, data: first_data_values}

    plot_df = pd.DataFrame(data=for_frame)
    plot_df.set_index('Date', inplace=True)
    name = selected_data[0]
    selected_data.pop(0)

    for data in selected_data:
        look = data.split('  ')
        info = data_file \
            [look[0]] \
            [look[1]] \
            [look[2]] \
            [look[3]]

        data_dates = []
        data_values = []
        for i in range(len(info)):
            data_dates.append(info[i][0])
            data_values.append(info[i][1])

        for_frame = {'Date': data_dates, data: data_values}
        input_df = pd.DataFrame(data=for_frame)
        input_df.set_index('Date', inplace=True)
        plot_df = pd.concat([plot_df, input_df], axis=1)

    plot_df.reset_index(inplace=True)
    Data_reverse = plot_df.iloc[::-1]
    selected_data.append(name)
    fig = px.line(Data_reverse, x='Date', y=selected_data, title='WASDE Graph')
    fig.update_layout(
        xaxis_title='Date',
        yaxis_title='Million Metric Tons',
        xaxis=dict(
            rangeslider=dict(
                visible=True
            ),
            type="category"
        )
    )
    return fig


if __name__ == '__main__':
    app.run(debug=False)

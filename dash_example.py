from dasher_src import initial_access, persistence, exfiltration, execution, privilege_escalation, credential_access, lateral_movement
import csv
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd


class open_csv():

    def __init__(self):
        pass

    def create_csv(self):
        fields = ["Name", "Counter"]
        rows = [[f"initial_access", f"{initial_access.initial_access()}"],
                [f"persistence", f"{persistence.persistence()}"], [f"exfiltration", f"{exfiltration.exfiltration()}"],
                [f"execution", f"{execution.execution()}"], [f"privilege_escalation", f"{privilege_escalation.privilege_escalation()}"],
                [f"credential_access", f"{credential_access.credential_access()}"], [f"lateral_movement", f"{lateral_movement.lateral_movement()}"]]
        filename = "dasher.csv"
        with open(filename, 'w') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(fields)
            csvwriter.writerows(rows)

#
# test = open_csv()
# test.create_csv()



df = pd.read_csv("dasher.csv")
mgr_options = df["Name"].unique()

app = dash.Dash()

app.layout = html.Div([
    html.H2("Technique Analytics - Mitre ATT&CK"),
    html.Div(
        [
            dcc.Dropdown(
                id="Technique",
                options=[{
                    'label': i,
                    'value': i
                } for i in mgr_options],
                value='All Techniques'),
        ],
        style={'width': '25%',
               'display': 'inline-block'}),
    dcc.Graph(id='funnel-graph'),
])


@app.callback(
    dash.dependencies.Output('funnel-graph', 'figure'),
    [dash.dependencies.Input('Technique', 'value')])
def update_graph(Manager):
    if Manager == "All Technique":
        df_plot = df.copy()
    else:
        df_plot = df[df['Name'] == Manager]

    pv = pd.pivot_table(
        df_plot,
        index=['Name'],
        columns=['Type'],
        values=['Counter'],
        aggfunc=sum,
        fill_value=0)

    trace1 = go.Bar(x=pv.index, y=pv[('Counter', "141")], name="initial_access")
    trace2 = go.Bar(x=pv.index, y=pv[('Counter', "193")], name="persistence")
    trace3 = go.Bar(x=pv.index, y=pv[('Counter', "145")], name="exfiltration")
    trace4 = go.Bar(x=pv.index, y=pv[('Counter', "159")], name="execution")
    trace5 = go.Bar(x=pv.index, y=pv[('Counter', "151")], name="privilege_escalation")
    trace6 = go.Bar(x=pv.index, y=pv[('Counter', "129")], name="credential_access")
    trace7 = go.Bar(x=pv.index, y=pv[('Counter', "129")], name="lateral_movement")



    return {
        'data': [trace1, trace2, trace3, trace4, trace5, trace6, trace7],
        'layout':
        go.Layout(
            title='Tools MITRE ATTACK'.format(Manager),
            barmode='stack')
    }


if __name__ == '__main__':
    app.run_server(debug=True)

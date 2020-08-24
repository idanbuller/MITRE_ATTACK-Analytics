from attackcti import attack_client
from dasher_src import initial_access, persistence, exfiltration, execution, privilege_escalation, credential_access, lateral_movement
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go


class Mitre():

    def __init__(self):
        pass

    def technique_analytics(self):
        tech = ['initial_access', 'persistence', 'exfiltration', 'execution', 'privilege_escalation', 'credential_access',
                'lateral_movement']

        fig1 = go.Figure([go.Bar(x=tech,
                                 y=[initial_access.initial_access(), persistence.persistence(), exfiltration.exfiltration(),
                                    execution.execution(), privilege_escalation.privilege_escalation(),
                                    credential_access.credential_access(), lateral_movement.lateral_movement()])])
        return fig1

    def tools(self):
        lift = attack_client()
        all_enterprise = lift.get_enterprise_tools()
        names = []
        urls = []
        for i in range(1, len(all_enterprise)):
            try:
                name = all_enterprise[i]["name"]
                description = all_enterprise[i]["description"]
                url = all_enterprise[i]["external_references"][0]["url"]
                names.append(name)
                urls.append(url)
                # print(f"Name: {name}\nDescription: {description}\nURL: {url}\n")
            except Exception as err:
                name = err
                description = err
                url = err
        fig2 = go.Figure(data=[go.Table(header=dict(values=['Name', 'URL']),
                                        cells=dict(values=[names, urls]))
                               ])
        return fig2

    def tools_detection(self):
        lift = attack_client()
        all_enterprise = lift.get_enterprise_tools()
        names = []
        height = []
        for i in range(1, len(all_enterprise)):
        # for i in range(0, 10):
            try:
                name = all_enterprise[i]["name"]
                times_detected = len(all_enterprise[i]["external_references"])
                names.append(name)
                height.append(times_detected)

            except Exception as err:
                name = err
                times_detected = err

        fig2 = go.Figure([go.Bar(x=names, y=height)])
        return fig2

    def techniques(self):
        lift = attack_client()
        all_enterprise = lift.get_enterprise_techniques()
        names = []
        urls = []
        for i in range(1, len(all_enterprise)):
            try:
                name = all_enterprise[i]["name"]
                description = all_enterprise[i]["description"]
                url = all_enterprise[i]["external_references"][0]["url"]
                names.append(name)
                urls.append(url)
                # print(f"Name: {name}\nDescription: {description}\nURL: {url}\n")
            except Exception as err:
                name = err
                description = err
                url = err
        fig3 = go.Figure(data=[go.Table(header=dict(values=['Name', 'URL']),
                                        cells=dict(values=[names, urls]))
                               ])
        return fig3

    def techniques_detection(self):
        lift = attack_client()
        all_enterprise = lift.get_enterprise_techniques()
        names = []
        height = []
        for i in range(1, len(all_enterprise)):
        # for i in range(0, 10):
            try:
                name = all_enterprise[i]["name"]
                times_detected = len(all_enterprise[i]["external_references"])
                names.append(name)
                height.append(times_detected)

            except Exception as err:
                name = err
                times_detected = err

        fig3 = go.Figure([go.Bar(x=names, y=height)])
        return fig3

    def malwares(self):
        lift = attack_client()
        all_enterprise = lift.get_enterprise_malware()
        names = []
        urls = []
        for i in range(1, len(all_enterprise)):
            try:
                name = all_enterprise[i]["name"]
                description = all_enterprise[i]["description"]
                url = all_enterprise[i]["external_references"][0]["url"]
                names.append(name)
                urls.append(url)
                # print(f"Name: {name}\nDescription: {description}\nURL: {url}\n")
            except Exception as err:
                name = err
                description = err
                url = err
        fig4 = go.Figure(data=[go.Table(header=dict(values=['Name', 'URL']),
                                        cells=dict(values=[names, urls]))
                               ])
        return fig4

    def malwares_detection(self):
        lift = attack_client()
        all_enterprise = lift.get_enterprise_malware()
        names = []
        height = []
        for i in range(1, len(all_enterprise)):
        # for i in range(0, 10):
            try:
                name = all_enterprise[i]["name"]
                times_detected = len(all_enterprise[i]["external_references"])
                names.append(name)
                height.append(times_detected)

            except Exception as err:
                name = err
                times_detected = err

        fig4 = go.Figure([go.Bar(x=names, y=height)])
        return fig4

    def groups(self):
        lift = attack_client()
        all_enterprise = lift.get_enterprise_groups()
        names = []
        urls = []
        for i in range(1, len(all_enterprise)):
            try:
                name = all_enterprise[i]["name"]
                description = all_enterprise[i]["description"]
                url = all_enterprise[i]["external_references"][0]["url"]
                names.append(name)
                urls.append(url)
                # print(f"Name: {name}\nDescription: {description}\nURL: {url}\n")
            except Exception as err:
                name = err
                description = err
                url = err
        fig5 = go.Figure(data=[go.Table(header=dict(values=['Name', 'URL']),
                                        cells=dict(values=[names, urls]))
                               ])
        return fig5

    def groups_detection(self):
        lift = attack_client()
        all_enterprise = lift.get_enterprise_groups()
        names = []
        height = []
        for i in range(1, len(all_enterprise)):
            # for i in range(0, 10):
            try:
                name = all_enterprise[i]["name"]
                times_detected = len(all_enterprise[i]["external_references"])
                names.append(name)
                height.append(times_detected)

            except Exception as err:
                name = err
                times_detected = err

        fig5 = go.Figure([go.Bar(x=names, y=height)])
        return fig5


colors = {
    'background': '#111111',
    'text': '#FF6347	'
}

test = Mitre()
app = dash.Dash()
app.layout = html.Div([
    html.H1("Technique Analytics - Mitre ATT&CK", style={'textAlign': 'center', 'color': colors['text']}),
    html.Br(),
    html.Br(),
    html.H2(
        "A cyber attack is any type of offensive action that targets computer information systems, infrastructures, computer networks or personal computer devices, using various methods to steal, alter or destroy data or information systems."),
    html.H2("WHAT is the most common attack technique? (Based on ATT&CK detection)"),
    dcc.Graph(figure=test.technique_analytics()),
    html.Br(),

    html.H2(f"All Tools - Mitre ATT&CK"),
    html.H3("Malicious Tools are malicious software programs that have been designed for automatically creating viruses, worms or Trojans , conducting DoS attacks on remote servers, hacking other computers, and more."),
    dcc.Graph(figure=test.tools()),
    html.H3(
        "How many times the tools detected?"),
    dcc.Graph(figure=test.tools_detection()),
    html.Br(),

    html.H2(f"All Techniques - Mitre ATT&CK"),
    html.H3(
        "In un-targeted attacks, attackers indiscriminately target as many devices, services or users as possible. They do not care about who the victim is as there will be a number of machines or services with vulnerabilities. To do this, they use techniques that take advantage of the openness of the Internet."),
    dcc.Graph(figure=test.techniques()),
    html.H3(
        "How many times the technique detected?"),
    dcc.Graph(figure=test.techniques_detection()),
    html.Br(),

    html.H2(f"All Malwares - Mitre ATT&CK"),
    html.H3(
        "Malware is any software intentionally designed to cause damage to a computer, server, client, or computer network(by contrast, software that causes unintentional harm due to some deficiency is typically described as a software bug). A wide variety of types of malware exist, including computer viruses, worms, Trojan horses, ransomware, spyware, adware, rogue software, and scareware."),
    dcc.Graph(figure=test.malwares()),
    html.H3(
        "How many times the malware detected?"),
    dcc.Graph(figure=test.malwares_detection()),
    html.Br(),

    html.H2(f"All Groups - Mitre ATT&CK"),
    html.H3(
        "APT groups try to steal data, disrupt operations or destroy infrastructure. Unlike most cyber criminals, APT attackers pursue their objectives over months or years. They adapt to cyber defenses and frequently retarget the same victim."),
    dcc.Graph(figure=test.groups()),
    html.H3(
        "How many times the group detected?"),
    dcc.Graph(figure=test.groups_detection()),
    html.Br(),
])

app.run_server(debug=True, use_reloader=False)

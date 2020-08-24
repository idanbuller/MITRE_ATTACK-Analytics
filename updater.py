from updater_src import groups, malwares, techniques, tools


class Mitre():

    def __init__(self):
        pass

    def groups(self):
        groups.groups()

    def malware(self):
        malwares.malware()

    def techniques(self):
        techniques.techniques()

    def tools(self):
        tools.tools()


bull = Mitre()
print("""
^^ Welcome to Mitre ATT&CK Updater ^^

You can be updated by the following:
1. New Groups
2. New Malware
3. New Techniques
4. New Tools""")
while True:
    user_input = str(input("\n>> Enter your choise: "))
    if user_input == "1":
        bull.groups()
    if user_input == "2":
        bull.malware()
    if user_input == "3":
        bull.techniques()
    if user_input == "4":
        bull.tools()
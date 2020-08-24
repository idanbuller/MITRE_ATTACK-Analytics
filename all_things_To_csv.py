from all_things_src import all_groups, all_malwares, all_techniques, all_tools


class Mitre():

    def __init__(self):
        pass

    def groups(self):
        all_groups.all_groups()

    def malware(self):
        all_malwares.all_malwares()

    def techniques(self):
        all_techniques.all_techniques()

    def tools(self):
        all_tools.all_tools()


bull = Mitre()
print("""
^^ Welcome to Mitre ATT&CK All-Retriever ^^

You can be print out the following:
1. All Groups
2. All Malwares
3. All Techniques
4. All Tools""")
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
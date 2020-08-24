from times_detected_src import groups_detection, malwares_detection, techniques_detection, tools_detection


class Mitre():

    def __init__(self):
        pass

    def groups(self):
        groups_detection.groups_detect()

    def malware(self):
        malwares_detection.malwares_detect()

    def techniques(self):
        techniques_detection.techniques_detect()

    def tools(self):
        tools_detection.tools_detect()


bull = Mitre()
print("""
^^ Welcome to Mitre ATT&CK Times Detector ^^

You can Count Detections of the following:
1. Groups
2. Malwares
3. Techniques
4. Tools""")
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
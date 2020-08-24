from attackcti import attack_client
from prettytable import PrettyTable


class Execution():

    def __init__(self):
        pass

    def execution(self):
        print("""

 _____                    _   _             
|  ___|                  | | (_)            
| |____  _____  ___ _   _| |_ _  ___  _ __  
|  __\ \/ / _ \/ __| | | | __| |/ _ \| '_ \ 
| |___>  <  __/ (__| |_| | |_| | (_) | | | |
\____/_/\_\___|\___|\__,_|\__|_|\___/|_| |_|


The adversary is trying to run malicious code.
Execution consists of techniques that result in adversary-controlled code running on a local or remote system. 
Techniques that run malicious code are often paired with techniques from all other tactics to achieve broader goals, like exploring a network or stealing data. 
For example, an adversary might use a remote access tool to run a PowerShell script that does Remote System Discovery.""")
        lift = attack_client()
        all_enterprise = lift.get_enterprise_techniques()
        preT = PrettyTable()
        for i in range(1, len(all_enterprise)):
            try:
                name = all_enterprise[i]["name"]
                # description = all_enterprise[i]["description"]
                phase_name = all_enterprise[i]["kill_chain_phases"][0]["phase_name"]
                url = all_enterprise[i]["external_references"][0]["url"]
                if "execution" == phase_name:
                    preT.field_names = ["Execution Technique", "Link"]
                    preT.add_row([f"{name}", f"{url}"])
            except KeyError as err:
                pass
        print(preT)


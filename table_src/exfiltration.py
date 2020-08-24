from attackcti import attack_client
from prettytable import PrettyTable


class Exfiltration():

    def __init__(self):
       pass

    def exfiltration(self):
        print("""

 _____      __ _ _ _             _   _             
|  ___|    / _(_) | |           | | (_)            
| |____  _| |_ _| | |_ _ __ __ _| |_ _  ___  _ __  
|  __\ \/ /  _| | | __| '__/ _` | __| |/ _ \| '_ \ 
| |___>  <| | | | | |_| | | (_| | |_| | (_) | | | |
\____/_/\_\_| |_|_|\__|_|  \__,_|\__|_|\___/|_| |_|


The adversary is trying to steal data.
Exfiltration consists of techniques that adversaries may use to steal data from your network. 
Once they’ve collected data, adversaries often package it to avoid detection while removing it. This can include compression and encryption. 
Techniques for getting data out of a target network typically include transferring it over their command and control channel or an alternate channel and may also include putting size limits on the transmission.""")

        lift = attack_client()
        all_enterprise = lift.get_enterprise_techniques()
        preT = PrettyTable()
        for i in range(1, len(all_enterprise)):
            try:
                name = all_enterprise[i]["name"]
                # description = all_enterprise[i]["description"]
                phase_name = all_enterprise[i]["kill_chain_phases"][0]["phase_name"]
                url = all_enterprise[i]["external_references"][0]["url"]
                if "exfiltration" == phase_name:
                    preT.field_names = ["Exfiltration Technique", "Link"]
                    preT.add_row([f"{name}", f"{url}"])
            except KeyError as err:
                pass
        print(preT)


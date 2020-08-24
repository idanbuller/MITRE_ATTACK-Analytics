from attackcti import attack_client
from prettytable import PrettyTable


class Privilege_escalation():

    def __init__(self):
        pass

    def privilege_escalation(self):
        print("""

______     _       _ _                   _____              _       _   _             
| ___ \   (_)     (_) |                 |  ___|            | |     | | (_)            
| |_/ / __ ___   ___| | ___  __ _  ___  | |__ ___  ___ __ _| | __ _| |_ _  ___  _ __  
|  __/ '__| \ \ / / | |/ _ \/ _` |/ _ \ |  __/ __|/ __/ _` | |/ _` | __| |/ _ \| '_ \ 
| |  | |  | |\ V /| | |  __/ (_| |  __/ | |__\__ \ (_| (_| | | (_| | |_| | (_) | | | |
\_|  |_|  |_| \_/ |_|_|\___|\__, |\___| \____/___/\___\__,_|_|\__,_|\__|_|\___/|_| |_|
                             __/ |                                                    
                            |___/                                             


The adversary is trying to gain higher-level permissions.
Privilege Escalation consists of techniques that adversaries use to gain higher-level permissions on a system or network. 
Adversaries can often enter and explore a network with unprivileged access but require elevated permissions to follow through on their objectives. 
Common approaches are to take advantage of system weaknesses, misconfigurations, and vulnerabilities. 
Examples of elevated access include: • SYSTEM/root level • local administrator • user account with admin-like access • user accounts with access to specific system or perform specific function. 
These techniques often overlap with Persistence techniques, as OS features that let an adversary persist can execute in an elevated context.""")

        lift = attack_client()
        all_enterprise = lift.get_enterprise_techniques()
        preT = PrettyTable()
        for i in range(1, len(all_enterprise)):
            try:
                name = all_enterprise[i]["name"]
                # description = all_enterprise[i]["description"]
                phase_name = all_enterprise[i]["kill_chain_phases"][0]["phase_name"]
                url = all_enterprise[i]["external_references"][0]["url"]
                if "privilege-escalation" == phase_name:
                    preT.field_names = ["Privilege Escalation Technique", "Link"]
                    preT.add_row([f"{name}", f"{url}"])
            except KeyError as err:
                pass
        print(preT)


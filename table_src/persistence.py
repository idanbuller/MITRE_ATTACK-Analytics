from attackcti import attack_client
from prettytable import PrettyTable


class Persistence():

    def __init__(self):
        pass

    def persistence(self):
        print("""

______             _     _                      
| ___ \           (_)   | |                     
| |_/ /__ _ __ ___ _ ___| |_ ___ _ __   ___ ___ 
|  __/ _ \ '__/ __| / __| __/ _ \ '_ \ / __/ _ \
| | |  __/ |  \__ \ \__ \ ||  __/ | | | (_|  __/
\_|  \___|_|  |___/_|___/\__\___|_| |_|\___\___|


The adversary is trying to maintain their foothold.
Persistence consists of techniques that adversaries use to keep access to systems across restarts, changed credentials, and other interruptions that could cut off their access. 
Techniques used for persistence include any access, action, or configuration changes that let them maintain their foothold on systems, such as replacing or hijacking legitimate code or adding startup code.""")

        lift = attack_client()
        all_enterprise = lift.get_enterprise_techniques()
        preT = PrettyTable()
        for i in range(1, len(all_enterprise)):
            try:
                name = all_enterprise[i]["name"]
                # description = all_enterprise[i]["description"]
                phase_name = all_enterprise[i]["kill_chain_phases"][0]["phase_name"]
                url = all_enterprise[i]["external_references"][0]["url"]
                if "persistence" == phase_name:
                    preT.field_names = ["Persistence Technique", "Link"]
                    preT.add_row([f"{name}", f"{url}"])
            except KeyError as err:
                pass
        print(preT)

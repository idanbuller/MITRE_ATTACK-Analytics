from attackcti import attack_client
from prettytable import PrettyTable


class Credential_access():

    def __init__(self):
        pass

    def credential_access(self):
        print("""

   _____              _            _   _       _                                 
  / ____|            | |          | | (_)     | |     /\                         
 | |     _ __ ___  __| | ___ _ __ | |_ _  __ _| |    /  \   ___ ___ ___  ___ ___ 
 | |    | '__/ _ \/ _` |/ _ \ '_ \| __| |/ _` | |   / /\ \ / __/ __/ _ \/ __/ __|
 | |____| | |  __/ (_| |  __/ | | | |_| | (_| | |  / ____ \ (_| (_|  __/\__ \__ \\
  \_____|_|  \___|\__,_|\___|_| |_|\__|_|\__,_|_| /_/    \_\___\___\___||___/___/


The adversary is trying to steal account names and passwords.
Credential Access consists of techniques for stealing credentials like account names and passwords. 
Techniques used to get credentials include keylogging or credential dumping. 
Using legitimate credentials can give adversaries access to systems, make them harder to detect, and provide the opportunity to create more accounts to help achieve their goals.""")
        lift = attack_client()
        all_enterprise = lift.get_enterprise_techniques()
        preT = PrettyTable()
        for i in range(1, len(all_enterprise)):
            try:
                name = all_enterprise[i]["name"]
                # description = all_enterprise[i]["description"]
                phase_name = all_enterprise[i]["kill_chain_phases"][0]["phase_name"]
                url = all_enterprise[i]["external_references"][0]["url"]
                if "credential-access" == phase_name:
                    preT.field_names = ["Credential Access Technique", "Link"]
                    preT.add_row([f"{name}", f"{url}"])
            except KeyError as err:
                pass
        print(preT)

from attackcti import attack_client
from prettytable import PrettyTable


class Initial_access():

    def __init__(self):
        pass

    def initial_access(self):
        print("""

 _____      _ _   _       _    ___                        
|_   _|    (_) | (_)     | |  / _ \                       
  | | _ __  _| |_ _  __ _| | / /_\ \ ___ ___ ___  ___ ___ 
  | || '_ \| | __| |/ _` | | |  _  |/ __/ __/ _ \/ __/ __|
 _| || | | | | |_| | (_| | | | | | | (_| (_|  __/\__ \__ \
 \___/_| |_|_|\__|_|\__,_|_| \_| |_/\___\___\___||___/___/


The adversary is trying to get into your network.
Initial Access consists of techniques that use various entry vectors to gain their initial foothold within a network. 
Techniques used to gain a foothold include targeted spearphishing and exploiting weaknesses on public-facing web servers. 
Footholds gained through initial access may allow for continued access, like valid accounts and use of external remote services, or may be limited-use due to changing passwords.""")
        lift = attack_client()
        all_enterprise = lift.get_enterprise_techniques()
        preT = PrettyTable()
        for i in range(1, len(all_enterprise)):
            try:
                name = all_enterprise[i]["name"]
                # description = all_enterprise[i]["description"]
                phase_name = all_enterprise[i]["kill_chain_phases"][0]["phase_name"]
                url = all_enterprise[i]["external_references"][0]["url"]
                if "initial-access" == phase_name:
                    preT.field_names = ["Initial Access Technique", "Link"]
                    preT.add_row([f"{name}", f"{url}"])
            except KeyError as err:
                pass
        print(preT)

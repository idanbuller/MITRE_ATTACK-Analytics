from attackcti import attack_client
from prettytable import PrettyTable


class Lateral_movement():

    def __init__(self):
        pass

    def lateral_movement(self):
        print("""

 _           _                 _  ___  ___                                    _   
| |         | |               | | |  \/  |                                   | |  
| |     __ _| |_ ___ _ __ __ _| | | .  . | _____   _____ _ __ ___   ___ _ __ | |_ 
| |    / _` | __/ _ \ '__/ _` | | | |\/| |/ _ \ \ / / _ \ '_ ` _ \ / _ \ '_ \| __|
| |___| (_| | ||  __/ | | (_| | | | |  | | (_) \ V /  __/ | | | | |  __/ | | | |_ 
\_____/\__,_|\__\___|_|  \__,_|_| \_|  |_/\___/ \_/ \___|_| |_| |_|\___|_| |_|\__|


The adversary is trying to move through your environment.
Lateral Movement consists of techniques that adversaries use to enter and control remote systems on a network. 
Following through on their primary objective often requires exploring the network to find their target and subsequently gaining access to it. 
Reaching their objective often involves pivoting through multiple systems and accounts to gain. 
Adversaries might install their own remote access tools to accomplish Lateral Movement or use legitimate credentials with native network and operating system tools, which may be stealthier.""")

        lift = attack_client()
        all_enterprise = lift.get_enterprise_techniques()
        preT = PrettyTable()
        for i in range(1, len(all_enterprise)):
            try:
                name = all_enterprise[i]["name"]
                # description = all_enterprise[i]["description"]
                phase_name = all_enterprise[i]["kill_chain_phases"][0]["phase_name"]
                url = all_enterprise[i]["external_references"][0]["url"]
                if "lateral-movement" == phase_name:
                    preT.field_names = ["Lateral Movement Technique", "Link"]
                    preT.add_row([f"{name}", f"{url}"])
            except KeyError as err:
                pass
        print(preT)

from attackcti import attack_client


def credential_access():
    lift = attack_client()
    all_enterprise = lift.get_enterprise_techniques()
    counter = 0
    for i in range(1, len(all_enterprise)):
        try:
            # name = all_enterprise[i]["name"]
            # description = all_enterprise[i]["description"]
            phase_name = all_enterprise[i]["kill_chain_phases"][0]["phase_name"]
            # url = all_enterprise[i]["external_references"][0]["url"]
            if "credential_access" == phase_name:
                counter += 1
        except KeyError as err:
            counter += 1
    return counter
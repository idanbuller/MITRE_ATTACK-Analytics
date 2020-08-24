from attackcti import attack_client


def tools():
    lift = attack_client()
    all_enterprise = lift.get_enterprise_tools()
    if len(all_enterprise) - 60 != 0:
        print("There is a new MALWARE!")
        created = all_enterprise[0]["created"]
        name = all_enterprise[0]["name"]
        description = all_enterprise[0]["description"]
        print(f"Created: {created}\nName: {name}\nDescription: {description}")

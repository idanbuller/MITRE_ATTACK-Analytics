from attackcti import attack_client

def techniques():
    lift = attack_client()
    all_enterprise = lift.get_enterprise_techniques()
    if len(all_enterprise) - 567 != 0:
        print("There is a new TECHNIQUE!")
        created = all_enterprise[0]["created"]
        name = all_enterprise[0]["name"]
        description = all_enterprise[0]["description"]
        print(f"Created: {created}\nName: {name}\nDescription: {description}")

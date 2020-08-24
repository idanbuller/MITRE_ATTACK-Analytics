from attackcti import attack_client


def groups():
    lift = attack_client()
    all_enterprise = lift.get_enterprise_groups()
    if len(all_enterprise) - 107 != 0:
        print("There is a new ATT&CKing group!")
        created = all_enterprise[0]["created"]
        name = all_enterprise[0]["name"]
        description = all_enterprise[0]["description"]
        print(f"Created: {created}\nName: {name}\nDescription: {description}")

from attackcti import attack_client
import csv


def all_tools():
    filename = "tools.csv"
    fields = ["Name", "Description", "URL"]
    rows = []
    lift = attack_client()
    all_enterprise = lift.get_enterprise_tools()
    for i in range(1, len(all_enterprise)):
        try:
            name = all_enterprise[i]["name"]
            description = all_enterprise[i]["description"]
            url = all_enterprise[i]["external_references"][0]["url"]
            # print(f"Name: {name}\nDescription: {description}\nURL: {url}\n")
            rows.append([name, description, url])
        except Exception as err:
            name = err
            description = err
            url = err
    with open(filename, 'w', encoding="utf-8") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(rows)



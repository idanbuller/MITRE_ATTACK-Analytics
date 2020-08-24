from attackcti import attack_client
import matplotlib.pyplot as plt


def tools_detect():
    lift = attack_client()
    all_enterprise = lift.get_enterprise_tools()

    # left = list(range(1, len(all_enterprise) - 1))
    left = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    height = []
    tick_label = []

    # for i in range(1, len(all_enterprise)):
    for i in range(0, 10):
        try:
            name = all_enterprise[i]["name"]
            times_detected = len(all_enterprise[i]["external_references"])
            tick_label.append(name)
            height.append(times_detected)

        except Exception as err:
            name = err
            times_detected = err

    plt.bar(left, height, tick_label=tick_label,
            width=0.8, color=['red'])

    plt.xlabel('Tool Name')
    plt.ylabel('Times Detected')
    plt.title('Tools Detection Analytics!')
    plt.show()


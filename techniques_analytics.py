from techniques_analytics_src import initial_access, persistence, exfiltration, execution, privilege_escalation, credential_access, lateral_movement
import matplotlib.pyplot as plt


class Technique_analytics():

    def __init__(self):
        self.left = [1, 2, 3, 4, 5, 6, 7]
        self.height = []
        self.tick_label = ["Initial Access", "Persistence", "Exfiltration", "Execution", "Privilege_Escalation", "Credential_Access", "Lateral_Movement"]

    def chart(self):
        self.height.append(initial_access.initial_access())
        self.height.append(persistence.persistence())
        self.height.append(exfiltration.exfiltration())
        self.height.append(execution.execution())
        self.height.append(privilege_escalation.privilege_escalation())
        self.height.append(credential_access.credential_access())
        self.height.append(lateral_movement.lateral_movement())

        plt.bar(self.left, self.height, tick_label=self.tick_label,
                width=0.8, color=['orange'])

        plt.xlabel('Technique')
        plt.ylabel('Times Detected')
        plt.title('Mitre ATT&CK Techniques Detection Analytics!')
        plt.show()


test = Technique_analytics()
test.chart()

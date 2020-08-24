from table_src import credential_access, execution, initial_access, lateral_movement, persistence, privilege_escalation



class Table_view():


      def __init__(self):
            pass

      def credential_access(self):
            credential_access.Credential_access.credential_access(self)

      def execution(self):
            execution.Execution.execution(self)

      def initial_access(self):
            initial_access.Initial_access.initial_access(self)

      def lateral_movement(self):
            lateral_movement.Lateral_movement.lateral_movement(self)

      def persistence(self):
            persistence.Persistence.persistence(self)

      def privilege_escalation(self):
            privilege_escalation.Privilege_escalation.privilege_escalation(self)


bull = Table_view()
print("""
^^ Welcome to Mitre ATT&CK Table-Retriever ^^

You can be print out the following:
1. Credential Access
2. Execution
3. Initial Access
4. Lateral Movement
5. Persistence
6. Privilege Escalation""")

while True:
    user_input = str(input("\n>> Enter your choise: "))
    if user_input == "1":
        bull.credential_access()
    if user_input == "2":
        bull.execution()
    if user_input == "3":
        bull.initial_access()
    if user_input == "4":
        bull.lateral_movement()
    if user_input == "5":
        bull.persistence()
    if user_input == "6":
        bull.privilege_escalation()

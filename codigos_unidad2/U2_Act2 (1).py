class accountant:
    def generate_report(self):
        print("Generating financial report")

class technician:
    def repair_machine(self):
        print("Repairing machine")

class boss(accountant, technician):
    pass

boss1 = boss()
boss1.generate_report()
boss1.repair_machine()
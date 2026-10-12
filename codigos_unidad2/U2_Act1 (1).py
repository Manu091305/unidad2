class employee: 
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_info(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

class manager(employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary, department)
        self.department = department

    def show_info(self):
        print(f"Name: {self.name}, Salary: {self.salary}, Department: {self.department}")

manager1 = manager("Laura", 60000, "Networking")
manager1.show_info()
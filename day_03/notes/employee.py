class Employee:
    """Class representation for employee data"""
    def __init__(self, name, id, time_in, time_out):
        self.name = name
        self.id = id
        self.tasks = []
        print(f"Employee {self.name} created with ID {self.id} Time-in:{time_in} Time-out:{time_out}")

    def add_work(self, task):
        self.tasks.append(task)
        
class Recruiter(Employee):
    def __init__(self, name, id, time_in, time_out):
        super().__init__(name, id, time_in, time_out)

    def recruit(self):
        print("Recruit")

class Developer(Employee):
    def __init__(self,name, id, time_in, time_out):
        super().__init__(name, id, time_in, time_out)

    def developer(self ):
        print("Code")

class Manager(Employee):
    def __init__(self,name, id, time_in, time_out):
        super().__init__(name, id, time_in, time_out)

    def manager(self):
        print("Manage")

employee1 = Employee("Jayson", "1234", "8am", "5pm")
manager = Manager("Jake", "12345", "6am", "2pm")
manager.manager()












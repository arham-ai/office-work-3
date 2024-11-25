from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def set_name(self, new_name):
        pass

    @abstractmethod
    def set_salary(self, new_salary):
        pass

# Create a concrete subclass of Employee
class ConcreteEmployee(Employee):
    def set_name(self, new_name):
        self.name = new_name

    def set_salary(self, new_salary):
        self.salary = new_salary

# Create an object emp of ConcreteEmployee  
emp = ConcreteEmployee()

# Use set_name to set the name of emp to 'Korel Rossi'
emp.set_name('Korel Rossi')

# Set the salary of emp to 50000
emp.set_salary(50000)

# Print the name and salary to verify
print(f"Employee Name: {emp.name}")
print(f"Employee Salary: {emp.salary}")


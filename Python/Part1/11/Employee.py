class Employee():
    """
    Class which describe employee (name and price).
    """
    def __init__(self, first_name, last_name, salary):
        """Initial employee's name and salary"""
        self.first = first_name
        self.last = last_name
        self.salary = salary
    
    def give_raise(self, my_raise=5000):
        """Salary raise"""
        self.salary += my_raise
    
    def show_salary(self):
        """Show result salary"""
        print(str(self.salary))
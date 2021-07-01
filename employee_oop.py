'''
Design a system to reflect a company where each employee has the following attributes:
+ First name
+ Last name
+ Salary
+ Title
+ Manager

There are different types of employees with different tasks:
For example for the same performTask():
+ Network Engineer:
 print "working in Data Center"
+ Software Engineer:
 print "typing code"
+ Manager:
 print "manage employee <List FirstName of employees that directly managed by this manager>"

 Followup: getSalaries() -> return sum salaries this employee and all employees that directly or undirectly managed by the manager
'''


from abc import abstractmethod


class Employee:
	
    def __init__(self, fname, lname, salary, title, manager):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        self.title = title
        self.manager = manager		

        
    def __repr__(self):
        return f'<{self.fname} {self.lname}, title: {self.title}>'


    @abstractmethod
    def perform_task():
        pass
        #to be implemented


class SoftWareEng(Employee):
    
    def __init__(self, fname, lname, salary, title, manager, languages=[]):
        super().__init__(fname, lname, salary, title, manager)
        self.languages = languages
        if manager:
            manager.employees.append(self)


    def __repr__(self):
        return f'<[SWE] {self.fname} {self.lname}>'


    def perform_task(self):
        print("Typing code")


class NetworkEng(Employee):

    def __init__(self, fname, lname, salary, title, manager, api_level):
        super().__init__(fname, lname, salary, title, manager)
        self.api_level = api_level


    def perform_task():
        print("Working in Data Center")


    def fixing_router():
        print("Fixing router")


class Manager(Employee):

    def __init__(self, fname, lname, salary, title, manager, employees=[]):
        super().__init__(fname, lname, salary, title, manager)
        self.employees = employees

    def assign_reportee(self, employee):
        self.employees.append(employee)

    def perform_task(self):
        ''' manage employee <List FirstName of employees that directly managed by this manager>'''

        employee_fnames = []

        for employee in self.employees:
            employee_fnames.append(employee.fname)
        
        print(f'Manage emloyees {employee_fnames}')


mgr1 = Manager("A", "Ng", 100, "CEO", None)
swe1 = SoftWareEng("B", "Smith", 80, "swe", mgr1, ['python'])
# mgr1.employees.append(swe1)



#===== Resources =====
'''
Example of using super's method: https://github.com/Lynguyen237/oo-melons/blob/master/melons.py
https://fellowship.hackbrightacademy.com/materials/pt7g/lectures/classes-2/ 

Abstract base classes: https://www.python-course.eu/python3_abstract_classes.php
'''
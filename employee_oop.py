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
        
    @abstractmethod
    def perform_task():
        pass
        #to be implemented


class SoftWareEng(Employee):
    def __init__(self, languages=[]):
        self.languages = languages


    def perform_task(self):
        print("Typing code")


class NetworkEng(Employee):
    def __init__(self, api_level):
        # super().__init__()
        self.api_level = api_level

    def perform_task():
        print("Working in Data Center")

    def fixing_router():
        print("Fixing router")


class Manager(Employee):
    def __init__(self, employees):
        self.employees = employees

    # def perform_task()
    # Print “”

swe = SoftWareEng('python')



#===== Resources =====


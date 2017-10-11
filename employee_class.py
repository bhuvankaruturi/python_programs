class Employee:

    def __init__(self, name, age, salary, location):
        self.name = name
        self.age = age
        self.salary = salary
        self.location = location
        print('New Employee has been created successfully!')

    def printDetails(self):
        print('Name:',self.name)
        print('Age:',self.age)
        print('salary:',self.salary)
        print('Location:',self.location)

    def getAnnualSalary(self):
        x = self.salary * 12
        print('Annual earnings of the employee:',x)
    

print('Execution started')

bhuvan = Employee('Bhuvan',21,150000,'Hyderabad')
tejaswini = Employee('Tejaswini',22,150000,'Hyderabad')

bhuvan.printDetails()
bhuvan.getAnnualSalary()

print('**************')

tejaswini.printDetails()
tejaswini.getAnnualSalary()

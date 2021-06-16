class Employee:
    def __init__(self,first,last,empid,pay):
        self.first=first
        self.last=last
        self.empid=empid
        self.pay=pay
        self.display()
    
    def display(self):
        print(self.first)
        print(self.last)
        print(self.empid)
        
